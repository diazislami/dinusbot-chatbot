import json
import random
import string
import numpy as np
import pickle
import tensorflow as tf
from nlp_id.lemmatizer import Lemmatizer
from nlp_id.stopword import StopWord
from tensorflow import keras
from tensorflow.keras.preprocessing.sequence import pad_sequences


# import dataset answer
def load_response():
    responses = {}
    with open('dataset/intents.json') as content:
        data = json.load(content)
    for intent in data['intents']:
        responses[intent['tag']] = intent['responses']
    return responses

# hapus tanda baca
def remove_punctuation(text):
    text = [letters.lower() for letters in text if letters not in string.punctuation]
    text = ''.join(text)
    return text

# removal stopwords
def removal_stopwords(text):
    stopword = StopWord()
    text = stopword.remove_stopword(text)
    return text

# lematisasi
def lemmatization(text):
    text_p = []
    lemmatizer = Lemmatizer()
    text = lemmatizer.lemmatize(text)
    text_p.append(text)
    return text_p

# mengubah text menjadi vector
def vectorization(texts_p):
    input_shape = 20
    tokenizer = pickle.load(open('model/tokenizers.pkl', 'rb'))
    vector = tokenizer.texts_to_sequences(texts_p)
    vector = np.array(vector).reshape(-1)
    vector = pad_sequences([vector], input_shape)
    return vector

# klasifikasi pertanyaan user
def predict(vector):
    prob = 0.9 # -> perlu di-tunning
    responses = load_response()
    model = keras.models.load_model('model/chat_model.h5')
    le = pickle.load(open('model/labelencoder.pkl', 'rb'))
    output = model.predict(vector)
    output_prob = round(output.max(), 4)
    output = output.argmax()
    print(output_prob)

    if output_prob > prob:
        response_tag = le.inverse_transform([output])[0]
        response = random.choice(responses[response_tag])
        return response
    else:
        return 'Maaf, aku tidak mengerti pertanyaanmu'

# menghasilkan jawaban berdasarkan pertanyaan user
def get_response(msg):
    answer = remove_punctuation(msg)
    answer = lemmatization(answer)
    answer = vectorization(answer)
    answer = predict(answer)
    return answer
