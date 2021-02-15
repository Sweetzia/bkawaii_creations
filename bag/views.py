from django.shortcuts import render

# Create your views here. Used Code from Code Institute - Project Boutique Ado -

def view_bag(request):
    """ A view that renders the shoppingbag contents page """

    return render(request, 'bag/bag.html')