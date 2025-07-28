Déploiement et gestion
========================

Le site OC Lettings est déployé automatiquement grâce à un pipeline CI/CD (intégration et déploiement continu) configuré via **GitHub Actions** et hébergé sur **Render**.

---

CI/CD avec GitHub Actions
--------------------------

L’intégration continue (CI) et le déploiement continu (CD) sont gérés dans le fichier YAML situé à l’emplacement suivant :

``.github/workflows/cicd.yml``

À chaque `push` ou `pull request` sur la branche `master`, GitHub Actions déclenche automatiquement les étapes suivantes :

**Étapes du pipeline :**

1. **Installation des dépendances**
   - Mise à jour de `pip`
   - Installation des dépendances du projet depuis `requirements.txt`

2. **Vérification du style de code**
   - Lancement de `flake8` pour valider la conformité aux conventions PEP8

3. **Tests automatisés et couverture**
   - Exécution des tests avec `pytest`
   - Génération d’un rapport de couverture avec `coverage`
   - Si la couverture descend sous 80 %, le pipeline échoue

4. **Connexion à Docker Hub**
   - Authentification sécurisée via les secrets `DOCKER_USERNAME` et `DOCKER_PASSWORD` dans GitHub

5. **Construction de l’image Docker**
   - Création de l’image avec le tag basé sur le SHA du commit GitHub

6. **Tagging de l’image**
   - L’image est également taguée comme `latest` pour indiquer qu’il s’agit de la dernière version stable

7. **Push de l’image Docker**
   - Envoi des deux images (`latest` et SHA spécifique) sur Docker Hub

8. **Déploiement automatique via Render**
   - Si les changements proviennent de `master`, le pipeline envoie un `POST` vers un **webhook Render** défini dans la variable `RENDER_DEPLOY_HOOK`

---

Accès au site en production
----------------------------

Le site est accessible en ligne à l’adresse suivante :

https://p13-oc-lettings.onrender.com/



Exécution locale avec Docker
-----------------------------

Pour tester l’image Docker localement :

.. code-block:: bash

   # Remplacez <docker-username> et <repository-name> par vos informations Docker Hub
   docker pull <docker-username>/<repository-name>:latest
   docker run -p 8000:8000 <docker-username>/<repository-name>:latest

---

Ce système garantit que chaque changement de code est automatiquement vérifié, packagé, et mis en ligne avec rigueur, assurant un déploiement fluide et professionnel.
