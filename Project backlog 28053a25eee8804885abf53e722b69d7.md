# Project backlog

## Overall features / key specs

- Saisie des données par laboratoire/unité (personnel, déplacements, infrastructure, équipements, achats, services, cloud)
- Calcul des émissions CO₂-eq selon les facteurs d'émission
- Visualisation des résultats et export de données
- Simulation de projets de recherche
- Interfaces de gestion pour IT et métier
- Authentification et gestion des rôles utilisateurs
- API REST et système d'ingestion automatique
- Support multilingue et accessibilité
- Documentation, support et formation
- Maintenance, tests et revue de code

### ⚡S0

- Définition design system
    
    Création de standards pour les formulaires, tableaux et graphiques
    
    Structuration des interfaces de saisie structurées par domaine (laboratoire, déplacements, infrastructure, équipements, achats, services, cloud, etc.). Placeholders Il permet à l’utilisateur :
    
    - d’accéder uniquement aux modules autorisés selon son rôle ;
    - de saisir les données via des champs contrôlés et assistés ;
    - de visualiser, modifier, trier ou supprimer les lignes saisies ;
    - de consulter en temps réel l’impact CO2-eq calculé ;
    - de valider un module une fois complet ;
    - de naviguer librement entre les modules ;
    - d’importer des données en CSV ou via ingestion automatique.
    Le cas échéant, ce module inclut également des sous-modules spécifiques (ex. : émissions directes, transport des
    achats, impact cloud) et des fonctionnalités optionnelles selon les besoins de chaque unité

prendre connaissance de quelles data sont dispos sous quelles formes

### ⚡S1 ⚖️

- Page d'accueil minimaliste
    
    Interface simplifiée avec sélection du laboratoire
    
- Module mon labo
    
    Saisie EPT, surfaces, infos de base, import data en csv
    
- Module déplacement pro
    
    Import data en csv
    
    Saisie déplacements (train, avion)
    
    Calcul Co2 en temps réel
    
    intégrations facteurs d’émissions
    

Validation specs S2 : Module Infrastucture

### ⚡S2 ⚖️

- Module Infrastucture
    
    Import data en csv
    
    Saisie bâtiments, ventilation, chauffage, éclairage
    
    occupation des locaux et surface de pièces correspondant au nom du labo auto avec un fichier csv métier
    
    Intégration des facteurs d'émission liés à la consommation électrique
    
    calcul CO2 avec le coeff du bâtiment (qui est dans un csv Métier)
    
    - Sous-module émissions directes (optionnel)
        
        Import data en csv
        
        Saisie des émissions directes du laboratoire
        
- Navigation inter-modules (placeholders de toute l’architecture)
    
    Système de navigation entre les différents modules de l'application
    
- Améliorations UX
    
    Ergonomie améliorée (accessibilité)
    

specs S3 :  Modules consomation électrique équipements / Achats

### ⚡S3 ⚖️

- Module consommation électrique équipements
    
    Import data en csv
    
    Saisie équipements + consommation électrique + usage (se base sur N-1)
    
    avec trois familles
    
    Ajout des facteurs d'émission spécifiques aux différents types d'équipements
    
    (optionel) modif cat. et sous cat depuis interface gestion métier
    
    Calcul CO2-eq par équipement
    
- Visualisation des résultats
    
    Graphiques, filtres interactifs pour mieux analyser les données
    
- Export des résultats
    
    Export des résultats (CSV, PDF)
    

specs S4: Modules achats

*Livrable : App structure (prototype)* 

### ⚡S4 ⚖️

- Auth : Gestion des rôles (5 types) & Mapping des rôles avec Accred & Sécurité d'accès (groupes, permissions)
    
    Définition et attribution des différents niveaux d'accès utilisateurs
    
    Intégration avec le système de gestion des accès EPFL
    
    Protection des données sensibles selon les droits utilisateurs (groupes, permissions)
    
- Journalisation / logs
    
    Enregistrement des actions 
    
    historique
    
- Module achats (1/2)
    
    Import data en csv
    
    Saisie achats (NACRES, IT, consommables)
    
    calcul du CO2-eq
    
    Intégration des facteurs d'émission liés aux achats
    
    fichier contenant les codes NACRES et facteurs import et export possible depuis Métier
    
    fichier correspondance UNSCP ↔ NACRES import et export depuis Métier
    
    Transport des achats (optionnel)
    
    Empreinte carbone alternative (optionnel)
    
    outil IA EPFL (optionnel)
    

specs S5: Module Achat / service interne

### ⚡S5 ⚖️

- Module achats (2/2)
    
    Import data en csv
    
    Saisie achats (NACRES, IT, consommables)
    
    calcul du CO2-eq
    
    Intégration des facteurs d'émission liés aux achats
    
    fichier contenant les codes NACRES et facteurs import et export possible depuis Métier
    
    fichier correspondance UNSCP ↔ NACRES import et export depuis Métier
    
    Transport des achats (optionnel)
    
    Empreinte carbone alternative (optionnel)
    
    outil IA EPFL (optionnel)
    
- Comparaison temporelle
    
    montrer les tendances, les catégories et sous catégories sur plusieurs années
    
    naviguer entre plusieurs années
    
- Documentation user help
    
    CMS pour documentation, système de gestion de contenu pour textes explicatifs sans passer par le prestataire
    
    interface documentation
    
    intégrer des explication pour les modules
    
    3 pages; explication durabilité, info et liens ress externe, info et liens ress intern
    
- Ingestion automatique CSV (optionnel)
    
    Import automatisé de fichiers CSV depuis sources externes
    

specs S6: Module services interne

### ⚡S6 ⚖️

- Module services Interne
    
    Import data en csv
    
    Saisie services internes (plateformes, types)
    
    liste de centres et plateformes modif depuis Métier
    
- Métier complet/restreint
    
    Suivi, import, seuils critiques
    
    vu restreinte vs complet
    
- Messages d'erreur et validations
    
    Validation en temps réel des données saisies
    
- Interface IT
    
    Activation des module
    
    Gestion des utilisatrices et utilisateurs
    
    Configuration et supervision du système
    
    Gestion des données et des logs
    

specs S7: Alimentation et énergie grise / module service cloud

*Alpha version (6 modules)*

### ⚡S7 ⚖️

- Alimentation et pendularité (optionel)
    
    calcul  avec data fourni par Métier et module labo
    
- Energie grise (optionel)
    
    calcul avec data fourni par Métier
    

Specs S8: Module service cloud / Déchets / Simulation de projet

### ⚡S8 ⚖️

- Module Impact des services cloud (optionel)
    
    Intégration des facteurs d'émission liés aux services
    
    type de services et facteurs mis à jour dans Métier
    
- Déchets (optionel)
    
    calcul avec data fourni par Métier et module labo
    

Specs S9: Simulation de projet

### ⚡S9 ⚖️

- Simulation de projet (optionnel)
- API REST sécurisée (lecture)
    
    Mise en place d'une API sécurisée avec authentification
    
- Documentation Swagger/OpenAPI
    
    Documentation complète des endpoints disponibles
    

Retour

### ⚡S10

- Intégration des retours
    
    Ajustements UX/UI
    
    Corrections mineures
    
    Préparation à la mise en production