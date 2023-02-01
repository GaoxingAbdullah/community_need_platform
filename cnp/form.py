from django.forms import ModelForm

from .models import RequestResource

class RequestResourceForm(ModelForm):
    class Meta:
        model = RequestResource
        fields = ['userName', 'email', 'phone', 'resourceNeed', 'details']