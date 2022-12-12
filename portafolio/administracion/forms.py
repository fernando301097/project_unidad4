from django import forms


class ProyectoForm(forms.Form):
    foto = forms.ImageField()
    titulo = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class": "form-control mb-3"}))
    descripcion = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class": "form-control mb-3"}))
    tags = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class": "form-control mb-3"}))
    url_github = forms.URLField(initial='http://', widget=forms.TextInput(attrs={"class": "form-control mb-3"}))
