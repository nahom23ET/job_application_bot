from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    """Dashboard homepage showing application tracker."""
    try:
        df = pd.read_csv("job_applications.csv")
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Job Title", "Company Name", "Date Applied"])
    
    return render_template("dashboard.html", applications=df.to_dict(orient="records"))

@app.route('/settings', methods=["GET", "POST"])
def settings():
    """Page to configure bot settings."""
    if request.method == "POST":
        # Save settings (e.g., job keywords, location)
        with open("settings.txt", "w") as f:
            f.write(f"JOB_KEYWORDS={request.form['keywords']}\n")
            f.write(f"LOCATION={request.form['location']}\n")
        return "Settings updated successfully!"
    return render_template("settings.html")

if __name__ == "__main__":
    app.run(debug=True)
