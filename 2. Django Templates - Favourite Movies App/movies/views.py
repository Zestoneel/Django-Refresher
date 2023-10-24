from django.shortcuts import render, HttpResponse

# Create your views here.
def index(response):
    context = {
        "movies": ["Your Name", "Suzume", "Once Upon A Crime"]
    }
    return render(response, 'movies/index.html', context)

def about(response):
    return render(response, 'movies/about.html', {})