from django.db import models
from django.utils.text import slugify


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(help_text="Brève description du projet.")
    details = models.TextField(blank=True, null=True, help_text="Informations détaillées sur le projet.")
    image = models.ImageField(upload_to="portfolio/images/")
    url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
