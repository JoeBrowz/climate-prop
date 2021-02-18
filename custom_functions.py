import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
import re
import time
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')

from wordcloud import WordCloud, STOPWORDS
import matplotlib.colors as mcolors

import nltk
# nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import string
from nltk import word_tokenize, FreqDist
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def re_clean(tweet):
    '''
    takes the text of a tweet and returns a cleaned string ready for tokenization and lemmatization 
    '''
    # remove emojis
    emoji = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags = re.UNICODE)
    tweet = emoji.sub('', tweet)
    # regex cleaning
    tweet = tweet.lower()
    tweet = re.sub(r'[@][\w]+','', tweet) # <-- remove usernames
    tweet = re.sub(r'[#]','', tweet) # <-- remove hashtags 
    tweet = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', tweet) # <-- remove urls
    tweet = re.sub(r'(?:^| )\w(?:$| )', ' ', tweet) # <-- remove one letter words
    tweet = re.sub(r'\s{2,15}', ' ', tweet) # <-- remove extra blank spaces
    tweet = re.sub(r'\n', ' ', tweet)  # <-- remove line breaks
    tweet = re.sub(r'\s{2,15}', ' ', tweet) # <-- combine multiple space again 
    return tweet.strip() # <-- remove lingering spaces at the start and end of tweets


def lemm(tweet, lemmatizer):
    '''
    lemmatizes a sentence and returns string ready to be vectorized
    '''
    # tokenize, lemmatize
    tok = nltk.regexp_tokenize(tweet, r"([a-zA-Z]+(?:'[a-z]+)?)")
    lemma = [lemmatizer.lemmatize(token) for token in tok]
    # return combined string 
    return ' '.join(lemma)


def clean_and_lem(tweet, lemmatizer):
    '''
    clean then lammatize tweet
    '''
    return lemm(re_clean(tweet), lemmatizer)

def tok(tweet):
    return nltk.regexp_tokenize(tweet, r"([a-zA-Z]+(?:'[a-z]+)?)")

# create function to compare original text to cleaned text 
def check_cleaned(df, n = None):
    '''
    sanity check function. Look at cleaned text for edge case detection.
    '''
    if not n:
        n = np.random.randint(0, len(df) - 1)
    print(f"ORIGINAL: \n{df.iloc[n]['full_text']} \n")
    print(f"CLEANED: \n{clean_and_lem(df.iloc[n]['full_text'])}")
    

