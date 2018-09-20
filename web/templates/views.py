from django.shortcuts import render_to_response

from blog.models import posts

def home(request):
    return render_to_response ('website.html', {'title' : 'My first stap'})