from flask import Flask, jsonify, request
from keras.models import load_model
# from sklearn.externals import joblib
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd

from nltk.tokenize import TweetTokenizer # doesn't split at apostrophes
import nltk
from nltk import Text
from nltk.tokenize import regexp_tokenize
from nltk.tokenize import word_tokenize  
from nltk.tokenize import sent_tokenize 
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer


# import cv2
import base64
import os
import re
import pickle

def clean_text(text):
    text = text.lower()
    text = re.sub(r"what's", "what is ", text)
    text = re.sub(r"\'s", " ", text)
    text = re.sub(r"\'ve", " have ", text)
    text = re.sub(r"can't", "can not ", text)
    text = re.sub(r"n't", " not ", text)
    text = re.sub(r"i'm", "i am ", text)
    text = re.sub(r"\'re", " are ", text)
    text = re.sub(r"\'d", " would ", text)
    text = re.sub(r"\'ll", " will ", text)
    text = re.sub(r"\'scuse", " excuse ", text)
    #text = re.sub('\W', ' ', text)
    #text = re.sub('\s+', ' ', text)
    text = text.strip(' ')
    return text

app = Flask(__name__, static_url_path='/static') #panggil modul flask
mapping = {
	"[0]":"Role in Scale",
	"[1]":"Patches",
	"[2]":"Crazing",
	"[3]":"Pitt Surface",
	"[4]":"Inclusion",
	"[5]":"Scratces",
	"[6]":"Scratch Patches",
	"[7]":"Role Patches",
	"[8]":"Ground Ground"
}
	
@app.route('/inference/', methods=['GET', 'OPTIONS'])
def inference():
	#PROGRAM DEEP LEARNING
	hasil = ""
	model = load_model('static/model.h5')
	#im = cv2.imread('static/inclusion_13.jpg')
	im = cv2.imread('static/crazing_1.jpg')
	im = cv2.resize(im,(32,32))
	im = np.array(im) #change image into array
	X_test = []
	X_test.append(np.array(im))
	y_pred = model.predict_classes([X_test])
	#END PROGRAM DEEP LEARNING
	hasil = {"status":"200", "hasil":mapping.get(str(y_pred))} #JSON OUT
	return jsonify(hasil) #RETURN KEPADA yang panggil

def save(encoded_data, filename):
	# nparr = np.fromstring(base64.b64decode(encoded_data), np.uint8)
	# img = cv2.imdecode(nparr, cv2.IMREAD_ANYCOLOR)
	# return cv2.imwrite(filename, img)
    f = open(filename, "x")
    f.write(text)
    f.close

@app.route('/post_inference/',methods=['POST','OPTIONS'])
def post_inference():
	data = request.json
	text = data["text"]
	# save(text, "coba.txt")
	f = open("coba.txt", "w")
	f.write(text)
	hasil = ""

    # Preprocessing Vectorizer
	tfidf = TfidfVectorizer(stop_words ='english', smooth_idf=False, sublinear_tf=False, norm=None, analyzer='word')
	movies = pd.read_csv('Preprocessed_Movies.csv')
	movies['PlotCleaned'] = movies['Plot'].apply(clean_text)
	MoviesTrain, MoviesTest = train_test_split(movies, random_state=42, test_size=0.30, shuffle=True)
	x_train = tfidf.fit_transform(MoviesTrain.PlotCleaned)
	f = open("coba.txt", "r")
	txt = f.read()
	txt = txt.replace('\n',' ').replace('\r','') 
	txt = clean_text(txt)
	txt = [txt]
	x_test  = tfidf.transform(txt)

	Genre = ['Action', 'Adult', 'Animation', 'Biography', 'Black', 'Children', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'History', 'Musical', 'Mistery', 'Political', 'Romance', 'Series', 'Short', 'Sports', 'Thriller']
	temp = []

#Model Action
	model = joblib.load('models/action.pkl')
	pred = model.predict(x_test)

	if pred == 1:
		temp.append('Action ')
#Model Adult
	model = joblib.load('models/adult.pkl')
	pred = model.predict(x_test)

	if pred == 1:
		temp.append('Adult ')

#Model Animation
	model = joblib.load('models/animation.pkl')
	pred = model.predict(x_test)

	if pred == 1:
		temp.append('Animation ')

#Model Biography
	model = joblib.load('models/biography.pkl')
	pred = model.predict(x_test)

	if pred == 1:
		temp.append('Biography ')

#Model Black
	model = joblib.load('models/black.pkl')
	pred = model.predict(x_test)

	if pred == 1:
		temp.append('Black ')

#Model Children
	model = joblib.load('models/children.pkl')
	pred = model.predict(x_test)

	if pred == 1:
		temp.append('Children ')

#Model Comedy
	model = joblib.load('models/comedy.pkl')
	pred = model.predict(x_test)

	if pred == 1:
		temp.append('Comedy ')

#Model Crime
	model = joblib.load('models/crime.pkl')
	pred = model.predict(x_test)

	if pred == 1:
		temp.append('Crime ')

#Model Documentary
	model = joblib.load('models/documentary.pkl')
	pred = model.predict(x_test)

	if pred == 1:
		temp.append('Documentary ')

#Model Drama
	model = joblib.load('models/drama.pkl')
	pred = model.predict(x_test)

	if pred == 1:
		temp.append('Drama ')

#Model Fantasy
	model = joblib.load('models/fantasy.pkl')
	pred = model.predict(x_test)

	if pred == 1:
		temp.append('Fantasy ')

#Model History
	model = joblib.load('models/history.pkl')
	pred = model.predict(x_test)

	if pred == 1:
		temp.append('History ')

#Model Musical
	model = joblib.load('models/musical.pkl')
	pred = model.predict(x_test)

	if pred == 1:
		temp.append('Musical ')

#Model Mystery
	model = joblib.load('models/mystery.pkl')
	pred = model.predict(x_test)

	if pred == 1:
		temp.append('Mystery ')

#Model Political
	model = joblib.load('models/political.pkl')
	pred = model.predict(x_test)

	if pred == 1:
		temp.append('Political ')

#Model Romance
	model = joblib.load('models/romance.pkl')
	pred = model.predict(x_test)

	if pred == 1:
		temp.append('Romance ')

#Model Series
	model = joblib.load('models/series.pkl')
	pred = model.predict(x_test)

	if pred == 1:
		temp.append('Series ')

#Model Short
	model = joblib.load('models/short.pkl')
	pred = model.predict(x_test)

	if pred == 1:
		temp.append('Short ')

#Model Sports
	model = joblib.load('models/sports.pkl')
	pred = model.predict(x_test)

	if pred == 1:
		temp.append('Sports ')

#Model Thriller
	model = joblib.load('models/thriller.pkl')
	pred = model.predict(x_test)

	if pred == 1:
		temp.append('Thriller ')

	hasil = ''.join(temp)
	print(temp)
	print(len(temp))

	# for i in range (len(temp)):
		# hasil.append(Genre[temp[i]])
		# print(Genre[temp[i]])

	# print np.fromstring(ts,dtype=int)
	# X_test = []
	# X_test.append(np.array(im))
	# y_pred = model.predict([x_test])
	# hasil = {"status":"200", "hasil":mapping.get(str(y_pred))} #JSON OUT
	hasil = {"status":"200", "hasil": hasil} #JSON OUT
	return jsonify(hasil)

if __name__ == '__main__': #RUN PROGRAM
	app.run(host='127.0.0.1', port=5005) #LOCALHOST, 5005