from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

def split_into_paragraphs(text):
    """Splits the resume text into paragraphs for detailed analysis."""
    # Using one or more newlines to split (adjust regex if necessary)
    paragraphs = re.split(r'\n+', text)
    return [p.strip() for p in paragraphs if p.strip()]

def extract_tech_skills(job_description):
    """Extracts important tech skills from the job description."""
    tech_skills = ["Python", "Java", "JavaScript", "SQL", "Machine Learning", "Data Science", 
                   "Deep Learning", "NLP", "React", "Node.js", "Django", "Flask", "PostgreSQL", "MongoDB"]
    
    job_desc_words = set(job_description.lower().split())
    extracted_skills = [skill for skill in tech_skills if skill.lower() in job_desc_words]
    
    return extracted_skills

def calculate_paragraphwise_ats(resume_text, job_description):
    """Evaluates ATS score for each paragraph and gives recommendations."""
    
    paragraphs = split_into_paragraphs(resume_text)
    
    # If no paragraphs are found, return score 0 with an appropriate message
    if not paragraphs:
        return 0, [("No Content", 0)], ["No valid paragraphs found in the resume."]
    
    extracted_skills = extract_tech_skills(job_description)
    
    vectorizer = TfidfVectorizer()
    try:
        vectors = vectorizer.fit_transform([job_description] + paragraphs)  # First vector = Job description
    except Exception as e:
        # In case of any vectorization error, return 0 with error message
        return 0, [("Error", 0)], [f"Vectorization error: {e}"]
    
    ats_scores = []
    recommendations = []
    
    for i, paragraph in enumerate(paragraphs):
        # Check if the paragraph produced a valid vector
        if i+1 >= vectors.shape[0]:
            continue
        similarity = cosine_similarity(vectors[0:1], vectors[i+1:i+2])[0][0] * 100  # Compare each paragraph

        # Use a keyword-based check to boost the score
        paragraph_words = set(paragraph.lower().split())
        matching_skills = [skill for skill in extracted_skills if skill.lower() in paragraph_words]
        keyword_score = (len(matching_skills) / len(extracted_skills)) * 100 if extracted_skills else 0
        
        # Adjust the weighting as needed (e.g., 70% cosine similarity, 30% keyword match)
        total_score = (similarity * 0.7) + (keyword_score * 0.3)
        
        ats_scores.append((f"Paragraph {i+1}", total_score))
        
        # Recommendations for missing skills
        missing_skills = [skill for skill in extracted_skills if skill.lower() not in paragraph_words]
        if missing_skills:
            recommendations.append(f"Paragraph {i+1}: Consider adding skills - {', '.join(missing_skills)}.")

    overall_ats = sum(score for _, score in ats_scores) / len(ats_scores)
    return overall_ats, ats_scores, recommendations
