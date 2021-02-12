from django.shortcuts import render

# Create your views here. Used Code from Code Institute - Project Boutique Ado -


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')