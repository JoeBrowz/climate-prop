from custom_functions import *
import pickle

import streamlit as st
import twint

st.title('Classify Climate Change Tweets')

@st.cache(allow_output_mutation=True)
def load_pkls():
    pickle_in = open('data/pickle_jar/lr1_grid.pkl', 'rb')
    model = pickle.load(pickle_in)
    pickle_in.close()
    
    pickle_in = open('data/pickle_jar/vec.pkl', 'rb')
    vectorizer = pickle.load(pickle_in)
    pickle_in.close()

    return model, vectorizer

lemmatizer = WordNetLemmatizer()

st.subheader("This crude web app uses a logistic regression model to classify a text as a beleiver or a denier of climate change")
tweet = st.text_input('Enter the tweet text in the box below')
model, vectorizer = load_pkls()

believer_out = ["Lean, green, science believing machine",
                "I see you read",
                "Your grandkids would be so proud had they been able to live on this planet"]

denier_out = ["Bless your heart, you're confused",
                  'I see you do your "research" on YouTube',
                  "Quick! Look! Bill Gates is right behind you with a microchip! \n\n...I figured you might believe it since this iswritten on the internet"]

def classify(tweet):
    if len(tweet) < 3:
        return None
    cleaned_tweet = clean_and_lem(tweet, lemmatizer)
    tweet_pd = pd.Series(cleaned_tweet)
    tweet_vec = vectorizer.transform(tweet_pd)
    prediction = model.predict(tweet_vec)
    if prediction[0] == 1:
        print_ = np.random.choice(believer_out)
    elif prediction[0] == 0:
        print_ = np.random.choice(denier_out)
    else:
        print_ = None
    return print_

output = classify(tweet)

if len(tweet) > 2:
    st.write(output)
