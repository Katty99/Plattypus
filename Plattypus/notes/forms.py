from django import forms

from Plattypus.notes.models import Notes


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = '__all__'
        exclude = ['sender']
