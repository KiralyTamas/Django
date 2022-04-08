from django import forms
from clinicalApp.models import Patient,ClinicalData

class PatientForm(forms.ModelForm):
    class Meta:
        model=Patient
        fields='__all__'
        
class ClinicalForm(forms.ModelForm):
    class Meta:
        model=ClinicalData
        fields='__all__'