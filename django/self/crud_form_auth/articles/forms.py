from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        # fields = '__all__'
        exclude = ('ssafyclass', )  # tuple 값으로 알려줘야한다.
    
    # title = forms.CharField(max_length=10)
    # content = forms.CharField(widget=forms.Textarea)
    
    # CLASS_A = 's1'
    # CLASS_B = 's2'
    # CLASS_C = 's3'
    # CLASS_D = 's4'
    # CLASS_E = 's5'
    # CLASS_F = 's6'
    
    # CLASS_CHOICES = [
    #     (CLASS_A, '🚫'),
    #     (CLASS_B, '🚫'),
    #     (CLASS_C, '🚫'),
    #     (CLASS_D, '🚫'),
    #     (CLASS_E, '💌'),
    #     (CLASS_F, '🚫'),
    # ]

    # ssafyclass = forms.ChoiceField(choices=CLASS_CHOICES)