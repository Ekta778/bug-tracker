# 🔞 Bug Tracker & Test Case Management System

A simple Flask-based web application to manage software bugs and test cases. Ideal for Software Quality Assurance (SQA) projects, educational demos, or lightweight internal use.


## 🚀 Features

- 🐛 Add, view, and manage bug reports with severity and assignment
- ✅ Create and track test cases with steps and expected outcomes
- 🧪 Clean, responsive interface using Flask and HTML templates
- 📀 SQLite database integration for persistent storage
- ☁️ Deployable to Heroku or Render with minimal setup

---

🛠 Tech Stack

- Python 3.x
- Flask (Micro web framework)
- SQLite (Lightweight relational database)
- HTML5 + Jinja2 (Templating engine)

---

🗂️ Project Structure

```
bug-tracker-sqa/
├── app.py                     # Main Flask application
├── sqa.db                     # SQLite database file (auto-generated)
├── requirements.txt           # Project dependencies
├── Procfile                   # For Heroku deployment
├── README.md                  # Project documentation
├── templates/                 # HTML templates
│   ├── index.html             # Home page
│   ├── bugs.html              # Bug list view
│   ├── bug_form.html          # Bug submission form
│   ├── test_cases.html        # Test cases view
│   └── test_case_form.html    # Test case submission form
```

---

🧰 Run Locally

```bash
git clone https://github.com/your-username/bug-tracker-sqa.git
cd bug-tracker-sqa

# Create virtual environment (optional)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

Open your browser and go to: [http://localhost:5000](http://localhost:5000)

---

🌐 Deploy to Heroku

1. Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
2. Deploy using Git:

```bash
heroku login
git init
heroku create
git add .
git commit -m "Initial commit"
git push heroku master
