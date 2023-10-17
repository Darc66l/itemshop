from django.shortcuts import render

def index(request):
    title="Home"
    links_menu = [{'link':'index','name':'Главная'},
                  {'link':'about','name':'О нас'},
                  {'link':'products:index','name':'Продукты'},
                  {'link':'contact','name':'Контакты'},
    
                  ]
    context = {'title': title,
               'links_menu':links_menu,
    }

    return render(request, 'index.html',context)
def about(request):
    title="About US"
    
    context = {'title': title}

    return render(request, 'about.html',context)
def products(request):
    title="Каталог продуктов"
    context = {'title': title}

    return render(request, 'products.html',context)
def contact(request):
    title="Contacts"
    context = {'title': title}

    return render(request, 'contact.html',context)
def product(request):
    title="Product"
    context = {'title': title}

    return render(request, 'single-product.html',context)

