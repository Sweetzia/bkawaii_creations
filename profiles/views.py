# Used the code from the Code Institute Project - Boutique Ado -
# Create your views here.

from django.shortcuts import render


def profile(request):
    """ Display the user's profile. """

    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)

