# resume_screening_system
A resume screening and ranking system.
Certainly! Here's an example of a **README.md** file for an AI-based Resume Screening and Ranking System:

---

# AI-Based Resume Screening and Ranking System

## Overview
The **AI-Based Resume Screening and Ranking System** is an intelligent tool designed to streamline the recruitment process. Using machine learning and natural language processing (NLP), the system can parse resumes, analyze candidate qualifications, and rank applicants based on predefined criteria. This system saves time and resources by automating the initial stages of candidate evaluation.

## Features
- **Resume Parsing**: Extracts text and relevant information from PDF and DOCX files.
- **Skills Matching**: Identifies and ranks candidates based on required skills and experience.
- **Keyword Analysis**: Performs keyword-based searches for specific qualifications or achievements.
- **Ranking**: Sorts and ranks resumes to highlight the most relevant candidates.
- **User-Friendly Interface**: Provides a seamless experience for recruiters with clear visual outputs.

## Technology Stack
- **Programming Language**: Python
- **Libraries and Frameworks**:
  - Streamlit (for the user interface)
  - PyPDF2 (for PDF parsing)
  - SpaCy or NLTK (for natural language processing)
  - Pandas (for data manipulation)
- **Other Tools**:
  - Virtual Environment for dependency management

## Installation
1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd resume_screening_and_ranking_system
   ```
2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

## How It Works
1. Upload resumes in PDF format.
2. Define ranking criteria, such as skills, or keywords.
3. The system parses the resumes and evaluates candidates based on the specified criteria.
4. View the ranked list of candidates in the output interface.

## License
This project is licensed under the [MIT License](LICENSE).

## Login Credentials (for testing, as no database has been implemented for this project)
1. "abc@gmail.com": "Test123#",
2. "user2@gmail.com": "user2@123"
