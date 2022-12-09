from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from api.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import json


@login_required
def main(request):

    subcategories = Subcategory.objects.all().order_by('parent_category_id')
    categories = Category.objects.all()

    return render(request, 'main/main.html', {'categories': categories, 'subcategories': subcategories})


def auth(request):

    if request.method == 'POST':

        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=email, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('banners')
        else:
            return redirect('auth')

    return render(request, 'main/auth.html')


@login_required
def banners(request):

    subcategories = Subcategory.objects.all().order_by('parent_category_id')
    categories = Category.objects.all()

    return render(request, 'main/banners.html', {'categories': categories, 'subcategories': subcategories})


@login_required
def payment(request):
    orders = Order.objects.filter(user=request.user).first()
    account = Account.objects.filter(user=request.user.id).first()
    total = 0
    for item in json.loads(orders.order):
        item_data = json.loads(orders.order)[item]
        cat_total = item_data['total']
        total += cat_total

    return render(request, 'main/payment.html', {'total': total, 'order_id': orders.id, 'account': account})


@login_required
def basket(request):
    order = {}
    orders = Order.objects.filter(user=request.user).first()
    total = 0
    for item in json.loads(orders.order):
        item_id = Product.objects.get(id=item)
        item_data = json.loads(orders.order)[item]
        cat_total = item_data['total']
        total += cat_total
        # category_total += total
        category = item_id.category.parent_category.name
        if category not in order:
            order[category] = {'total': cat_total, 'cat_id': item_id.category.parent_category.id,
                               'data': [{'product': item_id, 'count': item_data['count'], 'total': item_data['total']}]}
        else:
            order[category]['data'].append(
                {'product': item_id, 'count': item_data['count'], 'total': item_data['total']})
            order[category]['total'] += cat_total

    return render(request, 'main/basket.html', {'order': order, 'total': total})


@login_required
def account(request):

    account = Account.objects.filter(user=request.user.id).first()
    return render(request, 'main/account.html', {'account': account})


@login_required
def categories(request, itemid):

    if itemid > 10:
        return redirect('main', permanent=True)

    return HttpResponse(f'categories {itemid}')


def pageNotFound(request, exception):
    return redirect('auth')


@login_required
def logout_(request):
    """Logout"""
    logout(request)
    return redirect('auth')
