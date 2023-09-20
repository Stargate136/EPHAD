from django.contrib import admin

from .models import (
    PersonalInformation, Profile, Experience, Education, Skill, Language,
    Hobby, Project, Certification, CV
)


@admin.register(PersonalInformation)
class PersonalInformationAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'phone']
    search_fields = ['full_name', 'email']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['description']


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['company', 'position', 'start_date', 'end_date']
    search_fields = ['company', 'position']


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['institution', 'degree', 'start_date', 'end_date']
    search_fields = ['institution', 'degree']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'skill_type']
    list_filter = ['skill_type']


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name', 'proficiency']
    list_filter = ['proficiency']


@admin.register(Hobby)
class HobbyAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'link']
    search_fields = ['title']
    filter_horizontal = ['skills_used']


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ['title', 'issuing_organization', 'date_received']
    search_fields = ['title', 'issuing_organization']


@admin.register(CV)
class CVAdmin(admin.ModelAdmin):
    list_display = ['personal_info', 'profile']
    filter_horizontal = [
        'experiences', 'educations', 'skills', 'languages', 'hobbies',
        'projects', 'certifications'
    ]
