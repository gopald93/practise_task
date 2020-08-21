from django.shortcuts import render
from .models import Employee,Family,FamilyMember
from .forms import EmployeeForm,MaterialsFormset
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone

def employee_details(request):
    employee_obj=Employee.objects.all()
    return render(request,'company/employee_details.html', {'employee_obj': employee_obj})




def employee_add(request):
    context={}
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee_created_obj = form.save()
            formset = MaterialsFormset(request.POST,instance=employee_created_obj)
            if formset.is_valid():
                formset.save()
                return redirect('employee_details')
    else:
        context["form"]=EmployeeForm()
        context["formset"]=MaterialsFormset()   
        return render(request,"company/employee_add.html",context)


def employee_edit(request,id=None):
    context={}
    employee_obj = get_object_or_404(Employee, pk=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST,instance=employee_obj)
        if form.is_valid():
            employee_created_obj = form.save()
            formset = MaterialsFormset(request.POST,instance=employee_created_obj)
            if formset.is_valid():
                formset.save()
                return redirect('employee_details')
    else:
        context["form"]=EmployeeForm(instance=employee_obj)
        context["formset"]=MaterialsFormset(instance=employee_obj)   
        return render(request,"company/employee_add.html",context)        


def employee_delete(request,id=None):
    employee_obj = get_object_or_404(Employee, pk=id)
    if request.method == 'POST':
        employee_obj.delete()
        return redirect('employee_details')
    else:
        context = {}
        context['employee_obj'] = employee_obj
        return render(request, 'company/employee_delete.html', context)
