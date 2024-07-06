from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from .models import ToDoList, Item
from .forms import CreateNewList
from django.contrib.auth import logout

# Create your views here.
def index(request):
    return render(request, 'myapp/base.html',{})

def home(request):
    return render(request, 'myapp/home.html', {})


def create(request):
    if request.method == "POST":
        form = CreateNewList(request.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n, user=request.user)  # Associate the current user with the ToDoList
            t.save()
        return redirect(f"/{t.id}")
    else:
        form = CreateNewList()
    return render(request, 'myapp/create.html', {'form': form})

def view(request):
    return render(request, 'myapp/view.html', { })

def list(request, id):
    tdl_id = get_object_or_404(ToDoList, id=id)
    if tdl_id in request.user.todolist.all():
        if request.method == "POST":
            if "save" in request.POST:
                for item in tdl_id.item_set.all():
                    if request.POST.get("c" + str(item.id)) == "clicked":
                        item.completed = True
                    else:
                        item.completed = False
                    item.save()
            elif "newItem" in request.POST:
                txt = request.POST.get("new")
                if len(txt) > 2:
                    tdl_id.item_set.create(text=txt, completed=False)
                else:
                    print("invalid")
    else:
        return HttpResponse("You do not have permission to view this ToDo list.", status=403)
    
    return render(request, 'myapp/list.html', {'lst': tdl_id})


def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('')