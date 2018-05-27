from django import forms
from django.core.exceptions import ValidationError

from digitallab.models import Compound, ReagentLocation, Reagent, units


class CompoundModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.shortName


class ReagentLocationChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.descr


class CompoundForm(forms.ModelForm):
    iupacName = forms.CharField(help_text='UIPAC Name', required=False)
    shortName = forms.CharField(help_text='Short Name', min_length=0, required=False)
    molecularFormula = forms.CharField(widget=forms.HiddenInput, required=False)
    structure = forms.CharField(widget=forms.HiddenInput)
    cid = forms.CharField(help_text='CID', required=False)

    class Meta:
        model = Compound
        fields = ('shortName', 'iupacName', 'molecularFormula', 'structure', 'cid',)

    def clean(self):
        cleaned_data = self.cleaned_data
        shortName = cleaned_data.get('shortName')
        if not len(shortName):
            if not len(cleaned_data.get('iupacName')):
                raise ValidationError('Either short name or IUPAC name have to be specified')
            cleaned_data['shortName'] = cleaned_data.get('iupacName')
            return cleaned_data


class ReagentLocationForm(forms.ModelForm):
    descr = forms.CharField(help_text='Description', min_length=3)

    class Meta:
        model = ReagentLocation
        fields = ('descr',)


class ReagentForm(forms.ModelForm):
    receiptDate = forms.DateField(help_text='Reception date', required=False)
    storageLife = forms.CharField(help_text='Storage life', required=False)
    compound = CompoundModelChoiceField(Compound.objects, help_text='Select compound')
    amount = forms.CharField(max_length=20, help_text='Amount', required=False)
    measurementUnits = forms.ChoiceField(choices=units, help_text='Measurement units')
    reagentLocation = ReagentLocationChoiceField(ReagentLocation.objects, help_text='Select location')
    comments = forms.CharField(max_length=200, help_text='Comments', required=False)

    class Meta:
        model = Reagent
        fields = ('receiptDate', 'storageLife', 'compound', 'amount', 'measurementUnits', 'reagentLocation',
                  'comments',)
