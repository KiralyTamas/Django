from django import forms

class ItemForm(forms.Form):
    name=forms.CharField(max_length=40)
    quantity=forms.IntegerField()