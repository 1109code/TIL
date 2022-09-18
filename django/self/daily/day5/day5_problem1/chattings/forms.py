from django import forms
from .models import Chat

class ChatForm(forms.ModelForm):
    user = forms.CharField(
        label='작성자',
        widget=forms.TextInput(
            attrs={
                'class': 'my-name from-control',
                'placeholder': 'Enter the name',
                'maxlength': 10,
            }
        )
    )
    
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content from-control',
                'placeholder': 'Enter the content',
                'rows': 5,
                'cols': 50,
            }
        )
    )

    class Meta:
        model = Chat
        fields = '__all__'