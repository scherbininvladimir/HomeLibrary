from django import forms  
from p_library.models import Author  
  
class AuthorForm(forms.ModelForm):  
    class Meta:  
        model = Author  
        fields = '__all__'