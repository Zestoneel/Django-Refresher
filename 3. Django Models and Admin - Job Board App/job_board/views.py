from django.shortcuts import render, get_object_or_404
from .models import JobPosting

# Create your views here.
def index(request):
    # jobs = JobPosting.objects.all()
    # jobs = JobPosting.objects.filter(is_Active=True)
    # print(jobs)
    active_postings = JobPosting.objects.filter(is_Active=True)
    context = {
        'job_postings':active_postings
    }
    # return HttpResponse('<h1>Job Board</h1>')
    return render(request, 'job_board/index.html', context)

def job_detail(request, pk):
    active_posting = get_object_or_404(JobPosting,pk=pk, is_Active=True)
    context = {
        'posting':active_posting
    }
    return render(request, 'job_board/detail.html', context)