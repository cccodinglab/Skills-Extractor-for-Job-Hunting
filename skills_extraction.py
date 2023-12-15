import os
from PyPDF2 import PdfReader
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PdfReader(file)
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text

def extract_skills(text):
    # Tokenize the text
    words = word_tokenize(text)

    # Remove punctuation and convert to lowercase
    words = [word.lower() for word in words if word.isalpha()]

    # Remove stopwords and additional common words
    
    '''stop_words = set(stopwords.words("english"))
    common_words = set(["page", "years", "months", "experience", "skills", "work", "working", "knowledge", "ability", "strong", "new", "area", "york", "university","united","states"])
    words = [word for word in words if word not in stop_words and word not in common_words]'''
    
    common_skills = set(["numpy", "panda", "scikitlearn", "nltk", "communication","collaboration",
                        "bayesian", "clustering", "classification", "regression", "forecasting", "network", "testing", "deep learning", "random forest", "decision tree", "exploratory", "support vector", 
                        "machine learning", "visualization", "analysis", "dashboard",
                        "data collection", "data cleaning", "data wrangling", "data cleansing",
                        "python", "r", "sql", "tableau", "excel", "spark", "hadoop", "julia", "jupyter", "excel", 
                        "predictive", "statistics", "outlier"])
    words = [word for word in words if word in common_skills]
    return words

def generate_report(sorted_words, report_path):
    with open(report_path, 'w') as report_file:
        report_file.write("Top 10 most common data science-related words:\n")
        for word, count in sorted_words[:10]:
            report_file.write(f"{word}: {count} occurrences\n")

'''
    # Set the path to the directory containing the PDF files
    pdf_directory = '~/Downloads'

    # Get a list of PDF files in the directory
    pdf_files = [file for file in os.listdir(pdf_directory) if file.startswith("Profile")]

    # Initialize an empty list to store skills from all profiles
    all_skills = []

    # Process each PDF file
    for pdf_file in pdf_files:
        pdf_path = os.path.join(pdf_directory, pdf_file)

    # Process each PDF file
    for pdf_file in pdf_files:
        pdf_path = os.path.join(pdf_directory, pdf_file)

        # Extract text from the PDF
        profile_text = extract_text_from_pdf(pdf_path)

        # Extract skills from the text
        profile_skills = extract_skills(profile_text)

        # Add skills to the list of all skills
        all_skills.extend(profile_skills)'''

def main():
    all_skills = []
    profile_text = extract_text_from_pdf('/Users/cecichen/Desktop/jd.pdf')
    profile_skills = extract_skills(profile_text)
    all_skills.extend(profile_skills)

    # Count the occurrences of each skill
    skill_counts = {skill: all_skills.count(skill) for skill in set(all_skills)}

    # Sort skills by count in descending order
    sorted_skills = sorted(skill_counts.items(), key=lambda x: x[1], reverse=True)

    # Display the most common skills
    print("Top 10 most common skills:")
    for skill, count in sorted_skills[:10]:
        print(f"{skill}: {count} occurrences")
    
    report_path = "output/data_science_report.txt"
    generate_report(sorted_skills, report_path)
    print(f"Report generated at: {report_path}")

if __name__ == "__main__":
    main()