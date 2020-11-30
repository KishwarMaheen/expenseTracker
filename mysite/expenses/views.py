from django.http import HttpResponse, HttpResponseRedirect
from .models import Category, Item
from django.shortcuts import render, get_object_or_404
from django.db.models import Sum
from django.urls import reverse


# Create your views here.
def index(request):
    return render(request,
                  'expenses/index.html',
                  {'category_list': Category.objects.all()})


def category_detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    category.total_amount = category.item_set.all().aggregate(Sum('amount'))['amount__sum']
    category.save()
    return render(request,
                  'expenses/category_detail.html',
                  {'category': category})


def item_detail(request, category_id, item_id):
    return render(request,
                  'expenses/item_detail.html',
                  {'item': get_object_or_404(Item, pk=item_id)})


def add_category(request):
    return render(request, 'expenses/add_category.html')


def add_item(request, category_id):
    return render(request,
                  'expenses/add_item.html',
                  {'category': get_object_or_404(Category, pk=category_id)})


def edit_item(request, category_id, item_id):
    return render(request,
                  'expenses/edit_item.html',
                  {'item': get_object_or_404(Item, pk=item_id)})


def add_category_process(request):
    name = request.POST['category_name']
    c = Category(name=name)
    c.save()
    return HttpResponseRedirect("http://localhost:8000/expenses/")


def add_item_process(request, category_id):
    c = get_object_or_404(Category, pk=category_id)
    name = request.POST['item_name']
    amount = request.POST['item_amount']
    c.item_set.create(name=name, amount=amount)
    return HttpResponseRedirect("http://localhost:8000/expenses/category_detail/{}".
                                format(category_id))


def edit_item_process(request, category_id, item_id):
    i = get_object_or_404(Item, pk=item_id)
    i.name = request.POST['item_name']
    i.amount = request.POST['item_amount']
    i.save()
    return HttpResponseRedirect("http://localhost:8000/expenses/category_detail/{}".format(category_id, item_id))
