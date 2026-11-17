from django.contrib import admin
from .models import Resume, JobDescription, InterviewQuestion, InterviewAnswer



admin.site.register(Resume)
admin.site.register(JobDescription)
admin.site.register(InterviewQuestion)
admin.site.register(InterviewAnswer)