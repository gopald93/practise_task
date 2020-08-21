from django import forms
from .models import Collection,CollectionTitle
from django.forms.models import inlineformset_factory

class CollectionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model =Collection
        fields = ('subject','owner','note')

MaterialsFormset = inlineformset_factory(Collection,CollectionTitle,fields=('name', 'language'), can_delete=False, extra=3)



class Collection_Title_Edit_Form(forms.ModelForm):
    class Meta:
        model = CollectionTitle
        fields = ('name','language')
