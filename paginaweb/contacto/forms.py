from django import forms

class formulariocontacto(forms.Form):
    nombre= forms.CharField(label='nombre',max_length=50, required=True)
    email= forms.EmailField(label='email',max_length=50, required=True)
    mensaje=forms.CharField(label='mensaje', widget=forms.Textarea)