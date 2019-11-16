from django import forms  
from django.forms import formset_factory

from p_library.models import Author, Book, Mate

  
class AuthorForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput)   
    class Meta:  
        model = Author  
        fields = '__all__'

class BookForm(forms.ModelForm):  
    class Meta:  
        model = Book  
        fields = '__all__'

