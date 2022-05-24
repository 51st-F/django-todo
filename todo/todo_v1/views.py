from distutils.log import info
from django.shortcuts import redirect, render
from .models import *
from .forms import *

# Create your views here.
def list(request):
    items = todo_item.objects.all()
    
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/todo_v1/')

    info = {'items':items, 'form':form}
    return render(request, 'list.html', info)

def finish_item(request, pk):
    item = todo_item.objects.get(id=pk)

    form = TodoForm(instance=item)
    if request.method == 'POST':
        request_modify = request.POST.copy()
        request_modify['item'] = item.item
        request_modify['finished'] = 'on'
        form = TodoForm(request_modify, instance=item)
        if form.is_valid():
            form.save()
        return redirect('/todo_v1/')

    info = {'form':form}
    return render(request, 'finish_item.html', info)

def delete_item(request, pk):
    item = todo_item.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/todo_v1/')
    info = {'item':item}
    return render(request, 'delete_item.html', info)