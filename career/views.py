
from django.shortcuts import render, redirect
from .forms import ResumeUploadForm, JobDescriptionForm
from .models import (
    Resume,
    JobDescription,
    InterviewQuestion,
    InterviewAnswer
)
from .utils import match_resume_with_job
from .utils import generate_interview_questions
from .utils import evaluate_interview_answer
from django.db.models import Avg
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'career/home.html')


@login_required
def upload_resume(request):

    if request.method == 'POST':
        form = ResumeUploadForm(request.POST, request.FILES)

        if form.is_valid():
            resume = form.save()

            from .utils import extract_resume_text

            resume_text = extract_resume_text(resume.resume_file.path)

            resume.extracted_text = resume_text
            resume = form.save(commit=False)
            resume.user = request.user
            resume.save()
            

            print("Resume text saved successfully!")

            return redirect('resume_analysis', resume_id=resume.id)

    else:
        form = ResumeUploadForm()

    return render(request, 'career/upload_resume.html', {
        'form': form
    })


@login_required
def resume_analysis(request, resume_id):
    resume = get_object_or_404(
        Resume,
        id=resume_id,
        user=request.user
    )

    from .utils import analyze_resume_with_ai

    ai_analysis = analyze_resume_with_ai(resume.extracted_text)

    job = resume.job_descriptions.order_by('-created_at').first()

    job_match = None

    if job:
        job_match = match_resume_with_job(
            resume.extracted_text,
            job.description
        )

    return render(request, 'career/resume_analysis.html', {
        'resume': resume,
        'ai_analysis': ai_analysis,
        'job': job,
        'job_match': job_match,
    })


@login_required
def add_job_description(request, resume_id):
    resume = get_object_or_404(
        Resume,
        id=resume_id,
        user=request.user
    )

    if request.method == 'POST':
        form = JobDescriptionForm(request.POST)

        if form.is_valid():
            job = form.save(commit=False)
            job.resume = resume
            job.save()

            return redirect('resume_analysis', resume_id=resume.id)

    else:
        form = JobDescriptionForm()

    return render(request, 'career/job_description.html', {
        'form': form,
        'resume': resume
    })


@login_required
def interview_preparation(request, resume_id):
    resume = get_object_or_404(
        Resume,
        id=resume_id,
        user=request.user
    )

    job = resume.job_descriptions.order_by('-created_at').first()

    if not job:
        return redirect('add_job_description', resume_id=resume.id)

    if request.method == 'POST':
        questions = generate_interview_questions(
            resume.extracted_text,
            job.description
        )

        interview = InterviewQuestion.objects.create(
            resume=resume,
            job_description=job,
            questions=questions
        )

        return redirect(
            'interview_questions',
            interview_id=interview.id
        )

    return render(request, 'career/interview_preparation.html', {
        'resume': resume,
        'job': job
    })



@login_required
def interview_questions(request, interview_id):
    interview = get_object_or_404(
        InterviewQuestion.objects.select_related(
            'resume',
            'job_description'
        ),
        id=interview_id,
        resume__user=request.user
    )

    return render(
        request,
        'career/interview_questions.html',
        {'interview': interview}
    )


@login_required
def submit_interview_answer(request, interview_id):

    interview = get_object_or_404(
        InterviewQuestion,
        id=interview_id,
        resume__user=request.user
    )

    if request.method == 'POST':

        question = request.POST.get('question')
        candidate_answer = request.POST.get('candidate_answer')

        feedback, score = evaluate_interview_answer(
            question,
            candidate_answer
        )

        InterviewAnswer.objects.create(
            interview=interview,
            question=question,
            candidate_answer=candidate_answer,
            ai_feedback=feedback,
            score=score
        )

        return redirect(
            'interview_questions',
            interview_id=interview.id
        )

    return redirect(
        'interview_questions',
        interview_id=interview.id
    )


@login_required
def dashboard(request):
    total_resumes = Resume.objects.filter(
        user=request.user
    ).count()

    total_jobs = JobDescription.objects.filter(
        resume__user=request.user
    ).count()

    total_interviews = InterviewQuestion.objects.filter(
        resume__user=request.user
    ).count()

    total_answers = InterviewAnswer.objects.filter(
        interview__resume__user=request.user
    ).count()

    average_score = InterviewAnswer.objects.filter(
        interview__resume__user=request.user
    ).aggregate(
        average=Avg('score')
    )['average'] or 0

    answers = InterviewAnswer.objects.filter(
        interview__resume__user=request.user
    ).exclude(
        score__isnull=True
    ).order_by('created_at')[:10]

    chart_labels = [
        f"Attempt {i}" for i in range(1, len(answers) + 1)
    ]

    chart_scores = [answer.score for answer in answers]

    # Latest 5 uploaded resumes
    recent_resumes = Resume.objects.filter(
        user=request.user
    ).order_by('-uploaded_at')[:5]
    print("RECENT RESUMES:", list(recent_resumes))

    return render(request, 'career/dashboard.html', {
        'total_resumes': total_resumes,
        'total_jobs': total_jobs,
        'total_interviews': total_interviews,
        'total_answers': total_answers,
        'average_score': round(average_score, 1),
        'chart_labels': chart_labels,
        'chart_scores': chart_scores,
        'recent_resumes': recent_resumes,
    })

@login_required
def resume_history(request):
    resumes = Resume.objects.filter(
        user=request.user
    ).order_by('-uploaded_at')

    return render(request, 'career/resume_history.html', {
        'resumes': resumes
    })

@login_required
@require_POST
def delete_resume(request, resume_id):
    resume = get_object_or_404(
        Resume,
        id=resume_id,
        user=request.user
    )

    if resume.resume_file:
        resume.resume_file.delete(save=False)

    resume.delete()

    return redirect('resume_history')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'career/register.html', {
        'form': form
    })