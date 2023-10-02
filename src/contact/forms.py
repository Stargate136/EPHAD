from django import forms


class ContactForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.label_suffix = ""

    class Meta:
        fields = ['email', 'subject', 'message']

    # Personnalisation éventuelle des widgets (par exemple, pour ajouter des placeholders)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Votre email'}),
                             label="E-mail")
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Sujet'}),
                              label="Sujet")
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Votre message',
                                                           'rows': '5'}))
