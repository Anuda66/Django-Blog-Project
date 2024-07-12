from django import forms
from .models import postModel, comments

class postModelForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows':4}))
    class Meta:
        model = postModel
        fields = ('title', 'content')

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = postModel
        fields = ('title', 'content')
        
