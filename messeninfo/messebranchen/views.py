from django.shortcuts import render
from .models import Category, TradeFair


def HomeView(request):
    context = {}
    context["dataset"] = Category.objects.all().order_by('category_name').values()
    return render(request, "home.html", context)


def CategoryView(request, cats):
    category_posts = TradeFair.objects.filter(category=cats)
    return render(request, 'trade_fair.html', {'cats':cats, 'category_posts':category_posts})


