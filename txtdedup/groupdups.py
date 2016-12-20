from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem.snowball import SnowballStemmer

from fuzzywuzzy import fuzz

# Get the stop words
stop_words = set(stopwords.words('english'))
stop_words.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}'])

# STEMMING
stemmer = SnowballStemmer("english")

# LEMMATIZATION
lemmatizer = WordNetLemmatizer()

def get_processed_text(text, pp_technique):
    if pp_technique == 'lemmatize':
        return [lemmatizer.lemmatize(w).lower() for w in word_tokenize(text) if w not in stop_words]
    else:
        return [stemmer.stem(w) for w in word_tokenize(text) if w not in stop_words]


def get_duplicates(given_list, pp_technique='stem', similarity_ratio=70):
    processed_list = list(map(lambda i: get_processed_text(i, pp_technique), given_list))
    processed_indices = []
    result_list = []
    for i, text1 in enumerate(processed_list):
        if len(text1) > 2 and i not in processed_indices:
            processed_indices.append(i)
            title_dups = [given_list[i]]
            for j, text2 in enumerate(processed_list):
                not_preprocessed = j not in processed_indices
                is_similar = fuzz.token_set_ratio(text1, text2) >= similarity_ratio
                if len(text2) > 2 and not_preprocessed and is_similar:
                    processed_indices.append(j)
                    title_dups.append(given_list[j])
            result_list.append(title_dups)

    return result_list

