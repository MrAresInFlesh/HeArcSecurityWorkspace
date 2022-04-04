# HeArcSecurityWorkspace

Workspace containing the work about the security course.

La plupart des projets où exercices sont implémentés en `python`.
C'est pourquoi des environnements virtuels sont mis en place.

Pour configurer votre environnement virtuel, ouvrez une console `bash` à la racine du projet ou de l'exercice, et exécuter:

```bash=
# Windows
python -m venv .venv

# Linux
python3 -m venv .venv
```

Une fois votre `.venv` créer, activez le:

```bash=
# Windows
source .venv/Scripts/activate
# Or
. .venv/Scripts/activate
```

Une fichier nommé `requirements.txt` comporte tous les packages utilisés lors de l'implémentation du programme.

Lancez la commande:

```bash=
# Windows
pip install -r requirements.txt

# Linux
pip3 install -r requirements.txt
```

Pour installer les packages dans votre environnement virtuel. Ainsi il vous est possible d'utiliser le programme sans devoir installer directement sur votre machine les packages nécessaire à son fonctionnement.

## Arborescence du dossier

```typescript=
C:\DEV\CODE\SECURITY\HEARCSECURITYWORKSPACE
|   .gitignore
|   README.md
|
+---exercice4
|   |   .gitignore
|   |   README.md
|   |   requirements.txt
|   |   tree_hierarchy.txt
|   |
|   +---.venv
|   |
|   +---challenge_response_authentication
|   |   |   client.py
|   |   |   cryptool.py
|   |   |   main.py
|   |   |   server.py
|   |   |
|   |   \---__pycache__
|   |           client.cpython-39.pyc
|   |           cryptool.cpython-39.pyc
|   |           server.cpython-39.pyc
|   |
|   \---__pycache__
|           client.cpython-39.pyc
|           cryptool.cpython-39.pyc
|           server.cpython-39.pyc
|
+---presentation
|   |   Presentation_ModeleSecuriteAndroid.pptx
|   |   presentation_model_securite_technique_android.pdf
|   |
|   \---documentation
|       |   arc-logo.png
|       |   doc.md
|       |   doc.pdf
|       |   doc.synctex.gz
|       |   doc.tex
|       |   model.png
|       |   verified_boot.png
|       |
|       \---backgrounds
|               background_frontpage.png
|               background_page.png
|
\---projet
```
