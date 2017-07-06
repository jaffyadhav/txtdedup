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


def _get_processed_text(text, pp_technique):
    if pp_technique == 'lemmatize':
        return [lemmatizer.lemmatize(w).lower() for w in word_tokenize(text) if w not in stop_words]
    else:
        return [stemmer.stem(w) for w in word_tokenize(text) if w not in stop_words]


def groupdups(strings_to_group=[], pp_technique='stem', similarity_ratio=70):
    processed_list = list(map(lambda i: _get_processed_text(i, pp_technique), strings_to_group))
    processed_indices = []
    result_list = []
    for i, string_one in enumerate(processed_list):
        if len(string_one) > 2 and i not in processed_indices:
            processed_indices.append(i)
            similar_strings = [strings_to_group[i]]
            for j, string_two in enumerate(processed_list):
                not_preprocessed = j not in processed_indices
                is_similar = fuzz.token_set_ratio(string_one, string_two) >= similarity_ratio
                if len(string_two) > 2 and not_preprocessed and is_similar:
                    processed_indices.append(j)
                    similar_strings.append(strings_to_group[j])
            result_list.append(similar_strings)

    return result_list

