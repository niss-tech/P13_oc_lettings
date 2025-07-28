Journalisation et suivi des erreurs avec Sentry
===============================================

Afin de mieux surveiller l'application et réagir rapidement en cas de problème, un système de journalisation (`logging`) a été mis en place, couplé à l'outil de suivi des erreurs **Sentry**.

Fonctionnement du logging
-------------------------

Le module `logging` de Python est utilisé pour enregistrer les événements importants dans le projet.

- Les actions normales (comme l’affichage des vues) sont enregistrées au niveau `INFO`.
- Les erreurs critiques (comme des problèmes de récupération de données) sont enregistrées au niveau `ERROR`.

Tous les logs sont affichés dans la console lorsque l’application tourne en local ou en production.

Pourquoi intégrer Sentry ?
--------------------------

Sentry est un service qui permet de suivre les erreurs de manière centralisée, en particulier en production. Il offre :

- Une visualisation claire des erreurs avec traces complètes
- Des notifications en temps réel (mails, Slack, etc.)
- Une aide précieuse pour corriger rapidement les bugs

Sentry est activé uniquement lorsque `DEBUG = False`, pour éviter d’envoyer des erreurs pendant le développement.

Configuration technique
-----------------------

Dans `settings.py`, Sentry est initialisé via la variable d’environnement `SENTRY_DSN`, définie dans le fichier `.env` :

.. code-block:: bash

   SENTRY_DSN='https://<clé>@o123456.ingest.sentry.io/123456'

Un `handler` spécial est configuré pour envoyer à Sentry les logs de niveau `ERROR` et plus.

Test manuel
-----------

Pour vérifier que Sentry est bien actif, il suffit d’ajouter une ligne de code dans une vue :

.. code-block:: python

   import logging
   logger = logging.getLogger(__name__)
   logger.error("Erreur test envoyée à Sentry")
