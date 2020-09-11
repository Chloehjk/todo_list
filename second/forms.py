from django import forms
from .models import Favorite, Todo


class FavoriteModelForm(forms.ModelForm):

    class Meta:
        model = Favorite
        fields = '__all__'
        labels = {
            'name': '명칭', 'url':'URL', 'memo':'메모', 'group':'그룹'
        }



class TodoModelForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ['name', 'status', 'end_date', 'group']
        labels = {
            'name': '명칭', 'status':'상태', 'end_date':'종료일', 'group':'그룹'
        }