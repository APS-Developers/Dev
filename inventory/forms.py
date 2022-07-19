from django import forms
from .models import Inventory
from .models import Csvs
from customer.models import Organisation
 
StatusChoice=[
        ('', 'None'),
        ('Working','Working'),
        ('Not Working','Not Working')
    ]

# creating a form
class Form(forms.ModelForm):
    
    Make = forms.CharField(widget=forms.TextInput(attrs={
        'id': '',
        'type': 'text'
    }), label='')

    Part_Code = forms.CharField(widget=forms.TextInput(attrs={
        'id': '',
        'type': 'text'
    }), label='')

    Serial_Number = forms.CharField(widget=forms.Textarea(attrs={
        'id': '',
        'type': 'text',
        'cols': '30',
        'rows': '1'
    }), label='')

    Item = forms.CharField(widget=forms.TextInput(attrs={
        'id': '',
        'type': 'text'
    }), label='')

    Location = forms.CharField(widget=forms.Textarea(attrs={
        'id': '',
        'type': 'text',
        'cols': '30',
        'rows': '2'
    }), label='')

    Purchase_Date = forms.DateField(required=False, widget=forms.TextInput(attrs={
        'id': '',
        'type': 'date'
    }), label='')    

    Item_dispatched_Date = forms.DateField(required=False, widget=forms.TextInput(attrs={
        'id': '',
        'type': 'date'
    }), label='')    
        
    Organisation = forms.ModelChoiceField(required=False, queryset=Organisation.objects.all(),
        widget=forms.Select(attrs={
        'id': ''
        }), label='')

    Status = forms.ChoiceField(required=False, choices=StatusChoice,
        widget=forms.Select(attrs={
        'id': ''
        }), label='')

    Slip = forms.FileField(required=False, widget=forms.FileInput(attrs={
        'id': '',
        'type': 'file'
    }), label='')

    # create meta class
    class Meta:
        # specify model to be used
        model = Inventory
 
        # specify fields to be used
        fields = [
            'Make',
            'Part_Code',
            'Serial_Number',
            'Item',
            'Location',
            'Purchase_Date',
            'Item_dispatched_Date',
            'Organisation',
            'Status',
            'Slip',
        ]



class CsvsModelForm(forms.ModelForm):
	class Meta:
		model=Csvs
		fields=("file_name",)







