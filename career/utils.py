from PyPDF2 import PdfReader
import ollama


def extract_resume_text(pdf_file):
    reader = PdfReader(pdf_file)
    resume_text = ""

    for page in reader.pages:
        text = page.extract_text()

        if text:
            resume_text += text + "\n"

    return resume_text


def analyze_resume_with_ai(resume_text):
    response = ollama.chat(
        model='llama3.2:3b',
        messages=[
            {
                'role': 'system',
                'content': 'You are an expert resume reviewer and career coach.'
            },
            {
                'role': 'user',
                'content': f"""
                Analyze this resume.

                Provide:
                1. Technical skills
                2. Strengths
                3. Weaknesses
                4. Missing skills
                5. Suggestions for improvement

                Resume:
                {resume_text}
                """
            }
        ]
    )

    return response['message']['content']

def match_resume_with_job(resume_text, job_description):

    response = ollama.chat(
        model='llama3.2:3b',
        messages=[
            {
                'role': 'system',
                'content': 'You are an expert technical recruiter. Compare resumes with job descriptions and provide honest, evidence-based feedback.'
            },
            {
                'role': 'user',
                'content': f"""
                Compare the following resume with the job description.

                Provide:

                1. Resume Match Score (0-100)
                2. Matching Skills
                3. Missing Skills
                4. Relevant Experience
                5. Areas to Improve
                6. Final Recommendation

                RESUME:
                {resume_text}

                JOB DESCRIPTION:
                {job_description}
                """
            }
        ]
    )

    return response['message']['content']


def generate_interview_questions(resume_text, job_description):

    response = ollama.chat(
        model='llama3.2:3b',
        messages=[
            {
                'role': 'system',
                'content': 'You are an experienced technical interviewer.'
            },
            {
                'role': 'user',
                'content': f"""
                Generate 15 interview questions based on this resume
                and job description.

                Include:
                1. Python technical questions
                2. Django questions
                3. SQL and database questions
                4. Project-related questions
                5. HR and behavioural questions

                Resume:
                {resume_text}

                Job Description:
                {job_description}

                Number the questions from 1 to 15.
                """
            }
        ]
    )

    return response['message']['content']

import re

def evaluate_interview_answer(question, candidate_answer):

    response = ollama.chat(
        model='llama3.2:3b',
        messages=[
            {
                'role': 'system',
                'content': 'You are an experienced technical interviewer.'
            },
            {
                'role': 'user',
                'content': f"""
                Evaluate the candidate's answer.

                Question: {question}

                Candidate Answer: {candidate_answer}

                Return:
                SCORE: [number between 0 and 10]

                STRENGTHS:
                Explain strengths.

                WEAKNESSES:
                Explain weaknesses.

                SUGGESTIONS:
                Give improvement suggestions.

                IDEAL ANSWER:
                Provide an ideal answer.
                """
            }
        ]
    )

    feedback = response['message']['content']

    score_match = re.search(
        r'SCORE:\s*(\d+(?:\.\d+)?)',
        feedback,
        re.IGNORECASE
    )

    score = None

    if score_match:
        score = round(float(score_match.group(1)))

        score = max(0, min(10, score))

    return feedback, score