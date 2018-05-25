from django import forms
from digitallab.models import Compound, ReagentLocation, Reagent, units


class CompoundForm(forms.ModelForm):
    iupacName = forms.CharField(help_text='UIPAC Name')
    shortName = forms.CharField(help_text='Short Name', min_length=1, required=False)
    molecularFormula = forms.CharField(widget=forms.HiddenInput)
    structure = forms.CharField(widget=forms.HiddenInput)
    cid = forms.CharField(help_text='CID')

    class Meta:
        model = Compound
        fields = ('shortName', 'iupacName', 'molecularFormula', 'structure', 'cid', )

    def clean(self):
        cleaned_data = self.cleaned_data
        shortName = cleaned_data.get('shortName')
        if not len(shortName):
            cleaned_data['shortName'] = cleaned_data.get('iupacName')
            return cleaned_data


class ReagentLocationForm(forms.ModelForm):
    descr = forms.CharField(help_text='Description', min_length=3)

    class Meta:
        model = ReagentLocation
        fields = ('descr', )


class ReagentForm(forms.ModelForm):
    receiptDate = forms.DateField(help_text='Reception date')
    storageLife = forms.CharField(help_text='Storage life')
    compoundId = forms.ModelChoiceField(Compound)
    amount = forms.CharField(max_length=20)
    measurementUnits = forms.ChoiceField(choices=units)
    reagentLocation = forms.ModelChoiceField(ReagentLocation)
    comments = forms.CharField(max_length=200)

    class Meta:
        model = Reagent
        fields = ('receiptDate', 'storageLife', 'compoundId', 'amount', 'measurementUnits', 'reagentLocation',
                  'comments', )
