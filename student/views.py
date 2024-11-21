from django.shortcuts import render,HttpResponse,get_object_or_404
from .models import insert_details
from .form import insert_form

# Create your views here.

def insert(request):
    if request.method == 'POST':
        form = insert_form(request.POST)
        if form.is_valid():
            form.save()
            dict_insert = {
        'insert' : insert_details.objects.all()
    }
        return render(request,'home.html',dict_insert)
        
    form = insert_form()
    dict_form={
        'form':form
    }
    return render(request,'insert.html',dict_form)

def home(request):
    dict_insert = {
        'insert' : insert_details.objects.all()
    }
    return render(request,"home.html",dict_insert)

def edit(request,id):
    instance_to_edit=insert_details.objects.get(pk=id)
    if request.POST:
        form=insert_form(request.POST,instance=instance_to_edit)
        if form.is_valid():
            instance_to_edit.save()
            dict_insert = {
        'insert' : insert_details.objects.all()
    }
            return render(request,'home.html',dict_insert)
    else:
        form=insert_form(instance=instance_to_edit)
    return render(request,'edit.html',{'form':form})

def delete(request,id):
    instance=insert_details.objects.get(pk=id)
    instance.delete()
    dict_insert = {
        'insert' : insert_details.objects.all()
    }
    return render(request,'home.html',dict_insert)

def views_page(request,id):
   student = get_object_or_404(insert_details, pk=id)  # Fetch student details
   return render(request, 'views.html', {'student': student})
