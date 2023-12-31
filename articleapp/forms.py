from django.forms import ModelForm
from articleapp.models import Article
from projectapp.models import Project
from artistapp.models import Artist
from django import forms


class ArticleCreationForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable text-start','style':'height:auto'}))
    
    project = forms.ModelChoiceField(queryset=Project.objects.all(),required=False)
    artist = forms.ModelChoiceField(queryset=Artist.objects.all(),required=False)
    class Meta:
        model = Article
        fields = ['title', 'image', 'project','artist','content']