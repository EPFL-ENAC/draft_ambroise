
### ⚡S1 27.10 - 18.11

- API REST sécurisée (lecture)
    
    *CC 3.8.2*
    
    Mise en place d'une API sécurisée avec authentification
    
    documentation technique format OpenAPI/Swagger
    
- Gestion des rôles & Mapping Accred 🟠
    
    & Sécurité d'accès (groupes, permissions)
    
    *CC 3.8.3* 
    
    Use first Keycloack for testing
    
    Définition et attribution des différents niveaux d'accès utilisateurs
    
    Intégration avec le système de gestion des accès EPFL
    
    Protection des données sensibles selon les droits utilisateurs (groupes, permissions)
    
- Pages d'accueil minimalistes : Login, Unit selection, Year selection & Home
- Navigation inter-modules (Placeholders de toute l’architecture) — 1 wk
    
    Système de navigation entre les différents modules de l'application
    
    différentes pour chaque rôles
    
- Implémentation schéma de DB.
- gestion des utilisateurs

[Specs] Déplacement pro

[Specs] Résultat

### ⚡S2  19.11 - 02.12

Fixes de S1

- Interface admins et gestion des 5 rôles 
    *CC 3.7.8*
    
    Gestionnaire IT
    
    Gestionnaire Métier complet/restreint
    
    Utilisateurice principal/standard
    
- Déplacement pro 🟢
    
    *Annexe 6 3.3.4* 
    
    Import data en csv (manuel)
    
    Saisie déplacements, km, moyen de transport, etc..
    
    Calcul Co2 en temps réel avec l’aide des facteurs
    
    intégrations facteurs d’émissions
    
    Messages d’erreurs et validations
    
    Sauvegarde et historiques
    
    visualisation des data rentrées, avec filtres et graphiques
    
    implémentation des datas dans la DB
    
    gestion des accès/visualisations par utilisateurs
    
    Affichage de message si dépasse un certains seuils
    
- Améliorations UX
    
    Ergonomie améliorée (accessibilité)
    

[Specs] Mon labo

[Specs] Achat

### ⚡S3 03.12 - 18.12 

- Fixes de S2
- Résultats visu et calculs 🟢
    
    Graphiques, filtres interactifs pour mieux analyser les données
    
    comparaison temporelle
    
    export des résultats CSV/PDF
    
- Mon labo  🟢
    
    *Annexe 6 3.3.3*
    
    Saisie EPT, surfaces, infos de base
    
    import data en csv
    
    Messages d’erreurs et validations
    
    Sauvegarde et historiques
    
    visualisation des data rentrées, avec filtres et graphiques
    
    implémentation des datas dans la DB
    
    gestion des accès/visualisations par utilisateurs
    

[Specs] Infrastructure



### ⚡S4 19.12 - 19.01

- Fixes de S3
- Achats **Poc** 🟡🟢
    
    *Annexe 6 3.3.7.1*  
    
    construction avec sous modules
    
    Import data en csv
    
    Saisie achats (NACRES, IT, consommables)
    
    calcul du CO2-eq
    
    Intégration des facteurs d'émission liés aux achats
    
    fichier contenant les codes NACRES et facteurs import et export possible depuis Métier
    
    fichier correspondance UNSCP ↔ NACRES import et export depuis Métier
    
    Messages d’erreurs et validations
    
    Sauvegarde et historiques
    
    visualisation des data rentrées, avec filtres et graphiques
    
    implémentation des datas dans la DB
    
    gestion des accès/visualisations par utilisateurs
    
    Affichage de message si dépasse un certains seuils
    
    intégrer des explication sur les calculs
    
    Transport des achats (optionnel) 🟡
    
    Empreinte carbone alternative (optionnel)
    
    outil IA EPFL (optionnel)
    
- Documentation user help
    
    CMS pour documentation, système de gestion de contenu pour textes explicatifs sans passer par le prestataire
    
    interface documentation
    
    3 pages; explication durabilité, info et liens ress externe, info et liens ress intern
    

[Specs] Services interne

### ⚡S5 20.01 - 10.02

- Fixes de S4
- Achats **Done**
    
    *Annexe 6 3.3.7.1*
    
    construction avec sous modules
    
    Import data en csv
    
    Saisie achats (NACRES, IT, consommables)
    
    calcul du CO2-eq
    
    Intégration des facteurs d'émission liés aux achats
    
    fichier contenant les codes NACRES et facteurs import et export possible depuis Métier
    
    fichier correspondance UNSCP ↔ NACRES import et export depuis Métier
    
    Messages d’erreurs et validations
    
    Sauvegarde et historiques
    
    visualisation des data rentrées, avec filtres et graphiques
    
    implémentation des datas dans la DB
    
    gestion des accès/visualisations par utilisateurs
    
    Affichage de message si dépasse un certains seuils
    
    intégrer des explication sur les calculs
    
    sous module Transport des achats (optionnel)
    
    Empreinte carbone alternative (optionnel)
    
    outil IA EPFL (optionnel)
    
- Infrastucture 🟡
    
    *Annexe 6 3.3.5.1* 
    
    Import data en csv
    
    calcul du CO2-eq
    
    Messages d’erreurs et validations
    
    Sauvegarde et historiques
    
    visualisation des data rentrées, avec filtres et graphiques
    
    implémentation des datas dans la DB
    
    gestion des accès/visualisations par utilisateurs
    
    Affichage de message si dépasse un certains seuils
    
    intégrer des explication sur les calculs
    
    Saisie bâtiments, ventilation, chauffage, éclairage
    
    occupation des locaux et surface de pièces correspondant au nom du labo auto avec un fichier csv métier
    
    Intégration des facteurs d'émission liés à la consommation électrique
    
    calcul CO2 avec le coeff du bâtiment (qui est dans un csv Métier)
    

[Specs] Consommation électrique

[Specs] Impact des services cloud

### ⚡S6 11.02 - 02.03

- Fixes de S5
- Consommation électrique équipements  **🟡
    
    *Annexe 6 3.3.6*
    
    Import data en csv
    
    Messages d’erreurs et validations
    
    Sauvegarde et historiques
    
    visualisation des data rentrées, avec filtres et graphiques
    
    implémentation des datas dans la DB
    
    gestion des accès/visualisations par utilisateurs
    
    Affichage de message si dépasse un certains seuils
    
    Saisie équipements + consommation électrique + usage (se base sur N-1)
    
    avec trois familles
    
    Ajout des facteurs d'émission spécifiques aux différents types d'équipements
    
    (optionel) modif cat. et sous cat depuis interface gestion métier
    
    Calcul CO2-eq par équipement
    
- Services Interne  🟠
    
    *Annexe 6 3.3.8* 
    
    Import data en csv
    
    Saisie services internes (plateformes, types)
    
    liste de centres et plateformes modif depuis Métier
    
- Impact des services cloud (optionel)  🟠
    
    *Annexe 6 3.3.9* 
    
    Intégration des facteurs d'émission liés aux services
    
    type de services et facteurs mis à jour dans Métier
    

[Specs] Emissions directs

[Specs] Alimentation et pendularité

[Specs] Energie grise



### ⚡S7 03.03 - 23.03

- Fixes S6
- émissions directes (optionnel) 🟡
    
    Import data en csv
    
    Saisie des émissions directes du laboratoire
    
- Alimentation et pendularité (optionel) 🟡
    
    calcul  avec data fourni par Métier et module labo
    
- Energie grise (optionel) 🟡
    
    calcul avec data fourni par Métier
    

[Specs] Simulation de projet

[Specs] Déchets

### ⚡S8 23.03 - 13.04

- Fixes S7
- Gestion des bugs et ajouts intégrations des retours
    
    Intégrations des retours
    
    corriger bugs et imprévus
    
- Déchets (optionel) 🟡
    
    calcul avec data fourni par Métier et module labo
    

[Specs] Simulation de projet

### ⚡S9 14.04 - 04.05

- Fixes S8
- Simulation de projet (optionnel) 🔴
- Gestion des bugs et ajouts intégrations des retours
    
    Intégrations des retours
    
    corriger bugs et imprévus
    

[Specs] : S10

### ⚡S10 05.05 - 26.05

- Fixes S9
- Gestion des bugs et intégrations des retours
    
    Intégrations des retours
    
    corriger bugs et imprévus
    
- Intégration des retours
    
    Ajustements UX/UI
    
    Corrections mineures
    
    Préparation à la mise en production