# Snake Game en Python (Pygame)

## Présentation

Ce projet est une version du jeu **Snake** développée en **Python** avec la bibliothèque **Pygame**.
Il a été réalisé dans le cadre d’un stage d’une semaine en **2022** au sein de l’association **Science Ouverte**.

L’objectif du projet était de découvrir la programmation en Python à travers un jeu simple, en travaillant sur :

* la gestion d’une boucle de jeu,
* les déplacements en temps réel,
* les collisions,
* et la logique d’un jeu vidéo.

## Certification

J’ai réalisé ce projet dans le cadre d’un stage à l’association **Science Ouverte** en 2022.

Voir la certification : 

https://github.com/mariammm0/GAME_SNAKE/blob/main/Attestation%20de%20participation%20-%20Mariam%20Abd%20El%20Moneim.pdf

## Principe du jeu

Le joueur contrôle un serpent qui se déplace sur une grille.
Le but est de manger des fruits pour grandir, tout en évitant :

* de sortir de la zone de jeu,
* de se rentrer dedans.

Chaque fruit mangé augmente la taille du serpent.


## Fonctionnalités

* Déplacement du serpent avec les flèches du clavier
* Génération aléatoire des fruits
* Croissance du serpent après collision avec un fruit
* Détection des collisions :

  * avec les bords de l’écran
  * avec le corps du serpent
* Boucle de jeu fluide avec `pygame.time.set_timer`


## Structure du code

Le projet est organisé en plusieurs classes :

### `FRUIT`

* Génère la position aléatoire du fruit
* Affiche le fruit à l’écran

### `SNAKE`

* Gère le corps du serpent (liste de positions)
* Gère le déplacement
* Ajoute des segments lors de la consommation d’un fruit

### `MAIN`

* Gère la logique globale du jeu
* Vérifie les collisions
* Met à jour les éléments du jeu


## Bibliothèques utilisées

### Pygame

Pygame
Utilisée pour :

* créer la fenêtre du jeu
* dessiner les objets (serpent et fruit)
* gérer les événements clavier
* contrôler la boucle de jeu


### Random

Module Python intégré utilisé pour placer les fruits aléatoirement.

### Vector2 (Pygame)

pygame.math.Vector2
Utilisé pour représenter les positions et les directions du serpent.


## Contrôles

* ⬆️ Flèche haut : monter
* ⬇️ Flèche bas : descendre
* ⬅️ Flèche gauche : aller à gauche
* ➡️ Flèche droite : aller à droite


## Améliorations possibles

* Ajouter un écran de Game Over
* Ajouter un score affiché à l’écran
* Accélération progressive du jeu
* Le jeu ne s’arrête pas lorsque le serpent touche les bords de la fenêtre


## Contexte

Projet réalisé en **2022** lors d’un stage d’initiation à la programmation d’une semaine à l’association **Science Ouverte**.

Projet développé dans un cadre éducatif pour apprendre les bases du développement de jeux vidéo en Python.

