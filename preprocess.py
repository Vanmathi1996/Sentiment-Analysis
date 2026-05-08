import re
import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import re # regular expression



stop_words=stopwords.words('english')
lemmatizer=WordNetLemmatizer()


def preprocess(text):
  # convert reviews into lowercase
  text=text.lower()

  # remove punctuations and numbers
  text=re.sub(r'[^a-z \s]',"",text) # replace everything except a-z and single space with empty string

  # tokkenize : split reviews into indvidual word
  tokens=word_tokenize(text)

  # remove stop words
  tokens=[word for word in tokens if word not in stop_words]

  # lemmatize: convert tokens to its verb form
  tokens=[lemmatizer.lemmatize(word,pos='v') for word in tokens]


  return " ".join(tokens)# put together the tokens back to sentiment format


sample="Amazing product . Delivered promptly . 10/10"
print(preprocess(sample))

