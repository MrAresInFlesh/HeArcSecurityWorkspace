
# Challenge-response authentication protocole

## Consigne

> Voir <https://en.wikipedia.org/wiki/Challenge%E2%80%93response_authentication>
>
> Tenir compte des recommandations [hash, crypto, PRNG](02_Authentification/autres/nma-hash-crypt-PRNG-recommandations.pdf).
>
> PS: nous avons déjà vu un tel protocole challenge-response dans le CHAP des slides ainsi que pour l'authentification d'un téléphone IP à Asterisk en R+A 2e année.

**Délai: fin de la semaine des présentations.**

### 4. Exercice à rendre: challenge-response

Dans le langage de votre choix et par groupe de deux, implémentez un client et un serveur d'authentification basé sur un challenge-response.

Indications (répondre aux questions en commentaire dans le code)

### Questions

* quel hachage cryptographique utilisez-vous et pourquoi?
  * J'utilise MD5(pour Message Digest 5). C'est une fonction de hachage cryptographique qui permet d'obtenir l'empreinte numérique d'une variable, par exemple une chaîne de caractère. Il est aujourd'hui dépassé et absolument impropre à toute utilisation en cryptographie ou en sécurité. Le seul intérêt ici est qu'il convient bien à l'exercice d'implémentation du challenge-response protocole. Et voilà, c'est plus simple d'utiliser les fonctions directement proposées par hashlib.
* quelles précautions pour le générateur aléatoire?
* quelles précautions pour la construction garantissant l'unicité du nonce?
* quelles précautions pour la durée de validité du nonce?
  * Le nonce est renvoyé à chaque.
* la partie réseau n'est pas nécessaire: des appels de fonctions simples sont autorisés.

## Rendu

---

**Titre:** Exercice à rendre: challenge-response

**Etudiant:** Simon Meier

**Professeur:** Marc Schaefer

---

### Arborescence du projet

```typescript
exercice4
│   README.md
│   requirements.txt
│
├───.venv
├───__pycach__
└───challenge_response_authentication
       client.py
       cryptool.py
       main.py
       server.py
```

### Protocole choisi: CHAP

Le protocole CHAP (Challenge Handshake Authentication Protocol) est un protocole d'authentification point à point (PPP) développé par l'IETF (Internet Engineering Task Force). Il est utilisé au démarrage initial du lien. En outre, il effectue des vérifications périodiques pour vérifier si le routeur communique toujours avec le même hôte.

* CHAP:
  * utilise le protocole d'établissement de liaison à 3 voies (pas comme TCP). Tout d'abord, l'authentificateur envoie un paquet de défi au pair, puis le pair répond avec une valeur en utilisant sa fonction de hachage à sens unique. L'authentificateur fait alors correspondre la valeur reçue avec sa propre valeur de hachage calculée. Si les valeurs correspondent, l'authentification est confirmée, sinon la connexion sera interrompue.
  * utilise une fonction de hachage unidirectionnelle appelée MD5.
  * s'authentifie également périodiquement pour vérifier si la communication a lieu avec le même appareil ou non.
  * offre plus de sécurité que PAP (Password Authentication Procedure) car la valeur utilisée (découverte par la fonction de hachage) est modifiée de manière variable.
  * nécessite de connaître le texte en clair du secret car il n'est jamais envoyé sur le réseau.
