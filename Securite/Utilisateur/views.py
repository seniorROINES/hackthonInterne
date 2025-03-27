from django.shortcuts import render

def logging(request):
    return render(request, 'logging.html')

