from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'orphan/index.html',)

def about(request):
    return render(request, 'orphan/about.html',)

def causes(request):
    return render(request, 'orphan/causes.html',)

def event(request):
    return render(request, 'orphan/event.html',)

def blog(request):
    return render(request, 'orphan/blog.html',)
