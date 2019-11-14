from django.forms import ModelForm
from .models import Serial


class SerialForm(ModelForm):
    class Meta:
        model = Serial
        fields = ('title', 'description', 'premiere_date')
