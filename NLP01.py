# Assignment – High Frequency Words

# Please answer the following questions in an IPython Notebook, posted to GitHub.

# 1.Choose a corpus of interest.
# 2.How many total unique words are in the corpus?  
#   (Please feel free to define unique words in any interesting, defensible way).
# 3.Taking the most common words, how many unique words represent half of the total words in the 
#   corpus?
# 4.Identify the 200 highest frequency words in this corpus.
# 5.Create a graph that shows the relative frequency of these 200 words.
# 6.Does the observed relative frequency of these words follow Zipf’s law?  Explain.
# 7.In what ways do you think the frequency of the words in this corpus differ 
#   from “all words in all corpora.”

from bs4 import BeautifulSoup
import urllib.request 
import nltk 
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
from nltk import FreqDist

lemmatizer = WordNetLemmatizer()
porter = PorterStemmer() 

response = urllib.request.urlopen('https://www.realclearpolitics.com/')
# response = urllib.request.urlopen('http://php.net/')
html = response.read()
soup = BeautifulSoup(html,"html5lib")

for script in soup(["script", "style"]): 
    # remove all javascript and stylesheet code
    script.extract()

text = soup.get_text(strip=True).lower()


# wt = word_tokenize(text)

# tokenizer = RegexpTokenizer(r'\w+')
# print(tokenizer.tokenize(wt))

# mytext = "Hello Mr. Adam, how are you? I hope everything is going well. Today is a good day, see you dude."
wt = word_tokenize(text)
sw = stopwords.words('english')
csw = ['function', 'var', 'is', 'you', 'said', 'next', 'read', 'still', 'will', 'say']

fs = [word for word in wt if word.isalpha()]
fs = [word for word in fs if not word in sw]
fs = [word for word in fs if len(word) > 1]
fs = [word for word in fs if not word in csw]
fs = [lemmatizer.lemmatize(word) for word in fs]


freq = nltk.FreqDist(fs)
print(len(freq))
print(freq.most_common(200))
freq.plot(200,cumulative=False)

# print(stemmer.stem('working'))

fs = [porter.stem(word) for word in fs]

# print(fs)

wordcloud = WordCloud().generate(' '.join(fs))
# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()


# tokens = [t for t in text.split()]
# clean_tokens = tokens[:]
# sr = stopwords.words('english')
 
# for token in tokens:
#     if token in stopwords.words('english'):
#         clean_tokens.remove(token)
 
# freq = nltk.FreqDist(clean_tokens)
 
# for key,val in freq.items():
#     print (str(key) + ':' + str(val))

# freq.plot(20,cumulative=False)




# from nltk.tokenize import word_tokenize
# mytext = "Hello Mr. Adam, how are you? I hope everything is going well. Today is a good day, see you dude."

# print(word_tokenize(mytext))

# from nltk.corpus import wordnet

# syn = wordnet.synsets("pain")
# print(syn[0].definition())
# print(syn[0].examples())

# syn = wordnet.synsets("NLP")
# print(syn[0].definition()) 
# syn = wordnet.synsets("Python")
# print(syn[0].definition())

# from nltk.corpus import wordnet
 
# synonyms = []
 
# for syn in wordnet.synsets('Computer'):
#     for lemma in syn.lemmas(): 
#         synonyms.append(lemma.name())
 
# print(synonyms)

# from nltk.corpus import wordnet

# antonyms = []
 
# for syn in wordnet.synsets("small"):
#     for l in syn.lemmas(): 
#         if l.antonyms(): 
#             antonyms.append(l.antonyms()[0].name())
 
# print(antonyms)

# from nltk.stem import PorterStemmer
 
# stemmer = PorterStemmer() 
# print(stemmer.stem('working'))
# print(stemmer.stem('increases'))

# from nltk.stem import WordNetLemmatizer
 
# lemmatizer = WordNetLemmatizer()
# print(lemmatizer.lemmatize('increases'))
# print(lemmatizer.lemmatize('playing', pos="v"))
# print(lemmatizer.lemmatize('playing', pos="n"))
# print(lemmatizer.lemmatize('playing', pos="a"))
# print(lemmatizer.lemmatize('playing', pos="r"))



