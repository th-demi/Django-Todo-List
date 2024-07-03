from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ToDoList, Item
from .forms import CreateNewList

# Create your views here.
def index(request):
    return render(request, 'myapp/base.html',{})

def home(request):
    return render(request, 'myapp/home.html', {})

def list(request, id):
    tdl = ToDoList.objects.get(id=id)
    if request.method == "POST":
        print(request.POST.get("save"))
        if request.POST.get("save"):
            for item in tdl.item_set.all():
                print(request.POST.get("c" + str(item.id)))
                if request.POST.get("c" + str(item.id)) == "clicked":
                    item.completed = True
                else:
                    item.completed = False
                item.save()
        
        elif request.POST.get("newItem"):
            txt = request.POST.get("new")
            if len(txt) > 2:
                tdl.item_set.create(text=txt, completed=False)
            else:
                print("invalid")
    
    return render(request, 'myapp/list.html', {'lst': tdl})

def create(request):
    if request.method == 'POST':
        form = CreateNewList(request.POST)
        print(request.POST)
        print(form)
        if form.is_valid():
            name = form.cleaned_data['name']
            ToDoList.objects.create(name=name)
            return redirect('home')
    else:
        form = CreateNewList()
        print(form)
    return render(request, 'myapp/create.html', {'form': form})
