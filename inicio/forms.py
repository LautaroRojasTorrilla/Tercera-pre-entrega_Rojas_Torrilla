from django import forms

#form para remera, utilizo un placeholder
class CreacionRemeraFormulario(forms.Form):
    modelo = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Manga Corta, Manga Larga'}))
    talle = forms.CharField(max_length=5, widget=forms.TextInput(attrs={'placeholder': 's, m, l, xl, xxl'}))
    disenio = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'One Piece, Pokemon, etc'}))
    origen = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'China, Japon, etc'}))

#form para realizar busqueda del objeto remera, utilizando el diseño
class BuscarRemera(forms.Form):
    # permite que el campo este vacío
    disenio = forms.CharField(max_length=20, required=False)