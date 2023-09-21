
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib import messages
from .forms import ContactForm


class ContactFormView(FormView):
    template_name = "contact/form.html"
    form_class = ContactForm
    success_url = reverse_lazy("contact:form")  # Mettez l'URL de la page de remerciement ou de confirmation ici.

    def form_valid(self, form):
        # Si le formulaire est valide, sauvegardez l'objet sans le commettre en base de données.
        contact_message = form.save(commit=False)
        # Traitement supplémentaire si nécessaire (comme l'envoi d'un e-mail)
        contact_message.save()  # Sauvegardez l'objet en base de données.
        messages.success(self.request, "Votre message a été envoyé avec succès!")
        return super().form_valid(form)

    def form_invalid(self, form):
        # En cas d'erreur, affichez un message d'erreur à l'utilisateur.
        messages.error(self.request, "Il y a eu une erreur avec votre soumission. Veuillez vérifier vos informations.")
        return super().form_invalid(form)