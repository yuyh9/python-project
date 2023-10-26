from django.forms import ModelForm, Textarea
from app.models import Todo


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'todo_detail', 'status', 'priority']
        widgets = {
            'todo_detail': Textarea(attrs={'rows': 3, 'cols': 38}),
        }