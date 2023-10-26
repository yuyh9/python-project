from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as loginUser, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from app.forms import TodoForm
from app.models import Todo
# Create your views here.

@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        user = request.user
        form = TodoForm()
        all_todos = Todo.objects.filter(user=user).order_by('priority')
        
        # Configure the number of todos per page
        todos_per_page = 10
        paginator = Paginator(all_todos, todos_per_page)
        
        # Get the current page number from the request's GET parameters
        page_number = request.GET.get('page')
        
        # Get the todos for the current page
        todos = paginator.get_page(page_number)
        
        return render(request, 'index.html', context={'form': form, 'todos': todos})

@login_required(login_url='login')
def profile(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})

def login(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        context = {
            "form" : form
        }
        return render(request, 'login.html', context=context) 
    else:
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            print(form.is_valid())
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user is not None:
               loginUser(request, user) 
               return redirect("home")
            
        else:
            context = {
                "form" : form
            }
            return render(request, 'signup.html', context=context) 

def signup(request):
    if request.method == 'GET':
        form = UserCreationForm()
        context = {
        "form" : form
        }
        return render(request, 'signup.html', context=context) 
    else:
        print(request.POST)
        form = UserCreationForm(request.POST)
        context = {
            "form" : form
        }
        if form.is_valid():
            user = form.save()
            print(user)
            if user is not None:
                return redirect('login')
        else:
            return render(request, 'signup.html', context=context) 
        
@login_required(login_url='login')
def add_todo(request):
    if request.user.is_authenticated:
        user = request.user
        print(user)
        form = TodoForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            print(todo)
            return redirect("home")
        else: 
            return render(request, 'index.html', context={'form' : form})


def delete_todo(request, id):
    print(id)
    Todo.objects.get(pk = id).delete()
    return redirect('home')

def change_todo(request, id, status):
    todo = Todo.objects.get(pk = id)
    todo.status = status
    todo.save()
    return redirect('home')

def todo_detail(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_detail', todo_id=todo_id)
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo_detail.html', {'form': form, 'todo': todo})


def search(request):
    query = request.GET.get('query')
    if query:
        todos = Todo.objects.filter(title__icontains=query)
    else:
        todos = []
    return render(request, 'search_results.html', {'todos': todos, 'query': query})
    
def signout(request):
    logout(request)
    return redirect('login')