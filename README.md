# EPHAD

## A savoir
- J'ai supprimé les fichiers models.py, admin.py et les dossiers migrations/ parce qu'on n'utilise pas de base de donnée
- Il faut créer un environnement virtuel et installer les requirements
- Il faut créer un fichier .env a la racine du projet (au même niveau que requirements.txt et README.md)

### A mettre dans le fichier .env
pour générer la SECRET_KEY :
`python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`
```
SECRET_KEY=django-insecure-<clé_secrete_générée_avec_la_commande_du_dessus
DEBUG=True
ALLOWED_HOSTS="127.0.0.1
DJANGO_ENVIRONMENT=<DEV_ou_PROD>

EMAIL_HOST=
EMAIL_PORT=
EMAIL_USE_TLS=
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=

CONTACT_EMAIL_ADDRESS=<adresse_mail_de_la_personne_qui_doit_recevoir_les_mails_de_contact>
```


## Arborescence
- requirements.txt : Contient les librairies (à installer avec pip)
- README.md : Contient les explications
- .gitignore : Contient les fichiers a ignorer par Git
- .env : Contient les variables d'environnement
- src/ : Contient le code
  - config/ : Contient les fichiers de configuration
    - settings.py : Contient les paramètres de l'application
    - urls.py : Contient les include des fichiers urls.py des applications
    - \__init\__.py
    - wsgi.py
    - asgi.py
  - core/ : Application qui contient ce qui est commun a toutes les pages
    - static/ : Contient les fichiers statiques (CSS et logo)
      - core/ : Sous-dossier pour éviter les conflits
        - css/
          - base/ : Contient tous les fichiers css qui sont chargés avec le template base.html
            - reset.css : Réinitialise les styles
            - variables.css : Contient les variables (palette de couleurs, police, espacements)
            - base.css : Contient les styles de base des éléments
            - layout.css : Contient l'organisation de la page
            - navbar.css : Contient le style de la navbar
            - footer.css : Contient le style du footer
          - widgets/ : Contient les fichiers css des widgets personnalisés
            - buttons.css : Contient le style des boutons
            - cards.css : Contient le style des cartes 
            - forms.css : contient le style des formulaires
        - img/ : Contient les images statiques (logo, background)
          - background.png
          - logo.png
    - templates/ : Contient les templates
      - core/ : Sous-dossier pour éviter les conflits
        - base/ : Contient les parties du template de base (header et footer)
          - footer.html : Contient le footer
          - header.html : Contient le header
        - about.html : Page à propos
        - base.html : Template de base
        - home.html : Page d'accueil
        - personal_data_and_cookies.html : Données personnelles et cookies
        - under_construction.html : Page en cours de développement
    - urls.py : Contient les urls
    - views.py : Contient les vues
    - \__init\__.py
    - apps.py
  - contact/ : Application contenant la page de contact et l'envoie de l'email
    - static/ : Contient les fichiers statiques (CSS)
      - contact/ : Sous-dossier pour éviter les conflits
        - css/ : Contient les styles
          - contact_form.css : Contient les styles du template contact_form.html
    - templates/ : Contient les templates
      - contact/ : Sous-dossier pour éviter les conflits
        - contact_form.html : Contient la page de contact
    - urls.py : Contient les urls
    - forms.py : Contient le formulaire de contact
    - views.py : Contient la vue de contact et la logique de l'envoi d'email
    - \__init\__.py
    - apps.py
  - services/ : Contient les pages des prestations
    - templates/ : Contient les templates
      - services/ : Sous-dossier pour éviter les conflits
        - day_care.html : Contient le template pour l'accueil de jour
        - emergency_reception.html : Contient le template pour l'accueil d'urgence
        - index.html : Contient le template de la page d'accueil des prestations
        - permanent_stay.html : Contient le template de la page de séjour permanent
        - short_stay.html : Contient le template de la page de court séjour
    - urls.py : Contient les urls
    - views.py : Contient les vues
    - \__init\__.py
    - apps.py



## TODO
- Remplir les pages
- Configurer l'API de reCaptcha
- Ajouter burger sur la navbar
