# 4. Exercice à rendre: challenge-response

Dans le langage de votre choix et par groupe de deux, implémentez un client et un serveur d'authentification basé sur un challenge-response.

Indications (répondre aux questions en commentaire dans le code)

* quel hachage cryptographique utilisez-vous et pourquoi ?
* quelles précautions pour le générateur aléatoire ?
* quelles précautions pour la construction garantissant l'unicité du nonce ?
* quelles précautions pour la durée de validité du nonce ?
* la partie réseau n'est pas nécessaire: des appels de fonctions simples sont autorisés.

Voir <https://en.wikipedia.org/wiki/Challenge%E2%80%93response_authentication>

Tenir compte des recommandations [hash, crypto, PRNG](02_Authentification/autres/nma-hash-crypt-PRNG-recommandations.pdf).

PS: nous avons déjà vu un tel protocole challenge-response dans le CHAP
des slides ainsi que pour l'authentification d'un téléphone IP à
Asterisk en R+A 2e année.

Délai: fin de la semaine des présentations.
