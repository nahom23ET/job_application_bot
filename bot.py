from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
from jinja2 import Template
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load settings
def load_settings():
    with open("settings.txt", "r") as f:
        settings = {}
        for line in f:
            key, value = line.strip().split("=")
            settings[key] = value
    return settings

settings = load_settings()
JOB_KEYWORDS = settings["JOB_KEYWORDS"]
LOCATION = settings["LOCATION"]

LINKEDIN_EMAIL = "your_email@example.com"
LINKEDIN_PASSWORD = "your_password"
RESUME_PATH = "/path/to/your/resume.pdf"

def generate_cover_letter(job_title, company_name, hiring_manager_name=None):
    """Generates a customized cover letter."""
    with open("cover_letter_template.txt", "r") as template_file:
        template = Template(template_file.read())
    
    cover_letter = template.render(
        job_title=job_title,
        company_name=company_name,
        hiring_manager_name=hiring_manager_name,
        skills="cybersecurity and problem-solving",
        company_mission="advance cybersecurity solutions",
        specific_company_detail="your innovative approach to digital security"
    )
    return cover_letter

def match_jobs(resume_text, job_descriptions):
    """Ranks job descriptions based on similarity to the resume."""
    documents = [resume_text] + job_descriptions
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)
    similarity_scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()
    ranked_jobs = sorted(zip(job_descriptions, similarity_scores), key=lambda x: x[1], reverse=True)
    return ranked_jobs

def save_to_tracker(job_title, company_name, date_applied):
    """Saves application details to a CSV file."""
    data = {"Job Title": [job_title], "Company Name": [company_name], "Date Applied": [date_applied]}
    df = pd.DataFrame(data)
    with open("job_applications.csv", "a") as f:
        df.to_csv(f, header=f.tell() == 0, index=False)

def login_to_linkedin(driver):
    """Logs into LinkedIn."""
    driver.get("https://www.linkedin.com/login")
    time.sleep(2)
    driver.find_element(By.ID, "username").send_keys(LINKEDIN_EMAIL)
    driver.find_element(By.ID, "password").send_keys(LINKEDIN_PASSWORD)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(3)

def apply_to_jobs(driver):
    """Applies to jobs automatically."""
    job_listings = driver.find_elements(By.CLASS_NAME, "job-card-container")
    for job in job_listings[:5]:  # Apply to the first 5 jobs
        job.click()
        time.sleep(2)
        try:
            job_title = driver.find_element(By.CLASS_NAME, "topcard__title").text
            company_name = driver.find_element(By.CLASS_NAME, "topcard__org-name-link").text
            cover_letter = generate_cover_letter(job_title, company_name)
            print(f"Generated Cover Letter:\n{cover_letter}")
            save_to_tracker(job_title, company_name, time.strftime("%Y-%m-%d"))
            print(f"Application submitted for {job_title} at {company_name}!")
        except Exception as e:
            print("Error:", e)

def main():
    driver = webdriver.Chrome()
    driver.maximize_window()
    try:
        login_to_linkedin(driver)
        apply_to_jobs(driver)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
