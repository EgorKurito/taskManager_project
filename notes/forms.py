from django import forms
from . import models


class NoteForm(forms.ModelForm):
    class Meta:
        model = models.Note
        fields = [
            'title',
            'content',
            'favourite',
            'category',
        ]
