import numpy as np
import pandas as pd
from Levenshtein import distance
from nltk.tokenize import word_tokenize
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

corrected_word = pd.read_excel('data/tmtDB.xlsx')
corrected_word = corrected_word.dropna(subset=['word'])
corrected_word_lst = corrected_word['word'].to_list()

tmtProductName_df = pd.read_excel('data/tmtProductName.xlsx')
tmtProductName_lst = tmtProductName_df['tmtName'].to_list()

def tokenize(text):
    return word_tokenize(text)

def token_correction(token, corrected_word_lst):
    return min(corrected_word_lst, key=lambda word: distance(token, word))

def misspelled_correction(tokens):
    corrected_tokens = ''

    for token in tokens:
        if str(token).isdigit():
            corrected_tokens += f'{token} '
            continue
        corrected_token = token_correction(token, corrected_word_lst)
        corrected_tokens += f'{corrected_token} '
    
    return corrected_tokens

vectorizer = TfidfVectorizer(lowercase=False)
vectorizer = vectorizer.fit(tmtProductName_lst)
corrected_word_vertorize = vectorizer.transform(tmtProductName_lst)

def find_similar_word(text):
    text_vectorize = vectorizer.transform([text])
    cosine_similarities = cosine_similarity(text_vectorize, corrected_word_vertorize)
    top_5_idx = np.argsort(cosine_similarities[0])[-5:][::-1]  # Sort in descending order
    # top_5_scores = cosine_similarities[0][top_5_idx]
    result = [tmtProductName_df.iloc[idx]['tmtName'] for idx in top_5_idx]

    return result


