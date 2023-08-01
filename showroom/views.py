from django.shortcuts import render
from .models import *
# Create your views here.

def showroom_view(request):
    showroom = Showroom.objects.first()
    # models = Models.objects.all()
    models = Models.objects.order_by('?')[:3] #randomly picks 3 models from the database, 
    brands = Brands.objects.order_by('?')[:3]

    return render(request,'showroom/home.html',{'showroom':showroom,'models':models,'brands':brands})

def brand_list_view(request):
    brands = Brands.objects.all()
    return render(request,'showroom/brands_list.html',{'brands':brands})

def brand_models(request,brand_id):
    # models = Models.objects.get(brand = brand_id)
    brand = Brands.objects.get(id= brand_id)
    models = brand.models.all()

    return render(request,'showroom/models_list.html',{'models':models})

def models_list_view(request):
    models = Models.objects.all()
    return render(request,'showroom/models_list.html',{'models':models})

def model_detail(request,model_id):
    model = Models.objects.get(id = model_id)
    return render(request,'showroom/model_detail.html',{'model':model})

def team_list(request):
    team = Team.objects.all()
    return render(request,'showroom/team_list.html',{'team':team})

def member_detail(request,member_id):
    member = Team.objects.get(id = member_id)
    return render(request,'showroom/member_detail.html',{'member':member})

