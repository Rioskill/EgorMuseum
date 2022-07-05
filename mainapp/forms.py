from django import forms
from .models import LastQuestImage


class LastQuestImageForm(forms.ModelForm):
    class Meta:
        model = LastQuestImage
        fields = ('image',)
