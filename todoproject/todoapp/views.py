from django.shortcuts import render
from .models import TodoListItem
from django.http import HttpResponseRedirect
# Create your views here.
def home(request):
    all_todo_items = TodoListItem.objects.all()
    return render(request,'newhome.html',{'all_items':all_todo_items})
def addTodoView(request):
    x = request.POST['content']
    new_item = TodoListItem(content = x)
    new_item.save()
    return HttpResponseRedirect('/') 
def deleteTodoView(request,i):
    y = TodoListItem.objects.get(id= i)
    y.delete()
    return HttpResponseRedirect('/') 
def deletelist(request):
    y = TodoListItem.objects.all()
    y.delete()
    return HttpResponseRedirect('/')