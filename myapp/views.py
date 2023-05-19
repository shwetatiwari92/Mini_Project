from django.shortcuts import render
from .models import *

# Create your views here.
def admin_index(request):
    p1 = Product.objects.get(P_name = 'Samsung')
    filtered_Product = Product_sub.objects.all()
    try:
        
        return render(request,'admin_index.html', {'Products': filtered_Product})
    except:
        return render(request,'admin_index.html')


def add_product(request):
    return render(request,'add_product.html')

def edit_product(request, pid):
    productdata = Product_sub.objects.get(id = pid)
    if request.method == 'GET':
        return render(request,'edit_product.html', {'productdata': productdata})
    else:
        productdata.Model_no = request.POST['model']
        productdata.P_price = request.POST['price']
        productdata.P_ram = request.POST['ram']
        try:
            productdata.P_image = request.FILES['pic']
            productdata.save()
            return render(request, 'edit_product.html', {'productdata':productdata})
        except:
            productdata.save()
            return render(request, 'edit_product.html', {'productdata':productdata})