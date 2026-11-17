from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload-resume/', views.upload_resume, name='upload_resume'),
    path('resume-analysis/<int:resume_id>/', views.resume_analysis, name='resume_analysis'),
    path(
        'add-job-description/<int:resume_id>/',
        views.add_job_description,
        name='add_job_description'
    ),
    path(
        'interview-preparation/<int:resume_id>/',
        views.interview_preparation,
        name='interview_preparation'
    ),
    path(
        'interview-questions/<int:interview_id>/',
        views.interview_questions,
        name='interview_questions'
    ),
    path(
        'submit-interview-answer/<int:interview_id>/',
        views.submit_interview_answer,
        name='submit_interview_answer'
    ),
    path(
        'dashboard/',
        views.dashboard,
        name='dashboard'
    ),

    path(
        'resume-history/', 
        views.resume_history, 
        name='resume_history'
    ),

    path(
        'delete-resume/<int:resume_id>/', 
        views.delete_resume, 
        name='delete_resume'
    ),

    path(
        'register/', 
        views.register, 
        name='register'
    ),

    path(
        'login/', 
        auth_views.LoginView.as_view
        (
            template_name='career/login.html'
    ), name='login'),

    path(
        'logout/', 
        auth_views.LogoutView.as_view(), name='logout'),
    
]