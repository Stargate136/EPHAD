from django.db import models


# Create your models here.
class ContactMessage(models.Model):
    email = models.EmailField(verbose_name="E-mail")
    subject = models.CharField(max_length=100, verbose_name="Sujet")
    message = models.TextField(verbose_name="Message")

    is_processed = models.BooleanField(default=False)
    processed_at = models.DateTimeField(null=True, blank=True)

    sent_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.pk:
            model_in_db = ContactMessage.objects.get(pk=self.pk)
            if model_in_db.is_processed != self.is_processed:
                if self.is_processed is True:
                    self.processed_at = datetime.now()
                else:
                    self.processed_at = None
        super().save(*args, **kwargs)
