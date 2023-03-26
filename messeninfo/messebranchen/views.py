from django.shortcuts import redirect, render
from .models import Category, TradeFair
from .forms import ImageForm
from django.core.files.storage import FileSystemStorage
import os
import string

def HomeView(request):
    
    alphabet = string.ascii_uppercase
    context = {}
    context["dataset"] = TradeFair.objects.all().order_by('title').values()
    context["alphabet"] = alphabet
    return render(request, "branchenhome.html", context)

def CategoryView(request, cats):
    category_posts = TradeFair.objects.filter(category=cats)
    return render(request, 'trade_fair.html', {'cats':cats, 'category_posts':category_posts})

def NewBranchenView(request):
    # if request.method == 'POST':
    #     form = ImageForm(request.POST, request.FILES)
    #     print (form)
    #     if form.is_valid():
    #         form.save()
    #         # Get the current instance object to display in the template
    #         img_obj = form.instance
    #         return render(request, 'newbranchen.html', {'form': form, 'img_obj': img_obj})
    # else:
    #     form = ImageForm()
    # return render(request, 'newbranchen.html', {'form': form})
   
    if request.method == 'POST':
   
        en=TradeFair(category_id=request.POST.get('category'),title=request.POST.get('title'),
        description=request.POST.get('description'),image1=request.FILES.get('image1'),image2=request.FILES.get('image2'))
        en.save()
        
        return redirect('home')
        # img_obj = en.instance
        # return render(request, 'newbranchen.html', {'form': en, 'img_obj': en.image1})
    return render(request, "newbranchen.html")

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
    category_posts = TradeFair.objects.filter(category_id=cats)
    if request.method == 'POST':
        updateData = TradeFair.objects.get(category_id=cats)
        updateData.category_id = request.POST.get('category')
        updateData.title = request.POST.get('title')
        updateData.description = request.POST.get('description')
        updateData.image1 = request.FILES.get('image1')
        updateData.image2 = request.FILES.get('image2')
        
        # updateData=TradeFair(category_id=request.POST.get('category'),title=request.POST.get('title'),
        #     description=request.POST.get('description'),image1=request.FILES.get('image1'),image2=request.FILES.get('image2'))
        updateData.save()
        return redirect('home')
    return render(request, 'editbranchen.html', {'cats':cats, 'category_posts':category_posts})
def DeleteBranchen(request, cats):
    category_posts = TradeFair.objects.filter(category_id=cats).values()
    
    os.remove(category_posts[0]['image1'])
    os.remove(category_posts[0]['image2'])
    
    TradeFair.objects.filter(category_id=cats).delete()
    # print(category_posts[0].image1.url)
    # os.remove(category_posts[0].image1.url)
    return redirect('home')
    # return render(request, 'trade_fair.html', {'cats':cats, 'category_posts':category_posts})
    