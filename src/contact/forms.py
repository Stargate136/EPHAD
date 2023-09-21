from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.label_suffix = ""

    class Meta:
        model = ContactMessage
        fields = ['email', 'subject', 'message']

    # Personnalisation éventuelle des widgets (par exemple, pour ajouter des placeholders)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control',
                                                            'placeholder': 'Votre email'}),
                             label="E-mail")
    subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                            'placeholder': 'Sujet'}),
                              label="Sujet")
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',
                                                           'placeholder': 'Votre message',
                                                           'rows': '5'}),)
