# SignProc Résumé 2021

## Modalités

5 pages de résumé recto-verso. Pas d'exercices dans le résumé

### Contenu

## Rappel sur les examens (12.01.2022)

Ce qu'il n'y a pas :

- Algebre linéare
  - Lemme d'inversion
  - Normes L1 pour matrices
  - Valeurs propres et vecteurs propres
  - Théorème spéctral
  - Matrices mal conditionnées (et tout ce qui suit)
- Aléatoire
  - Variables conjointes
  - estimation par les moindres carrés
  - Meilleure estimation
  - Wide stationary process
  - Ergodicité
  - Power spectrum (a partir de 51)

Ce qu'il y a:

- Signaux et systèmes (introduction)
  - Tout
  - Tranformée en $z$
  - Filtres
  - DFT / FFT
- Algebre linéaires
  - Systèmes sur-déterminés avec moindres carrés
  - Poser les équations d'un problème (comme l'ellipse)
  - Formes spéciales de matrices (diagonales, etc...)
- Aléatoire
  - Variables
  - mapping
  - distribution et densité
  - espérence et variance (et espérence d'un fonction de variable aléatoire)
  - corrélation et covariance
  - orthogonalité des variables aléatoires
  - distribution gaussienne
  - Biais et consistance (important)
  - estimateurs (P.25-26 ?)
  - Processus aléatoires (ensemble de variables aléatoires)
  - moyennes d'ensembles
  - autocorrélations
  - Processus gaussien (savoir ce que c'est mais pas les calculs)
  - Savoir ce qu'est un processus stationnaire
  - matrice d'autocorrelation
  - Bruit blanc
- AWGN et Shannon
  - Débit, limites
  - Bruit
  - Sensibilité
  - BER
  - un peut tout

### Exercices à savoir

- Aléatoire
  - 3.3

## Liste des sujets

1) Introduction (signaux et systèmes)
   1) Signaux
   2) Saut unitaire
   3) unit sample
   4) Exponentielle complexes
   5) Linéarité, invariance en temps
   6) Convolution
   7) Causalité, stabilité, inversibilité
   8) DTFT, FFT et considérations
   9) (Transformée en z)
   10) Pôles, zéros
2) Algèbre linéaire
   1) Norme, transposée (hermitienne), span, rang, déterminant
   2) Équations linéaires
   3) Systèmes sous/sur-déterminés
   4) Valeurs propres
   5) Optimisation
3) Processus aléatoires en temps discret
   1) Variables aléatoires
   2) Distribution de probabilité
   3) Variance, sigma
   4) Orthogonalité
   5) Biais et consistence
   6) Moindre-carrés
   7) Procédés aléatoires
   8) Corrélation / autocorrélation
   9) Bruit et spectre
4) Introduction aux systèmes de communication
    1) OSI
    2) Canal de transmission
    3) Modèle
    4) Champ électromagnétique et atténuation
    5) Ondes
    6) Puissance, Friis
5) Codage de source
   1) Mesure de l'information
   2) Codes
   3) Huffman
   4) lempel-Ziv
   5) Lossless vs Lossy
6) Canal AWGN et limite de Shannon
   1) Symboles et signaux
   2) Bruit, AWGN
   3) Théorème de Shannon-Hartley
   4) Limite de Shannon
   5) Caractéristiques des systèmes de communication
7) Wireless
   1) Atténuation
   2) Path Loss exponent
   3) Fading, log-distance
   4) perturbations (atmosphère, ground reflection, diffraction, fresnel, multi-path, Rayleigh, Rician, Nakagami)
   5) Classification
   6) Doppler
8) Codage de canal (1-3)
   1) BER
   2) Hamming, dmin
   3) Paramètres standards (n, k, d, q)
   4) Matrices, systématique / non systématique
   5) Efficacité
   6) Syndrome
   7) Codes polynomiaux
   8) Codes Cycliques
   9) BCH
   10) Galois
   11) Polynôme primitif
   12) Générateurs
   13) Reed-Solomon
   14) Treillis
   15) Viterbi
9) Modulations
   1) Modulation en amplitude/fréquence/phase
   2) Bande passante
   3) ISI, Filtres (RC, Roll-off)
   4) Constellations, symboles
   5) DSSS
   6) OFDM
   7) Acronymes
10) Multiple-access
    1) Half/full duplex
    2) TDD / FDD
    3) Filtres
    4) Collisions (CSMA)
    5) TDMA, FDMA, CDMA, OFDMA, SDMA
    6) Walsh-Hadamard
    7) SISO, SIMO, MISO, MIMO, Massive MIMO
11) Acquisition et synchronisation
    1) Détection
    2) PAM
    3) AGC
    4) Récupération de la porteuse
    5) VCO
    6) Synchronisation de symboles (Early-late)
    7) Égalisation en temps
    8) Égalisation en fréquence (OFDM pilotes, égaliseur)