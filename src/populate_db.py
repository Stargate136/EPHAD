"""
A simple script to populate the database with 2 CVs
"""
import os
import django
from datetime import date

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from cv.models import (PersonalInformation, Profile, Experience, Education,
                       Skill, Language, Hobby, Project as CVProject, Certification, CV)

from portfolio.models import Project as PortfolioProject

def populate_cv():
    # Informations personnelles
    info1 = PersonalInformation(
        full_name="Jean Dupont",
        address="123 rue Paris",
        phone="+33123456789",
        email="jean.dupont@example.com",
        portfolio_url="http://jeandupont.fr",
        linkedin_url="http://linkedin.com/in/jeandupont",
        github_url="http://github.com/jeandupont",
        profile_picture="profile_pics/jean.jpg"
    )
    info1.save()

    info2 = PersonalInformation(
        full_name="Marie Martin",
        address="456 rue Lyon",
        phone="+33198765432",
        email="marie.martin@example.com",
        portfolio_url="http://mariemartin.fr",
        linkedin_url="http://linkedin.com/in/mariemartin",
        github_url="http://github.com/mariemartin",
        profile_picture="profile_pics/marie.jpg"
    )
    info2.save()

    # Profils
    profile1 = Profile(description="Développeur Web passionné avec plus de 5 ans d'expérience dans la création de sites web dynamiques et d'applications utilisant Python et Django.")
    profile1.save()

    profile2 = Profile(description="Data Scientist enthousiaste avec une expertise en Machine Learning, analyse prédictive, et visualisation de données.")
    profile2.save()

    # Compétences
    skills = [
        Skill(name="Python", skill_type="HARD"),
        Skill(name="Django", skill_type="HARD"),
        Skill(name="React", skill_type="HARD"),
        Skill(name="Machine Learning", skill_type="HARD"),
        Skill(name="SQL", skill_type="HARD"),
        Skill(name="Communication", skill_type="SOFT"),
        Skill(name="Teamwork", skill_type="SOFT"),
        Skill(name="Problem Solving", skill_type="SOFT"),
    ]

    for skill in skills:
        skill.save()

    # Expériences
    exp1 = Experience(
        company="TechCorp",
        position="Développeur Web Senior",
        start_date=date(2018, 1, 1),
        end_date=date(2022, 5, 30),
        responsibilities="Conception et développement de sites web, collaboration avec l'équipe de design, mise en place de solutions back-end avec Django."
    )
    exp1.save()

    exp2 = Experience(
        company="DataSolutions",
        position="Data Scientist",
        start_date=date(2019, 3, 1),
        end_date=date(2023, 4, 30),
        responsibilities="Analyse de grands ensembles de données, création de modèles prédictifs, travail en étroite collaboration avec l'équipe de marketing pour comprendre les tendances des données."
    )
    exp2.save()

    # Éducation
    edu1 = Education(
        institution="Université de Paris",
        degree="Master en Informatique",
        start_date=date(2015, 9, 1),
        end_date=date(2017, 6, 30),
        details="Spécialisation en développement web et bases de données."
    )
    edu1.save()

    edu2 = Education(
        institution="Université de Lyon",
        degree="Master en Data Science",
        start_date=date(2016, 9, 1),
        end_date=date(2018, 6, 30),
        details="Cours sur le Machine Learning, les statistiques avancées, et la programmation Python."
    )
    edu2.save()

    # Langues
    lang1 = Language(name="Français", proficiency="Langue maternelle")
    lang1.save()

    lang2 = Language(name="Anglais", proficiency="Courant")
    lang2.save()

    # Loisirs (Hobbies)
    hobby1 = Hobby(name="Photographie", description="Passionné de photographie de paysage.")
    hobby1.save()

    hobby2 = Hobby(name="Voyages", description="Voyage fréquemment pour découvrir différentes cultures.")
    hobby2.save()

    # Projets
    project1 = CVProject(
        title="E-Shop",
        description="Site e-commerce avec un back-end Django et un front-end React.",
        link="http://eshop.com"
    )
    project1.save()
    project1.skills_used.add(skills[0], skills[1], skills[2])

    project2 = CVProject(
        title="Sales Predictor",
        description="Application prédictive pour anticiper les ventes futures d'un e-commerce.",
        link="http://salespredictor.com"
    )
    project2.save()
    project2.skills_used.add(skills[0], skills[3], skills[4])

    # Certifications
    cert1 = Certification(
        title="Certification Python",
        issuing_organization="Python Institute",
        date_received=date(2019, 5, 15),
        link="http://pythoninstitute.org/cert"
    )
    cert1.save()

    cert2 = Certification(
        title="Certification Data Analysis with Python",
        issuing_organization="Coursera",
        date_received=date(2020, 11, 20),
        link="http://coursera.org/cert"
    )
    cert2.save()

    # CVs
    cv1 = CV(title="Développeur Web", personal_info=info1, profile=profile1)
    cv1.save()
    cv1.experiences.add(exp1)
    cv1.educations.add(edu1)
    cv1.skills.set(skills[:5])
    cv1.languages.set([lang1, lang2])
    cv1.hobbies.set([hobby1, hobby2])
    cv1.projects.add(project1)
    cv1.certifications.add(cert1)

    cv2 = CV(title="Data Scientist", personal_info=info2, profile=profile2)
    cv2.save()
    cv2.experiences.add(exp2)
    cv2.educations.add(edu2)
    cv2.skills.set(skills[2:6])
    cv2.languages.set([lang1, lang2])
    cv2.hobbies.set([hobby2])
    cv2.projects.add(project2)
    cv2.certifications.add(cert2)

    print("'cv' app : 2 CVs added successfully !")


def populate_portfolio():
    # Projet 1
    project1 = PortfolioProject(
        title="E-commerce Platform",
        description="Une plateforme de commerce électronique pour la vente de produits électroniques.",
        details="Développé avec Django, React et Stripe pour les paiements. Comprend une gestion des stocks et une intégration de chat en direct.",
        url="http://example.com/e-commerce",
        github_url="https://github.com/your_username/e-commerce-platform"
    )
    project1.save()

    # Projet 2
    project2 = PortfolioProject(
        title="Blog Platform",
        description="Un CMS de blog personnalisé avec des fonctionnalités de commentaires et d'authentification.",
        details="Créé avec Flask et PostgreSQL. Intégration avec SendGrid pour les notifications par e-mail.",
        url="http://example.com/blog",
        github_url="https://github.com/your_username/blog-platform"
    )
    project2.save()

    # Projet 3
    project3 = PortfolioProject(
        title="Weather App",
        description="Une application météo qui affiche les prévisions à 7 jours en utilisant l'API OpenWeather.",
        details="Construit avec Vue.js et Tailwind CSS. Comprend des graphiques interactifs pour la température et les précipitations.",
        url="http://example.com/weather-app",
        github_url="https://github.com/your_username/weather-app"
    )
    project3.save()

    # Projet 4
    project4 = PortfolioProject(
        title="Réseau Social",
        description="Un réseau social simplifié pour les développeurs.",
        details="Développé avec Node.js, Express et MongoDB. Comprend la messagerie en temps réel et les notifications.",
        url="http://example.com/dev-social",
        github_url="https://github.com/your_username/dev-social"
    )
    project4.save()

    # Projet 5
    project5 = PortfolioProject(
        title="Application de ToDo",
        description="Une application de gestion des tâches avec des rappels.",
        details="Construit avec React et Firebase pour l'authentification et le stockage des données.",
        url="http://example.com/todo-app",
        github_url="https://github.com/your_username/todo-app"
    )
    project5.save()

    # Projet 6
    project6 = PortfolioProject(
        title="Plateforme d'apprentissage",
        description="Une plateforme pour les cours en ligne avec des quiz et des certificats.",
        details="Développé avec Django et React. Intégration avec Stripe pour les paiements.",
        url="http://example.com/learning-platform",
        github_url="https://github.com/your_username/learning-platform"
    )
    project6.save()

    # Projet 7
    project7 = PortfolioProject(
        title="ChatBot",
        description="Un chatbot pour le support client.",
        details="Utilise Python avec la bibliothèque Rasa. Intégration avec les canaux de communication majeurs.",
        url="http://example.com/chatbot",
        github_url="https://github.com/your_username/chatbot"
    )
    project7.save()

    # Projet 8
    project8 = PortfolioProject(
        title="Jeu de plateforme",
        description="Un jeu de plateforme 2D.",
        details="Développé avec Unity et C#. Comprend plusieurs niveaux et une boutique en jeu.",
        url="http://example.com/platform-game",
        github_url="https://github.com/your_username/platform-game"
    )
    project8.save()

    # Projet 9
    project9 = PortfolioProject(
        title="Outil d'analyse de données",
        description="Un outil pour visualiser et analyser des ensembles de données volumineux.",
        details="Utilise Python avec les bibliothèques Pandas et Matplotlib. Interface utilisateur construite avec PyQt.",
        url="http://example.com/data-tool",
        github_url="https://github.com/your_username/data-tool"
    )
    project9.save()

    # Projet 10
    project10 = PortfolioProject(
        title="Agence de voyages",
        description="Un site web pour une agence de voyages avec une recherche et réservation de vols.",
        details="Construit avec PHP et MySQL. Utilise l'API Skyscanner pour les recherches de vols.",
        url="http://example.com/travel-agency",
        github_url="https://github.com/your_username/travel-agency"
    )
    project10.save()

    print("'portfolio' app : 10 projects added successfully !")


def main():
    pass


if __name__ == "main":
    main()
