from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .models import Contact
from .models import orders
from .models import orderUpdate
from math import ceil
import json


# Create your views here.
def index(request):
    allprods = []
    catofproducts = Product.objects.values('product_category', 'id')
    cats = {item['product_category'] for item in catofproducts}
    for cat in cats:
        prods = Product.objects.filter(product_category= cat)
        n = len(prods)
        NSlides = n // 4 + ceil((n / 4) - (n // 4))
        allprods.append([prods, range(1, NSlides), NSlides])
    param = {'allprods': allprods}
    return render(request, 'shop/index.html', param)
def searchMatch(query,item):
    if query in item.product_name.lower() or query in item.product_des.lower() or query in item.product_category.lower() or query in item.product_subCategory.lower():
        return True
    else:
        return False


def search(request):
    query = request.GET.get('search')
    allprods = []
    catofproducts = Product.objects.values('product_category', 'id')
    cats= {item['product_category'] for item in catofproducts}
    for cat in cats:
        prods = Product.objects.filter(product_category=cat)
        prod = [item for item in prods if searchMatch(query, item)]
        n = len(prod)
        NSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) != 0 :
            allprods.append([prods, range(1, NSlides), NSlides])
    param = {'allprods': allprods, 'msg' : ""}
    if len(allprods) == 0 or len(query) < 3 :
        param = {'msg' : "Sorry! We could not find any product regarding this query"}

    return render(request, 'shop/search.html', param)

def about(request):

    return render(request, 'shop/about.html', )



def contact(request):
    if request.method == 'POST':
       contact_name= request.POST.get('cname', '')
       contact_email= request.POST.get('cemail', '')
       contact_phone= request.POST.get('cphone', '')
       contact_desc= request.POST.get('cmessage', '')

       contact_subject= request.POST.get('csubject', '')

       try:
            if contact_name != '' and contact_email != '' and contact_phone != '' and contact_subject != '' and contact_desc != '':
                contact = Contact(contact_name=contact_name, contact_email=contact_email, contact_phone=contact_phone,
                                  contact_subject=contact_subject, contact_desc=contact_desc)
                contact.save()
                contactid = {'id': contact.contact_id}
                response = json.dumps(contactid, default=str)
                return HttpResponse(response)
            else:
                contactid = {'id': 'Please Fill all the Fields'}
                response = json.dumps(contactid, default=str)
                return HttpResponse(response)

       except Exception as e:
            return HttpResponse(f'{e}')
            
       

    return render(request, 'shop/contact.html')   


def tracker(request):
    if request.method== 'POST':
        order_id= request.POST.get('orderid', '')
        email= request.POST.get('oemail', '')
        order = orders.objects.filter(order_id = order_id, email = email)
        try:
            if len(order)>0:
                update = orderUpdate.objects.filter(order_id = order_id)
                updates = []

                for item in update:
                    updates.append({'text': item.desc, 'time': item.timestamp})
                    response = json.dumps([updates, order[0].items_json] ,default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse("{}")
    return render(request, 'shop/tracker.html')

def productView(request, prodid):

    prods = Product.objects.filter(id=prodid)

    param = {'products': prods[0]}

    return render(request,"shop/prodview.html",param)
def checkout(request):
    if request.method == 'POST':
        items_json= request.POST.get('itemsJson','')
        name = request.POST.get('oname', '')
        email = request.POST.get('oemail', '')
        phone = request.POST.get('ophone', '')
        address = request.POST.get('oaddress', '')
        checkout= orders(items_json= items_json,  name= name, email = email, phone= phone, address = address)
        checkout.save()
        update= orderUpdate(order_id = checkout.order_id, desc= 'The Order has been Placed.')
        update.save()
        thank= True
        id= checkout.order_id
        return render(request, 'shop/checkout.html', {'thank': thank, 'id': id})

    return render(request, 'shop/checkout.html')
