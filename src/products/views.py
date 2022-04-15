from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404

from .forms import ProductForm, RawProductForm
from .models import Product
# Create your views here.

def render_initial_data(request):
    initial_data = {
        'title': "My awesome title"
    }
    obj = Product.objects.get(id=1) #this steps update the first obj
    #form = ProductForm(request.POST or None, initial = initial_data1)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    
    context = {
        'form': form
    }
    return render(request, "products/product_rend_ini.html", context)

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm() #rerender
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)

def product_update_view(request, id=id):
    obj = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)

def product_list_view(request):
    queryset = Product.objects.all() #list of objects
    context = {
        "object_list": queryset
    }
    return render(request, "products/product_list.html", context)

# def product_create_view(request):
#     # print('get')
#     # print(request.GET)
#     # print('request title '+request.GET['title'])
#     # print('post')
#     # print(request.POST)
#     if request.method == 'POST':
#         my_new_title = request.POST.get('title')
#         # print('new title ')
#         print(my_new_title)
#         #Product.objects.create(title=my_new_title)
#     context = {}
#     return render(request, "products/product_create.html", context)

def product_form_view(request):
    my_form = RawProductForm() #equal to RawProductForm(request.GET)
    if request.method == 'POST':
        my_form = RawProductForm(request.POST)
        if my_form.is_valid():
            #now the data is good
            print(my_form.cleaned_data)
            #Product.objects.create(my_form.cleaned_data)#error takes 1 positional argument but 2 were given
            Product.objects.create(**my_form.cleaned_data)#workd fine
        else:
            print(my_form.errors)
    context = {
        'form': my_form
    }
    return render(request, "products/product_form.html", context)

def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description,
    # }
    context = {
        'object': obj
    }
    return render(request, "products/product_detail.html", context)

def dynamic_lookup_view(request, id):
    #obj = Product.objects.get(id=id)
    obj = get_object_or_404(Product, id=id)
    # try:
    #     obj = Product.objects.get(id=id)
    # except Product.DoesNotExist:
    #     raise Http404
    context = {
        "object": obj
    }

    return render(request, "products/product_detail2.html", context)
    
def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        #confirming delete
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "products/product_delete.html", context)
    