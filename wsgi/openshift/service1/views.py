from django.shortcuts import render, render_to_response

# Create your views here.
def hi(request):
    return render_to_response('home/home2.html')
