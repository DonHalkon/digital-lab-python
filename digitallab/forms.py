from django.forms import ModelForm

from digitallab.models import ReagentLocation


class ReagentLocationForm(ModelForm):
    class Meta:
        model = ReagentLocation
        fields = '__all__'

    def is_valid(self):
        if len(self.descr) > 3:
            return True
        return False
