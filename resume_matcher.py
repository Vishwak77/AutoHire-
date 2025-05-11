import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nlp = spacy.load("en_core_web_sm")

def preprocess(text):
    doc = nlp(text.lower())
    return ' '.join([token.lemma_ for token in doc if not token.is_stop and token.is_alpha])

def get_similarity(resume_text, jd_text):
    resume_processed = preprocess(resume_text)
    jd_processed = preprocess(jd_text)
    vect = TfidfVectorizer()
    vectors = vect.fit_transform([resume_processed, jd_processed])
    return cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
