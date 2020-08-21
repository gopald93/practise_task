from django import forms
from .models import Employee,Family,FamilyMember
from django.forms.models import inlineformset_factory

class EmployeeForm(forms.ModelForm):
    class Meta:
        model =Employee
        fields = ('name','designation','department')

MaterialsFormset = inlineformset_factory(Employee,FamilyMember,fields=('f_name', 'relationship', 'f_designation'), can_delete=False, extra=2)

