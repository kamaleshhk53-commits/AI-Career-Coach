# 🚀 AI Career Coach – Resume Analyzer & Interview Preparation Assistant

<p align="center">
  <b>An AI-powered career assistant to analyze resumes, match job descriptions, and prepare candidates for interviews.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django"/>
  <img src="https://img.shields.io/badge/Ollama-000000?style=for-the-badge&logo=ollama&logoColor=white" alt="Ollama"/>
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript"/>
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite"/>
</p>

---

## 📌 About the Project

**AI Career Coach** is a web-based application developed using Python and Django. It helps job seekers improve their resumes, identify skill gaps, and prepare for technical interviews using Artificial Intelligence.

The application integrates a locally running Large Language Model (LLM) through **Ollama (Llama 3.2)** to provide personalized career assistance.

## ✨ Key Features

- 🔐 **User Authentication** – Registration and secure login.
- 📄 **Resume Upload** – Upload resumes in PDF format.
- 🤖 **AI Resume Analysis** – Identify technical skills, strengths, weaknesses, and improvement areas.
- 🎯 **Job Description Matching** – Compare resume skills with job requirements.
- 💡 **Interview Preparation** – Generate job-specific interview questions.
- 📝 **Answer Evaluation** – Receive AI feedback and scores for interview answers.
- 📊 **Dashboard** – View resume statistics and recent uploads.
- 📁 **Resume History** – View and manage uploaded resumes.

## 🛠️ Technologies Used

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Backend Framework | Django |
| Frontend | HTML, CSS, JavaScript |
| Database | SQLite |
| AI Model | Llama 3.2 (3B) |
| AI Integration | Ollama |
| PDF Processing | PyPDF2 |
| Version Control | Git, GitHub |

## 🏗️ Project Structure

```text
AI-Career-Coach/
│
├── career/
│   ├── migrations/
│   ├── static/
│   │   └── career/css/
│   ├── templates/
│   │   └── career/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── utils.py
│   └── views.py
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/kamaleshhk53-commits/AI-Career-Coach.git
cd AI-Career-Coach
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

### 3️⃣ Activate Virtual Environment (Windows)

```bash
venv\Scripts\activate
```

### 4️⃣ Install Required Packages

```bash
pip install django PyPDF2 ollama
```

### 5️⃣ Install Ollama and Download the AI Model

Download Ollama:

https://ollama.com/

Pull the Llama 3.2 model:

```bash
ollama pull llama3.2:3b
```

Make sure the Ollama service is running before using AI features.

### 6️⃣ Apply Database Migrations

```bash
python manage.py migrate
```

### 7️⃣ Run the Django Development Server

```bash
python manage.py runserver
```

Open your browser:

**http://127.0.0.1:8000/**

## 🔄 Application Workflow

1. 👤 User registers and logs into the application.
2. 📄 Uploads a resume in PDF format.
3. 🔍 Django extracts text from the uploaded PDF.
4. 🤖 Ollama analyzes the resume and generates feedback.
5. 🎯 User enters a job description for skill matching.
6. 💬 AI generates interview questions based on the job role.
7. 📝 User submits answers for AI evaluation.
8. 📊 Feedback and scores are displayed in the application.

## 🧠 AI Integration

This project uses **Ollama with Llama 3.2 (3B)** to perform AI-based tasks locally.

AI functionalities include:

- Resume analysis.
- Skill gap identification.
- Job description matching.
- Interview question generation.
- Interview answer evaluation.

## 🎯 Project Objectives

- Help job seekers improve resume quality.
- Identify missing technical skills.
- Provide personalized interview preparation.
- Make AI-powered career assistance accessible through a web application.

## 🚀 Future Scope

- Support additional resume formats.
- Improve AI feedback quality.
- Expand interview preparation capabilities.

## 👨‍💻 Author

**Kamalesh H K**

Electronics and Communication Engineering Graduate

📌 GitHub: [kamaleshhk53-commits](https://github.com/kamaleshhk53-commits)

📂 Project Repository: [AI Career Coach](https://github.com/kamaleshhk53-commits/AI-Career-Coach)

---

<p align="center">
  <b>⭐ If you find this project interesting, consider giving it a star!</b>
</p>

<p align="center">
  Made with ❤️ using Python, Django and Ollama
</p>
