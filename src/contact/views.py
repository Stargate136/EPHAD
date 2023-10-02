from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib import messages
from .forms import ContactForm


class ContactFormView(FormView):
    template_name = "contact/contact_form.html"
    form_class = ContactForm
    success_url = reverse_lazy("contact:form")  # Mettez l'URL de la page de remerciement ou de confirmation ici.

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        subject = form.cleaned_data.get("subject")
        message = form.cleaned_data.get("message")
        send_mail(subject, message, email, ["test@gmail.com"])
        messages.success(self.request, "Votre message a été envoyé avec succès!")
        return super().form_valid(form)

    def form_invalid(self, form):
        # En cas d'erreur, affichez un message d'erreur à l'utilisateur.
        messages.error(self.request, "Il y a eu une erreur avec votre soumission. Veuillez vérifier vos informations.")
        return super().form_invalid(form)