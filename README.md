# Job Application Bot

## Overview
The Job Application Bot automates the process of applying for jobs online. It integrates features like customized cover letter generation, real-time application tracking via a dashboard, and a job matching algorithm to optimize your job search process.

### Features
1. **Enhanced Cover Letter Customization**:
   - Dynamically generates personalized cover letters using a Jinja2 template.
   - Inserts job-specific details like company name, job title, and more.

2. **Real-Time Dashboard**:
   - Built using Flask to monitor job applications.
   - Tracks applied jobs and provides a settings page for configuring job search preferences.

3. **Job Matching Algorithm**:
   - Uses TF-IDF and cosine similarity to rank job descriptions based on your resume.
   - Helps prioritize job applications based on relevance.

4. **Automated Job Applications**:
   - Applies to jobs on LinkedIn or other platforms using Selenium.
   - Automatically fills out forms and submits applications.

---

## Project Structure
```
job_application_bot/
├── templates/
│   ├── dashboard.html       # HTML for the dashboard
│   ├── settings.html        # HTML for settings page
├── static/
│   └── style.css            # Optional: Add custom styles for the dashboard
├── cover_letter_template.txt # Cover letter template
├── job_applications.csv      # Application tracker (generated after running the bot)
├── settings.txt              # Stores user preferences
├── dashboard.py              # Flask dashboard
├── bot.py                    # Main bot script
├── requirements.txt          # Python dependencies
├── README.md                 # Documentation
```

---

## Installation

### Prerequisites
- Python 3.7+
- Google Chrome
- ChromeDriver (compatible with your Chrome version)

### Steps
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd job_application_bot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Update the `bot.py` file with your LinkedIn credentials and resume path:
   ```python
   LINKEDIN_EMAIL = "your_email@example.com"
   LINKEDIN_PASSWORD = "your_password"
   RESUME_PATH = "/path/to/your/resume.pdf"
   ```

4. Ensure ChromeDriver is installed and added to your PATH.

---

## Usage

### Running the Flask Dashboard
Start the dashboard to monitor applications and configure preferences:
```bash
python dashboard.py
```
- Access the dashboard at: `http://127.0.0.1:5000/`

### Running the Bot
Run the bot to start applying for jobs:
```bash
python bot.py
```

---

## Features in Detail

### Enhanced Cover Letter Customization
- **Template**: Located in `cover_letter_template.txt`.
- **Customization**: Inserts job-specific details using Jinja2.
- **Example Usage**:
  ```python
  generate_cover_letter("Software Engineer", "TechCorp")
  ```

### Real-Time Dashboard
- Tracks job applications in `job_applications.csv`.
- Allows configuration of job keywords and location via `/settings` page.

### Job Matching Algorithm
- Uses TF-IDF to rank job descriptions based on your resume.
- **Example Usage**:
  ```python
  match_jobs(resume_text, job_descriptions)
  ```

### Automated Job Applications
- Navigates job platforms using Selenium.
- Automatically fills out forms and uploads your resume.

---

## Dependencies
- `selenium`: For automating browser actions.
- `flask`: For building the dashboard.
- `jinja2`: For generating dynamic cover letters.
- `pandas`: For tracking applications.
- `scikit-learn`: For job matching algorithm.

Install all dependencies via:
```bash
pip install -r requirements.txt
```

---

## Future Improvements
- Add multi-platform support (e.g., Indeed, Glassdoor).
- Enhance the job matching algorithm with machine learning.
- Implement notifications for application updates.

---

## Disclaimer
This project is for **educational purposes only**. Automating job applications may violate the terms of service of certain platforms. Use responsibly.

---

## Contributing
Contributions are welcome! Feel free to fork the repository and submit a pull request.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

