from django import forms
from p_library.models import Author, Book, Publisher, Friend

class AuthorForm(forms.ModelForm):
    full_name = forms.CharField(
        label='Имя автора',
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Введите имя автора'
            }
        )
    )
    birth_year = forms.CharField(
        label='Дата рождения автора',
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Введите дату рождения автора'
            }
        )
    )
    country = forms.CharField(
        label='Страна происхождения',
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Введите страну'
            }
        )
    )
    class Meta:
        model = Author
        fields = '__all__'

class BookForm(forms.ModelForm):
    ISBN = forms.CharField(
        label='ISBN',
        widget=forms.TextInput(
            attrs={
                'required': True,
                'type':'number',
                'class': 'form-control',
                'placeholder': 'Введите ISBN = 13 чисел'
            }
        )
    )
    title = forms.CharField(
        label='Название книги',
        widget=forms.TextInput(
            attrs={
                'required': True,
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Введите название книги'
            }
        )
    )
    description = forms.CharField(
        label='Описание книги',
        widget=forms.Textarea(
            attrs={
                'required': True,
                'class': 'form-control',
                'rows': '3',
                'placeholder': 'Введите описание книги'
            }
        )
    )
    year_release = forms.CharField(
        label='Дата публикации',
        widget=forms.TextInput(
            attrs={
                'required': True,
                'type': 'number',
                'class': 'form-control',
                'placeholder': 'Введите дату создания книги'
            }
        )
    )
    author = forms.ModelChoiceField(
        queryset=Author.objects.all(),
        label='Автор книги',
        widget=forms.Select(
            attrs={
                'required': True,
                'class': 'form-control'
            }
        )
    )
    publisher = forms.ModelChoiceField(
        queryset=Publisher.objects.all(),
        label='Издательство',
        widget=forms.Select(
            attrs={
                'required': True,
                'class': 'form-control'
            }
        )
    )
    copy_count = forms.CharField(
        label= 'Общее количество книг',
        widget= forms.TextInput(
            attrs={
                'required': True,
                'type': 'number',
                'class': 'form-control',
                'placeholder': 'Введите общее количество книг'
            }
        )
    )
    price = forms.CharField(
        label= 'Цена книги',
        widget= forms.TextInput(
            attrs={
                'required': True,
                'type': 'number',
                'class': 'form-control',
                'placeholder': 'Введите стоимость книги'
            }
        )
    )
    class Meta:
        model = Book
        fields = ('ISBN', 'title', 'description', 'year_release', 'author', 'price', 'copy_count', 'publisher')

class PublisherForm(forms.ModelForm):
    name = forms.CharField(
        label='Издательство',
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Введите название издательства'
            }
        )
    )
    class Meta:
        model = Publisher
        fields = '__all__'

class FriendForm(forms.ModelForm):
    full_name = forms.CharField(
        label='Имя друга',
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Введите имя друга'
            }
        )
    )
    class Meta:
        model = Friend
        fields = '__all__'