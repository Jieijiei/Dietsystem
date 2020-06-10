from django.shortcuts import render, redirect
from .models import Weight
from .forms import WeightForm

# Create your views here.
def index(request):
    data = Weight.objects.all()
    params = {
    'title' : 'my weight memory',
    'data' : data
    }
    return render(request, 'weight/index.html', params)

def create(request):
    params = {
    'title': 'score',
    'form': WeightForm()
    }

    if (request.method=='POST'):
        obj = Weight()
        weight = WeightForm(request.POST, instance=obj)
        height = WeightForm(request.POST, instance=obj)
        weight.save()
        height.save()
        bmi = int(request.POST['weight']) / (int(request.POST['height'])/100 )**2
        bmi.save()
        return redirect(to='/weight')
    return render(request, 'weight/create.html', params)

def edit(request, num):
    obj = Weight.objects.get(id=num)
    if (request.method=='POST'):
        weight = WeightForm(request.POST, instance=obj)
        height = WeightForm(request.POST, instance=obj)
        weight.save()
        height.save()
        return redirect(to='/weight')
    params = {
    'title' : 'edit',
    'id':num,
    'msg': '嘘はよくないよ',
    'form': WeightForm(instance=obj)
    }
    return render(request, 'weight/edit.html', params)

def delete(request, num):
    weight = Weight.objects.get(id=num)
    height = Weight.objects.get(id=num)
    if (request.method=='POST'):
        weight.delete()
        height.delete()
        return redirect(to='/weight')
    params = {
    'title': 'delete',
    'msg': '本当に消す？',
    'id':num,
    'obj':weight
    }
    return render(request, 'weight/delete.html', params)