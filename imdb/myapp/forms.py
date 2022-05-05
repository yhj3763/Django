from django import forms
from myapp.models import Authors
from myapp.models import Customers
from myapp.models import Publishers
from myapp.models import Titles
from myapp.models import Titleauthors
from myapp.models import Subjects

class AuthorsForm(forms.ModelForm):
    class Meta:
        model= Authors
        fields="__all__"

class CustomersForm(forms.ModelForm):
    class Meta:
        model= Customers
        fields="__all__"

class PublishersForm(forms.ModelForm):
    class Meta:
        model= Publishers
        fields="__all__"

class TitlesForm(forms.ModelForm):
    class Meta:
        model= Titles
        fields="__all__"

class TitleauthorsForm(forms.ModelForm):
    class Meta:
        model= Titleauthors
        fields="__all__"

class SubjectsForm(forms.ModelForm):
    class Meta:
        model= Subjects
        fields="__all__"