from django.forms import ModelForm, TextInput, EmailInput
from django.forms.utils import ErrorList

from .models import Question


class ParagraphErrorList(ErrorList):
    def __str__(self):
        return self.as_divs()

    def as_divs(self):
        if not self: return ''
        return '<div class="errorlist">%s</div>' % ''.join(['<p class="small error">%s</p>' % e for e in self])


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ["content", "mail"]
        widget = {
            'content': TextInput(attrs={'class': 'form-control'}),
            'mail': EmailInput(attrs={'class': 'form-control'})
        }
