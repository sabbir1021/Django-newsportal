from django import forms 
from .models import Comment , Article

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'name',
            'post_comment'
        ]
    
class CreateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'title',
            'picture',
            'body',
            'category',
            'lead',
            'lead2',
            'lead3'
        ]

