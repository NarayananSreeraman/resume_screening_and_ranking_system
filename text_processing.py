"""import spacy
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Load spaCy model
nlp = spacy.load('en_core_web_sm')

# Download NLTK stopwords
nltk.download('punkt')
nltk.download('stopwords')

def preprocess_text(text):
    text = text.lower()
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token.isalnum() and token not in stop_words]
    return " ".join(tokens)

def extract_features(text):
    doc = nlp(text)
    entities = [ent.text for ent in doc.ents]
    skills_list = ['python', 'java', 'javascript', 'sql', 'machine learning', 'data analysis']
    skills = [token.text for token in doc if token.text.lower() in skills_list]
    return {"entities": entities, "skills": skills}"""

import spacy
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import json

# Load spaCy model
nlp = spacy.load('en_core_web_sm')

# Download NLTK stopwords
nltk.download('punkt')
nltk.download('stopwords')

# Load a diverse set of tech skills dynamically
TECH_SKILLS = set([
    "python", "java", "javascript", "typescript", "c++", "c#", "golang", "ruby", "php",
    "swift", "kotlin", "r", "sql", "mysql", "postgresql", "mongodb", "firebase",
    "machine learning", "deep learning", "nlp", "computer vision", "data science", 
    "big data", "hadoop", "spark", "tensorflow", "pytorch", "keras", "flask", "django",
    "react", "angular", "vue", "node.js", "express.js", "docker", "kubernetes", "aws",
    "azure", "gcp", "terraform", "linux", "bash scripting", "git", "devops"
])

def preprocess_text(text):
    text = text.lower()
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token.isalnum() and token not in stop_words]
    return " ".join(tokens)

def extract_features(text):
    doc = nlp(text)
    entities = [ent.text for ent in doc.ents]
    skills = [token.text for token in doc if token.text.lower() in TECH_SKILLS]
    return {"entities": entities, "skills": skills}

