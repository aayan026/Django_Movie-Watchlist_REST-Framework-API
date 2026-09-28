from django import forms

from .models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'genre', 'release_year', 'status', 'rating']

        labels = {
            'title': 'Filmin adı',
            'genre': 'Janr',
            'release_year': 'Buraxılış ili',
            'status': 'Status',
            'rating': 'Qiymətləndirmə (1-10)',
        }

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control mb-3',
                'placeholder': "Filmin adını daxil edin",
            }),
            'genre': forms.TextInput(attrs={
                'class': 'form-control mb-3',
                'placeholder': "Məsələn: Drama, Komediya, Fantastika",
            }),
            'release_year': forms.NumberInput(attrs={
                'class': 'form-control mb-3',
                'placeholder': "Məsələn: 2024",
            }),
            'status': forms.Select(attrs={
                'class': 'form-select mb-3',
            }),
            'rating': forms.NumberInput(attrs={
                'class': 'form-control mb-3',
                'min': 1,
                'max': 10,
                'placeholder': "1-dən 10-a qədər",
            }),
        }

    def clean_release_year(self):
        release_year = self.cleaned_data['release_year']
        if release_year < 1888 or release_year > 2100:
            raise forms.ValidationError("Buraxılış ili düzgün deyil")
        return release_year
