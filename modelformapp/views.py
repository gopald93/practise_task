from django.shortcuts import render
from .models import Collection,CollectionTitle
from .forms import CollectionForm,MaterialsFormset,Collection_Title_Edit_Form
from django.shortcuts import render
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone

def collection_details(request):
    collection_obj=Collection.objects.all()
    return render(request,'modelformapp/collection_main.html', {'collection_obj': collection_obj})

def collection_add(request):
    context={}
    if request.method == 'POST':
        form = CollectionForm(request.POST)
        if form.is_valid():
            collection_created_obj = form.save()
            formset = MaterialsFormset(request.POST,instance=collection_created_obj)
            if formset.is_valid():
                formset.save()
                return redirect('collection_details')
    else:
        context["form"]=CollectionForm()
        context["formset"]=MaterialsFormset()   
        return render(request,"modelformapp/collection_add.html",context)

def collection_edit(request,id=None):
    context={}
    collection_obj = get_object_or_404(Collection, pk=id)
    collection_title_obj=CollectionTitle.objects.filter(collection__pk=id)
    if request.method == 'POST':
        form = CollectionForm(request.POST,instance=collection_obj)
        if form.is_valid():
            collection_created_obj = form.save()
            formset = MaterialsFormset(request.POST,instance=collection_created_obj)
            if formset.is_valid():
                formset.save()
                return redirect('collection_details')
    else:
        context["form"]=CollectionForm(instance=collection_obj)
        context["formset"]=MaterialsFormset(instance=collection_obj)   
        return render(request,"modelformapp/collection_add.html",context)


def collection_delete(request,id=None):
    collection_obj = get_object_or_404(Collection, pk=id)
    if request.method == 'POST':
        collection_obj.delete()
        return redirect('collection_details')
    else:
        context = {}
        context['collection_obj'] = collection_obj
        return render(request, 'modelformapp/collection_delete.html', context)


def collection_each_details(request,id=None):
    collection_obj = get_object_or_404(Collection, pk=id)
    return render(request,'modelformapp/collection_each_details.html', {'collection_obj': collection_obj})


def collection_title_edit(request, id=None):
    collection_title_obj=get_object_or_404(CollectionTitle, pk=id)
    collection_obj = get_object_or_404(Collection, pk=collection_title_obj.collection.pk)
    if request.method == "POST":
        form = Collection_Title_Edit_Form(request.POST, instance=collection_title_obj)
        if form.is_valid():
            collection_form_obj = form.save(commit=False)
            collection_form_obj.collection = collection_obj
            collection_form_obj.save()
            return redirect('collection_each_details',id=collection_obj.id)
    else:
        form = Collection_Title_Edit_Form(instance=collection_title_obj)
    return render(request, 'modelformapp/collection_title_edit.html', {'form': form})        



def collection_title_delete(request,id=None):
    collection_title_obj=get_object_or_404(CollectionTitle, pk=id)
    if request.method == 'POST':
        collection_title_obj.delete()
        return redirect('collection_each_details',id=collection_title_obj.collection.id)
    else:
        context = {}
        context['collection_title_obj'] = collection_title_obj
        return render(request, 'modelformapp/collection_title_delete.html', context)




def collection_title_detail(request,id=None):
    collection_title_obj=get_object_or_404(CollectionTitle, pk=id)
    return render(request,'modelformapp/collection_title_details.html', {'collection_title_obj': collection_title_obj})    




 # <style>
 #                    #textInput {
 #                border: none;
 #                border-bottom: 3px solid aqua;
 #            }

 #            .userText {
 #                color: white;
 #                font-family: monospace;
 #                font-size: 17px;
 #                text-align: right;
 #                line-height: 30px;
 #            }
 #            .userText span {
 #                background-color: #009688;
 #                padding: 10px;
 #                border-radius: 2px;
 #            }
 #            .botText {
 #                color: white;
 #                font-family: monospace;
 #                font-size: 17px;
 #                text-align: left;
 #                line-height: 30px;
 #            }
 #            .botText span {
 #                background-color: #EF5350;
 #                padding: 10px;
 #                border-radius: 2px;
 #            }
 #    </style>

