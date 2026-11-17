
from django.db import models
from django.contrib.auth.models import User


class Resume(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='resumes',
        null=True,
        blank=True
    )
    candidate_name = models.CharField(max_length=100)
    email = models.EmailField()
    resume_file = models.FileField(upload_to='resumes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    extracted_text = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.candidate_name


class JobDescription(models.Model):
    resume = models.ForeignKey(
        Resume,
        on_delete=models.CASCADE,
        related_name='job_descriptions'
    )
    job_title = models.CharField(max_length=150)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.job_title

class InterviewQuestion(models.Model):
    resume = models.ForeignKey(
        Resume,
        on_delete=models.CASCADE,
        related_name='interview_questions'
    )

    job_description = models.ForeignKey(
        JobDescription,
        on_delete=models.CASCADE,
        related_name='interview_questions'
    )

    questions = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Interview Questions - {self.resume.candidate_name}"


class InterviewAnswer(models.Model):
    interview = models.ForeignKey(
        InterviewQuestion,
        on_delete=models.CASCADE,
        related_name='answers'
    )

    question = models.TextField()
    candidate_answer = models.TextField()
    ai_feedback = models.TextField(blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Interview Answer - {self.interview.resume.candidate_name}"
