from django.db import models


class Section(models.Model):
    PAGES = [("HOME", "Accueil"),
             ("ABOUT", "A propos")]
    page = models.CharField(max_length=100, choices=PAGES)
    title = models.CharField(max_length=100)
    content = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)
    display_order = models.PositiveIntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.display_order is None:
            # Assign the current maximum value of display_order + 1
            max_order = Section.objects.all().aggregate(models.Max('display_order'))['display_order__max'] or 0
            self.display_order = max_order + 1

        # If the instance already has an ID, it's an update
        if self.id:
            # Get the old display order
            old_order = Section.objects.get(id=self.id).display_order
            # If the display order changed
            if old_order != self.display_order:
                # Update the other Section objects
                if old_order < self.display_order:
                    # If the display order increased, shift the Sections between the old order and the new order
                    Section.objects.filter(display_order__lte=self.display_order, display_order__gt=old_order).update(display_order=models.F('display_order') - 1)
                else:
                    # If the display order decreased, shift the Sections between the new order and the old order
                    Section.objects.filter(display_order__gte=self.display_order, display_order__lt=old_order).update(display_order=models.F('display_order') + 1)
        else:  # If it's a new instance
            # Shift all Sections with display_order >= the current display_order
            Section.objects.filter(display_order__gte=self.display_order).update(display_order=models.F('display_order') + 1)
