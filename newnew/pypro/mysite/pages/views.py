from django.shortcuts import render
from django.template import loader 
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Book, Order, OrderItem
from .forms import OrderForm
from .models import *
def index(request):
    books = Book.objects.all()
    return render(request, 'pages/base.html', {'books': books})

# def book_detail(request, book_id):
#     book = get_object_or_404(Book, pk=book_id)
#     return render(request, 'book_detail.html', {'book': book})

# def order_create(request):
#     if request.method == 'POST':
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             order = form.save()
#             return render(request, 'order_created.html', {'order': order})
#     else:
#         form = OrderForm()
#     return render(request, 'order_create.html', {'form': form})

# def order_detail(request, order_id):
#     order = get_object_or_404(Order, pk=order_id)
#     return render(request, 'order_detail.html', {'order': order})







# def  index (response):
#     return HttpResponse("<h1>helloworld!</h1> ")

# def index(request):
#   template = loader.get_template('pages/home.html')
#   context = {
#     'firstname': 'asghar',
#   }
#   return HttpResponse(template.render(context, request))



# def index(request):
#   template = loader.get_template('pages/home.html')
#   context = {
#     # 'fruits': ['Apple', 'Banana', 'Cherry', 'Orange']
#     'myvar':1
#     }
#   return HttpResponse(template.render(context, request))             


# def index (request):
#     students=Student.objects.all().values()
#     template=loader.get_template('pages/home.html')
#     context={
#         'students':students,
#     }
#     return HttpResponse(template.render(context,request))

# def  index (response):
#     return render(response,"pages/index.html",{})

# def index(request):
#     posts=Post.objects.all()
#     return render(request,'pages/home.html',{'posts':posts})