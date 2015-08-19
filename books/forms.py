from django import forms
from django.forms.models import inlineformset_factory
from .models import Author, Book
from bootstrap3_datetime.widgets import DateTimePicker

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('name', )


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('author', 'title')

BookFormSet = inlineformset_factory(Author, Book, extra=0, min_num=1,
    can_delete = False,
    fields = ('title','release_date' ),
    widgets = { 'release_date' : DateTimePicker(options={"format": "YYYY-MM-DD",
                                       "pickTime": False})} )
