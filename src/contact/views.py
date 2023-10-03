from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib import messages

from .forms import ContactForm
from config.settings import CONTACT_EMAIL_ADDRESS


class ContactFormView(FormView):
    template_name = "contact/contact_form.html"
    form_class = ContactForm
    success_url = reverse_lazy("contact:form")

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        subject = form.cleaned_data.get("subject")
        message = form.cleaned_data.get("message")
        # TODO : changer l'adresse email avec la vraie
        send_mail(subject, message, email, CONTACT_EMAIL_ADDRESS, fail_silently=False)
        messages.success(self.request, "Votre message a été envoyé avec succès!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Il y a eu une erreur avec votre soumission. Veuillez vérifier vos informations.")
        return super().form_invalid(form)
