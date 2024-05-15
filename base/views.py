from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Product
import json
from .forms import ProductForm


def get_products(request, user_id):
    if request.method == 'GET':
        data_objects = Product.objects.filter(user_id = user_id)
        return render(request, 'products.html', {'data': data_objects} )
    
def get_product(request, pk):
    if request.method == 'GET':
        product = Product.objects.get(id = pk)
        return render(request, 'product.html', {'data': product} )
    
def add_products(request, user_id):
    form = ProductForm()
    print(user_id)
    
    if request.method == 'POST':
        user = Product(user_id= user_id)
        form = ProductForm(request.POST, instance=user)
        if form.is_valid:
            form.save()
            return redirect('get_products', user_id= user_id)
    context = {'form': form}
    return render(request, 'products_form.html', context)

def update_product(request, pk):
    product = Product.objects.get(id = pk)
    form = ProductForm(instance = product)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance= product)
        if form.is_valid:
            form.save()
            return redirect('product', pk = pk)
    context = {'form': form}
    return render(request, 'products_form.html', context)

def delete_product(request, pk):
    product = Product.objects.get(id = pk)

    if request.method == 'POST':
        product.delete()
        return redirect('get_products', user_id= 1)
    context = {'form': product}
    return render(request, 'delete.html', context )
# def add_products(request, user_id):
#     if request.method == 'POST':

#         data = json.loads(request.body)
#         products = Product(
#             user_id = user_id,
#             name = data.get('name'),
#             price = data.get('price'),
#             stock= data.get('stock'),
#             image = data.get('image'),
#             barcode = data.get('barcode'),
#             category = data.get('category')
#         )
#         products.save()
#         return HttpResponse('adding products successfully')
        
# @csrf_exempt   
# def update_product(request, id):
#     if request.method == 'PUT':

#         req = json.loads(request.body)
#         # prod = Products.objects.filter(id=_id)
#         product = Product.objects.get(pk=id)

#         # update product depending on the request key & value
#         for key, value in req.items():
#             setattr(product, key, value)
#         product.save()

#         return HttpResponse('updating product successfully')
        
#     if request.method == 'DELETE':

#         product = Product.objects.get(pk=id)
#         product.delete()
#         return HttpResponse('product deleted successfully')


# def filter_products(request):
#     if request.method == 'GET':

#         req = json.loads(request.body)
#         product = {}
#         #filter by barcode 
#         if list(req.keys())[0] == 'barcode':
#             product = Product.objects.filter(barcode= req['barcode'])
            
#         # filter by name
#         if list(req.keys())[0] == 'name':
#             product = Product.objects.filter(user_id= req['user_id'], name__contains= req['name'])
                
#         array = []
#         for obj in product:
#             array.append({
#                 'name': obj.name,
#                 'price': obj.price,
#                 'stock': obj.stock,
#                 'image': obj.image,
#                 'barcode': obj.barcode,
#                 'category': obj.category
#             })
#         return JsonResponse({'data': array})
