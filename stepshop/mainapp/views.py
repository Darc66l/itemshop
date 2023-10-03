from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def prodocuts(request):
    return render(request, 'products.html')

