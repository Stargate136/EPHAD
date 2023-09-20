from django.db import models


# Create your models here.
class PersonalInformation(models.Model):
    full_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    portfolio_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to="profile_pics/", blank=True, null=True)


class Profile(models.Model):
    description = models.TextField()


class Experience(models.Model):
    company = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    responsibilities = models.TextField()


class Education(models.Model):
    institution = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    details = models.TextField(blank=True, null=True)


class Skill(models.Model):
    SKILL_TYPES = [
        ("HARD", "Hard skill"),
        ("SOFT", "Soft skill")
    ]
    name = models.CharField(max_length=255)
    skill_type = models.CharField(max_length=5, choices=SKILL_TYPES)


class Language(models.Model):
    name = models.CharField(max_length=255)
    proficiency = models.CharField(max_length=255)  # Example values: Fluent, Intermediate, Beginner


class Hobby(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    link = models.URLField(blank=True, null=True)
    skills_used = models.ManyToManyField(Skill, related_name="projects")


class Certification(models.Model):
    title = models.CharField(max_length=255)
    issuing_organization = models.CharField(max_length=255)
    date_received = models.DateField()
    link = models.URLField(blank=True, null=True)


class CV(models.Model):
    title = models.CharField(max_length=255)
    display_order = models.PositiveIntegerField(null=True, blank=True)

    personal_info = models.ForeignKey(PersonalInformation, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    experiences = models.ManyToManyField(Experience)
    educations = models.ManyToManyField(Education)
    skills = models.ManyToManyField(Skill)
    languages = models.ManyToManyField(Language)
    hobbies = models.ManyToManyField(Hobby)
    projects = models.ManyToManyField(Project)
    certifications = models.ManyToManyField(Certification)

    def save(self, *args, **kwargs):
        # If the instance already has an ID, it's an update
        if self.id:
            # Get the old display order
            old_order = CV.objects.get(id=self.id).display_order
            # If the display order changed
            if old_order != self.display_order:
                # Update the other CV objects
                if old_order < self.display_order:
                    # If the display order increased, shift the CVs between the old order and the new order
                    CV.objects.filter(display_order__lte=self.display_order, display_order__gt=old_order).update(display_order=models.F('display_order') - 1)
                else:
                    # If the display order decreased, shift the CVs between the new order and the old order
                    CV.objects.filter(display_order__gte=self.display_order, display_order__lt=old_order).update(display_order=models.F('display_order') + 1)
        else:  # If it's a new instance
            # Shift all CVs with display_order >= the current display_order
            CV.objects.filter(display_order__gte=self.display_order).update(display_order=models.F('display_order') + 1)

        super(CV, self).save(*args, **kwargs)
