from django.shortcuts import redirect, render
from .models import Category, TradeFair, Branchen
from .forms import ImageForm
from django.core.files.storage import FileSystemStorage
import os
import string
from django.db.models import Max
import shutil
from messeninfo.settings import STATIC_URL, STATIC_ROOT
from django.templatetags.static import static

def HomeView(request):
    
    alphabet = string.ascii_uppercase
    context = {}
    context["dataset"] = TradeFair.objects.all().order_by('title').values()
    context["branchen"] = Branchen.objects.filter(sprach_id = 2).order_by('text').values()
    
    
    
    
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
        
        image1 = request.FILES.get('image1')
        image2 = request.FILES.get('image2')
        
        maxBid = Branchen.objects.all()
        temp = maxBid.aggregate(Max('b_id'))
        b_id = 0
        for key,val in temp.items():
            total = val + 1
            b_id = total
        print(b_id,key)
        
        updateData=TradeFair(b_id=b_id,image1=request.FILES.get('image1'),image2=request.FILES.get('image2'))
        updateData.save()
        
        de=Branchen(b_id=b_id,sprach_id = 1,text=request.POST.get('category1'),
        messe_text=request.POST.get('title1'),beschreibung=request.POST.get('description1'))
        de.save()
        
        en=Branchen(b_id=b_id,sprach_id = 2,text=request.POST.get('category2'),
        messe_text=request.POST.get('title2'),beschreibung=request.POST.get('description2'))
        en.save()
        
        es=Branchen(b_id=b_id,sprach_id = 3,text=request.POST.get('category3'),
        messe_text=request.POST.get('title3'),beschreibung=request.POST.get('description3'))
        es.save()
        
        fr=Branchen(b_id=b_id,sprach_id = 4,text=request.POST.get('category4'),
        messe_text=request.POST.get('title4'),beschreibung=request.POST.get('description4'))
        fr.save()
        
        ru=Branchen(b_id=b_id,sprach_id = 5,text=request.POST.get('category5'),
        messe_text=request.POST.get('title5'),beschreibung=request.POST.get('description5'))
        ru.save()
        
        cn=Branchen(b_id=b_id,sprach_id = 6,text=request.POST.get('category6'),
        messe_text=request.POST.get('title6'),beschreibung=request.POST.get('description6'))
        cn.save()
        
        return redirect('home')
        # img_obj = en.instance
        # return render(request, 'newbranchen.html', {'form': en, 'img_obj': en.image1})
    return render(request, "newbranchen.html")

def EditBranchenView(request, cats): 
    
    # category_posts = TradeFair.objects.filter(category_id=cats)
    # if request.method == 'POST':
    #     updateData = TradeFair.objects.get(category_id=cats)
    #     updateData.category_id = request.POST.get('category')
    #     updateData.title = request.POST.get('title')
    #     updateData.description = request.POST.get('description')
    #     updateData.image1 = request.FILES.get('image1')
    #     updateData.image2 = request.FILES.get('image2')
        
    #     # updateData=TradeFair(category_id=request.POST.get('category'),title=request.POST.get('title'),
    #     #     description=request.POST.get('description'),image1=request.FILES.get('image1'),image2=request.FILES.get('image2'))
    #     updateData.save()
    #     return redirect('home')
    # return render(request, 'editbranchen.html', {'cats':cats, 'category_posts':category_posts})
    
    category_posts = Branchen.objects.filter(b_id=cats)
    if request.method == 'POST':
        updateData = Branchen.objects.filter(b_id=cats)
        updateImage = TradeFair.objects.get(b_id = cats)
        deleteImage = TradeFair.objects.filter(b_id = cats).values()
        for p in updateData:
            print(p.text)
            match (p.sprach_id):
                case (1):
                    p.text = request.POST.get('category1')
                    p.messe_text = request.POST.get('title1')
                    p.beschreibung = request.POST.get('description1')
                    
                    # comment: 
                case (2):
                    p.text = request.POST.get('category2')
                    p.messe_text = request.POST.get('title2')
                    p.beschreibung = request.POST.get('description2')
                    
                case (3):
                    p.text = request.POST.get('category3')
                    p.messe_text = request.POST.get('title3')
                    p.beschreibung = request.POST.get('description3')
                    
                case (4):
                    p.text = request.POST.get('category4')
                    p.messe_text = request.POST.get('title4')
                    p.beschreibung = request.POST.get('description4')
                    
                case (5):
                    p.text = request.POST.get('category5')
                    p.messe_text = request.POST.get('title5')
                    p.beschreibung = request.POST.get('description5')
                    
                case (6):
                    p.category_id = request.POST.get('category6')
                    p.messe_text = request.POST.get('title6')
                    p.beschreibung = request.POST.get('description6')
                    
            
            p.save()
            
            
        if request.FILES.get('image1'):
            print(deleteImage[0]['image1'])
            os.remove(deleteImage[0]['image1'])
            updateImage.image1 = request.FILES.get('image1')
        if request.FILES.get('image2'):
            os.remove(deleteImage[0]['image2'])
            updateImage.image2 = request.FILES.get('image2')
        updateImage.save()
        
        return redirect('home')
    return render(request, 'editbranchen.html', {'cats':cats, 'category_posts':category_posts})

def DeleteBranchen(request, cats):
    category_posts = TradeFair.objects.filter(b_id=cats).values()
    url = './static/sector_images/%d' % cats
    print(url)
    shutil.rmtree(url, ignore_errors = False)
    # os.remove(category_posts[0]['image1'])
    # os.remove(category_posts[0]['image2'])
    
    Branchen.objects.filter(b_id=cats).delete()
    TradeFair.objects.filter(b_id=cats).delete()
    # print(category_posts[0].image1.url)
    # os.remove(category_posts[0].image1.url)
    return redirect('home')
    # return render(request, 'trade_fair.html', {'cats':cats, 'category_posts':category_posts})
    