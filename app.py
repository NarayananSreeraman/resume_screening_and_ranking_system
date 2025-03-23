import streamlit as st 
import pandas as pd
from resume_parser import extract_text_from_pdf, extract_text_from_docx
from text_processing import preprocess_text, extract_features
from ats_score import calculate_paragraphwise_ats
from login import validate_login

# Set page configuration and add custom CSS for background styling
st.set_page_config(page_title="AI-powered Resume Screening System", layout="wide")

def add_bg_from_url():
    """Inject custom CSS to set a background image for the app."""
    st.markdown(
         """
         <style>
         .stApp {
             background: url("https://images.unsplash.com/photo-1515738611928-2a151b20a346?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
             background-size: cover;
         }
         </style>
         """,
         unsafe_allow_html=True
    )

def login_page():
    st.title("AI-powered Resume Screening System - Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login (Double Click to Enter the Dashboard!)"):
        if validate_login(email, password):
            st.success("Login successful!")
            st.session_state.logged_in = True  # Set login status
        else:
            st.error("Invalid email or password. Please try again.")

def main_app():
    st.header("Upload Resumes")
    resume_files = st.file_uploader("Choose resume files", type=['pdf', 'docx'], accept_multiple_files=True)

    st.header("Job Description")
    job_description = st.text_area("Enter the job description")

    if resume_files and job_description:
        # Preprocess the job description once
        processed_job_desc = preprocess_text(job_description)
        
        # Initialize a list to store results for each resume file
        results = []

        for resume_file in resume_files:
            st.subheader(f"Processing file: {resume_file.name}")
            
            # Extract text from the resume file
            if resume_file.type == "application/pdf":
                resume_text = extract_text_from_pdf(resume_file)
            else:
                resume_text = extract_text_from_docx(resume_file)
            
            # Preprocess the resume text
            processed_resume = preprocess_text(resume_text)
            
            # Prepare a dictionary to hold the file's result
            file_result = {"File": resume_file.name}
            
            if not processed_resume.strip():
                # If no valid text found, store a 0 ATS score
                file_result["ATS Score"] = 0
                file_result["Recommendations"] = "No valid text found in this resume."
            else:
                # Calculate ATS score for this resume
                overall_ats, ats_scores, recommendations = calculate_paragraphwise_ats(
                    processed_resume,
                    processed_job_desc
                )
                file_result["ATS Score"] = round(overall_ats, 2)
                file_result["Recommendations"] = "; ".join(recommendations) if recommendations else "None"
                
                # Optionally, display detailed results for each file
                st.write(f"Overall ATS Compatibility Score: {overall_ats:.2f}%")
                st.progress(int(overall_ats))
                
                st.write("### Paragraph-wise ATS Scores")
                for paragraph, score in ats_scores:
                    st.write(f"{paragraph}: {score:.2f}%")
                
                st.write("### Recommendations")
                for recommendation in recommendations:
                    st.write(recommendation)
                
                features = extract_features(resume_text)
                st.write("### Extracted Skills")
                st.write(", ".join(set(features['skills'])))
            
            results.append(file_result)
            st.write("---")

        # Convert list of results into a DataFrame and sort by ATS Score (descending)
        df_results = pd.DataFrame(results)
        df_results = df_results.sort_values(by="ATS Score", ascending=False)
        
        # Remove the 'Recommendations' column from the displayed table
        if "Recommendations" in df_results.columns:
            df_results = df_results.drop(columns=["Recommendations"])
        
        # Reset the index so it starts at 1 instead of 0
        df_results = df_results.reset_index(drop=True)
        df_results.index = df_results.index + 1
        df_results.index.name = "#"

        st.header("Overall ATS Compatibility Scores for Uploaded Resumes")
        st.dataframe(df_results)

    # Logout button
    if st.button("Logout"):
        st.session_state.logged_in = False  # Set login status to False

# Main logic to control the flow of the application
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Add background styling at the top of the app
add_bg_from_url()

if st.session_state.logged_in:
    main_app()  # Show main application features if logged in
else:
    login_page()  # Show login page if not logged in