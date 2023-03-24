from django.shortcuts import render
from .models import Category, TradeFair
from .forms import ImageForm

def HomeView(request):
    context = {}
    context["dataset"] = TradeFair.objects.all().order_by('title').values()
    return render(request, "branchenhome.html", context)


def CategoryView(request, cats):
    category_posts = TradeFair.objects.filter(category=cats)
    return render(request, 'trade_fair.html', {'cats':cats, 'category_posts':category_posts})


def NewBranchenView(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'newbranchen.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'newbranchen.html', {'form': form})
    # return render(request, "newbranchen.html")

def EditBranchenView(request, cats):
    # if request.method == 'POST':
    #     form = ImageForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         # Get the current instance object to display in the template
    #         img_obj = form.instance
    #         return render(request, 'newbranchen.html', {'form': form, 'img_obj': img_obj})
    # else:
    #     form = ImageForm()
    # return render(request, 'newbranchen.html', {'form': form})
   
    # return render(request, "editbranchen.html")
    category_posts = TradeFair.objects.filter(category=cats)
    return render(request, 'editbranchen.html', {'cats':cats, 'category_posts':category_posts})