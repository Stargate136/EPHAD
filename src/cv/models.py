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
    personal_info = models.OneToOneField(PersonalInformation, on_delete=models.CASCADE)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    experiences = models.ManyToManyField(Experience)
    educations = models.ManyToManyField(Education)
    skills = models.ManyToManyField(Skill)
    languages = models.ManyToManyField(Language)
    hobbies = models.ManyToManyField(Hobby)
    projects = models.ManyToManyField(Project)
    certifications = models.ManyToManyField(Certification)
