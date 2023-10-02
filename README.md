# EPHAD

## Applications
### core
- contient toutes les pages statiques de l'application, les fichiers CSS communs a toutes les pages

### contact
- contient le formulaire de contact

## TODO
- Remplir les pages
- Configurer le serveur SMTP
- Configurer l'API de reCaptcha
- Agrandir la police

# Ce dont on a besoin
- logo
- Adresse
- Mail
- Telephone 
- Serveur SMTP
- Clé d'API pour captcha

# A mettre dans un fichier .env a la racine du projet

pour générer la SECRET_KEY :
`python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`
## En local
```
SECRET_KEY=django-insecure-<clé_secrete_générée_avec_la_commande_du_dessus
DEBUG=True
ALLOWED_HOSTS="127.0.0.1
DJANGO_ENVIRONMENT=DEV
```

# Arborescence
## Accueil
- GRED VAS NOUS DONNER LES IMAGES ET LE TEXTE A METTRE
## Contact
- Formulaire de contact OK
## A Propos
- ?
## Prestations
- Court séjour
- Accueil de jour
- Accueil en situation d'urgence
- Séjour permanent
