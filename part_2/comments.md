# Commentaires

## Description du dataset

Le dataset présente des données médicales sur des patients qui ont eu ou non des accidents vasculaires-cérébraux (AVC). 
Il provient de la plateforme [kaggle](https://www.kaggle.com/fedesoriano/stroke-prediction-dataset).

Il contient des informations sur 5110 patients ; certaines colonnes ont des données manquantes (4909 lignes complètes).

Les informations présentes dans le dataset sont : 
- un id unique pour chaque patient
- l'âge en années
- le genre
- la présence ou non d'hypertension
- la présence ou non de maladies cardiaques
- si l'individu a déjà été marié
- le type de travail (public, privé, indépendant, etc.)
- le type de résidence
- la glycémie moyenne (en g/cL -- unité de mesure non précisée dans le dataset mais déduite en comparant les valeurs du dataset avec les valeurs normales de glycémie
- l'IMC, mesure de la corpulence d'une personne à partir de sa taille et de son poids (techniquement en kg/m2 mais en pratique sans unité)
- le tabagisme
- le fait que l'individu aie déjà eu un AVC

De premier abord, on peut supposer que des mesures qui correspondent à conditions propices aux maladies en général (comme l'IMC, indicateur du surpoids ; la glycémie, indicative du diabète ; l'âge avancé) seront positivement corrélés avec la présence d'AVC.
On peut aussi supposer que des facteurs extérieurs qui sont connus pour avoir un effet négatif sur la santé (le tabagisme, la pollution de l'air quand on habite en ville) présenteront aussi une corrélation avec la présence d'AVC.

Le but de ce projet sera de prédire les AVC chez les patients à partir des différentes mesures afin de pouvoir les prévenir.

## Explication de l'analyse quantitative et de la visualisation

## Commentaire sur les résultats obtenus
