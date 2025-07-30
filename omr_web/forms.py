# Esse formulário renderiza um campo para o usuário enviar uma imagem via formulário POST.

from django import forms

class UploadImageForm(forms.Form):
    image = forms.ImageField(label='Selecione a folha de respostas')
