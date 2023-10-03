from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def products(request):
    return render(request, 'products.html')
def contact(request):
    return render(request, 'contact.html')
def singleproduct(request):
    return render(request, 'single-product.html')

