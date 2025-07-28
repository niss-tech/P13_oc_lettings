Installation du projet
=======================


Cloner le dépôt
~~~~~~~~~~~~~~~

.. code:: bash

    cd /chemin/où/placer/le/projet
    git clone https://github.com/niss-tech/P13_oc_lettings.git

Créer l’environnement virtuel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

    cd P13_oc_lettings
    python -m venv venv

Activer l’environnement virtuel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

    # Linux/macOS
    source venv/bin/activate

    # Windows
    .\venv\Scripts\activate

Installer les dépendances
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

    pip install -r requirements.txt

Définir les variables d’environnement nécessaires
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

    # Optionnel si vous utilisez un fichier .env
    export SECRET_KEY='votre_clé_django'
    export SENTRY_DSN='dsn de sentry'


Linting
~~~~~~~

.. code:: bash

    flake8

Le fichier `setup.cfg` contient la configuration flake8.

---

Tests unitaires
~~~~~~~~~~~~~~~

.. code:: bash

    pytest

Pour mesurer la couverture :

.. code:: bash

    pytest --cov

Les tests sont organisés par application (`lettings`, `profiles`, `oc_lettings_site`), et couvrent les modèles, vues, urls et gestion des erreurs.

---

Interface d’administration
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Allez à l’adresse : ``http://localhost:8000/admin``  
Identifiants par défaut :

- Nom d’utilisateur : `admin`
- Mot de passe : `Abc1234!`

