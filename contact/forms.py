from django import forms
from django.core.exceptions import ValidationError
from . import models

class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'classe-a classe-b',
                'placeholder': 'Aqui veio do init',
            }
        ),
        label='Primeiro Nome',
        help_text='Texto de ajuda para seu usuário'
    )
    
    # qualquer = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             'class':'classe-a classe-b',
    #             'placeholder': 'Aqui veio do init',
    #         }
    #     ),
    #     help_text='Texto de ajuda para seu usuário',
    # )


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # atualizando o widget
        # self.fields['first_name'].widget.attrs.update({
        #     'class':'classe-a classe-b',
        #     'placeholder': 'Aqui veio do init',
        # })

    class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone',
        )
        # Criando um novo widget pro campo
        # widgets = {
        #     'first_name':forms.TextInput(
        #         attrs={
        #            
        #         }
        #     )
        # }

    def clean(self):
        # cleaned_data = self.cleaned_data

        self.add_error(
            None,
            ValidationError(
                'Mensagem de erro',
                code='invalid'
            )
        )

        self.add_error(
            None,
            ValidationError(
                'Mensagem de erro 2',
                code='invalid'
            )
        )
        
        return super().clean()