from django.shortcuts import render, redirect


def index(request):
    return render(request, "survey_app/index.html")

def process(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    request.session['count'] += 1
    request.session['post'] = request.POST

    print request.session['count']
    print request.session['post']

    return redirect("/submitted")

def submitted(request):

    return render(request, "survey_app/submitted.html")

def back(request):

    return redirect('/')