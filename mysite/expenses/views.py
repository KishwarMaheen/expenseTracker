from django.http import HttpResponse
from .models import Category, Item
from django.shortcuts import render, get_object_or_404
from django.db.models import Sum


# Create your views here.
def index(request):
    return render(request,
                  'expenses/index.html',
                  {'category_list': Category.objects.all()})


def category_detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    return render(request,
                  'expenses/category_detail.html',
                  {'category': category,
                   'total_expense': category.item_set.all().aggregate(Sum('amount'))['amount__sum']})


def item_detail(request, category_id, item_id):
    return render(request,
                  'expenses/item_detail.html',
                  {'item': get_object_or_404(Item, pk=item_id)})


def add_category(request):
    return HttpResponse("Still in development")


def add_item(response, category_id):
    return HttpResponse("Still in development")


def edit_item(response, category_id, item_id):
    return HttpResponse("Still in development")
