from django.shortcuts import render
from  . models import Movie,seller,buyer
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import datetime
from django.db.models import Q
import secrets

# Create your views here.
def index(request):
    pro = Movie.objects.all()
    slr = seller.objects.all()
    return render(request,'index.html',{'products':pro,'seller':slr})


def search(request):
    if 'q' in request.GET:
        keyword = request.GET['q']
        if keyword:
            movies = Movie.objects.order_by('-time').filter(Q(name__icontains=keyword))
    return render(request,'search.html', {'movies':movies})



def buy(request,pk):
    print(pk)
    pro = Movie.objects.get(pk=pk)

    if  request.method == 'POST':
        name = request.POST['name']
        role = request.POST['role']
        no_ticket = request.POST['no_ticket']
        address = request.POST['address']
        phone = request.POST['phone']
        movie = request.POST.get('movie', False)
        quantity = int(request.POST['no_ticket'])

        code = ''.join(secrets.choice('12345678900987654321') for i in range(6))
        
        by = buyer(name=name,address=address,phone=phone,role=role,no_ticket=no_ticket)
        by.movie = pro
        by.amount_paid = (int(pro.price)) *(int(no_ticket))
        by.verified = True
        by.code = code 
        by.save()



        
        pn = pro.name
        dis = pro.dis
        price = pro.price
        pro_quantity =no_ticket
        pro_total = by.amount_paid         
        
        data = {'pname':pn,'pprice':price,'bname':name,'baddress':address,'bphone':phone,'pdis':dis,'pquantity':pro_quantity, 'ptotal':pro_total, 'id':by.code, 'purchase_date':by.purchase_date}
        return render(request, 'pdf.html', {'data': data,})

    return render(request, 'buy.html', {'movie':pro})


def payments(request):
    if request.is_ajax():
        role = request.POST.get('role', False)
        phone = request.POST.get('phone', False)
        name = request.POST.get('name', False)
        email = request.POST.get('email', False)
        amount = request.POST.get('amount', False)
        no_ticket = request.POST.get('no_ticket', False)
        ref = request.POST.get('ref', False)
        movie = request.POST.get('movie', False)
        deposited = True
        return JsonResponse({'deposited':deposited})


def order_complete(request,):
    ref = request.GET.get('ref')
    return render(request, 'order_complete.html', context={})


def pdf(request):
    slr = seller.objects.all()
    return render(request,'pdf.html',{'seller':slr})

