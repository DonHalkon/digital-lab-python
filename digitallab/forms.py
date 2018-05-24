from django import forms
from digitallab.models import Compound, ReagentLocation, Reagent


class CompoundForm(forms.ModelForm):
    iupacName = forms.CharField(help_text='UIPAC Name:')
    shortName = forms.CharField(help_text='Short Name:', min_length=1, required=False)
    molecularFormula = forms.CharField(widget=forms.HiddenInput)
    structure = forms.CharField(widget=forms.HiddenInput)
    cid = forms.CharField(help_text='CID:')

    class Meta:
        model = Compound
        fields = ('shortName', 'iupacName', 'molecularFormula', 'structure', 'cid', )

    def clean(self):
        cleaned_data = self.cleaned_data
        shortName = cleaned_data.get('shortName')
        if not len(shortName):
            cleaned_data['shortName'] = cleaned_data.get('iupacName')
            return cleaned_data
