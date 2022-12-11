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

def single(request):
    return render(request, 'orphan/single.html',)

def service(request):
    return render(request, 'orphan/service.html',)

def team(request):
    return render(request, 'orphan/team.html',)

def donate(request):
    return render(request, 'orphan/donate.html',)

def volunteer(request):
    return render(request, 'orphan/volunteer.html',)

def contact(request):
    return render(request, 'orphan/contact.html',)
