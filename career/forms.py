from django import forms

from .models import Resume, JobDescription


class ResumeUploadForm(forms.ModelForm):

    class Meta:
        model = Resume
        fields = ['candidate_name', 'email', 'resume_file']

def clean_resume_file(self):
    file = self.cleaned_data.get('resume_file')

    if file:
        if not file.name.lower().endswith('.pdf'):
            raise forms.ValidationError(
                "Only PDF files are allowed."
            )

        if file.size > 5 * 1024 * 1024:
            raise forms.ValidationError(
                "File size must be less than 5 MB."
            )

    return file



class JobDescriptionForm(forms.ModelForm):
    class Meta:
        model = JobDescription
        fields = ['job_title', 'description']

        widgets = {
            'job_title': forms.TextInput(attrs={
                'placeholder': 'Example: Python Full Stack Developer'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Paste the complete job description here...',
                'rows': 10
            })
        }
