import bs4 as bs
import urllib.request
import nltk
import re
nltk.download('punkt')
#Open the cat web data page
cat_data = urllib.request.urlopen('https://simple.wikipedia.org/wiki/Cat').read()
#Find all the paragraph html from the web page
cat_data_paragraphs  = bs.BeautifulSoup(cat_data,'lxml').find_all('p')
#Creating the corpus of all the web page paragraphs
cat_text = ''
#Creating lower text corpus of cat paragraphs
for p in cat_data_paragraphs:
    cat_text += p.text.lower()
print(cat_text)
cat_text = re.sub(r'\s+', ' ',re.sub(r'\[[0-9]*\]', ' ', cat_text))
cat_sentences = nltk.sent_tokenize(cat_text)
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
def chatbot_answer(user_query):
    #Append the query to the sentences list
    cat_sentences.append(user_query)
    #Create the sentences vector based on the list
    vectorizer = TfidfVectorizer()
    sentences_vectors = vectorizer.fit_transform(cat_sentences)    
    #Measure the cosine similarity and take the second closest index because the 	first index 	is the user query
    vector_values = cosine_similarity(sentences_vectors[-1], sentences_vectors)
    answer = cat_sentences[vector_values.argsort()[0][-2]]
    #Final check to make sure there are result present. If all the result are 0, means the text 		input by us are not captured in the corpus
    input_check = vector_values.flatten()
    input_check.sort()
    if input_check[-2] == 0:
        return "Please Try again"
    else: 
        return answer
print("Hello, I am the Cat Chatbot. What is your meow questions?:")
while(True):
    query = input().lower()
    if query not in ['bye', 'good bye', 'take care']:
        print("Cat Chatbot: ", end="")
        print(chatbot_answer(query))
        cat_sentences.remove(query)
    else:
        print("See You Again")
        break
