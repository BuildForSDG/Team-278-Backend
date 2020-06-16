from django.shortcuts import render

# Create your views here.

# views for the Home Page.
def homePage(request):
    return render(request, 'home/homePage.html', {})

