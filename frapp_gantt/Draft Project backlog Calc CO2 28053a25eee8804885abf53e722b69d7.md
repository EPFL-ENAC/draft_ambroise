# Draft Project backlog Calc CO2

Type: Discussion
Created: 2 octobre 2025 16:38
Last Edited Time: 2 octobre 2025 16:39
Created By: ambroise.delaly@epfl.ch

## Projet Backlog

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

### ⚡S1

- Feat
    - Définition d'un mini design system
        
        Création de standards pour les formulaires, tableaux et graphiques
        
    - module mon labo
        
        Saisie EPT, surfaces, infos de base 
        
    - module déplacement pro
        
        Saisie déplacements (train, avion) 
        
    - Calcul CO2-eq en temps réel
        
        calcul directement los de la saisie le CO2-eq, lors de la validation
        Visualisation préliminaire des résultats en live
        
    - Import CSV manuel
        
        avec format de variables imposé
        
    - Intégration des premiers facteurs d'émission (transport)
        
        ajouter un facteurs modulable au sein du calcul, pourra être modifé avec un import de Métier
        
    - data Métier espace
        
        peut ajouter des csv qui sont pris en compte lors des calculs
        
        ajouter d’autre données qui sont reprises dans les opérations côté users
        
    - AUTH
        
        connexion sous différents rôles simples (sans lier à ACCRED)
        
- Users stories
    
    En tant qu'utilisateur principal, je veux saisir les données de mon labo pour calculer les émissions.
    En tant qu'utilisateur standard, je veux saisir mes déplacements pour contribuer au calcul.
    En tant qu'utilisateur, je veux voir l'impact CO2-eq dès la saisie.
    
    En tant que métier je veux modifir les facteurs et d’autres fonctions
    
    En tant qu’utilisateur je veux me conecter et avoir accès à ce que j’ai le droit
    

### ⚡S2

- Feat
    - Module Infrastucture
        
        Saisie bâtiments, ventilation, chauffage, éclairage
        
        occupation des locaux et surface de pièces correspondant au nom du labo auto avec un fichier csv métier
        
        Intégration des facteurs d'émission liés à la consommation électrique
        
        calcul CO2 avec le coeff du bâtiment (qui est dans un csv Métier)
        
    - Sous-module émissions directes (optionnel)
        
        Saisie des émissions directes du laboratoire
        
    - Navigation inter-modules
        
        Système de navigation entre les différents modules de l'application
        
- Users stories
    
    En tant qu'utilisateur principal, je veux saisir les données de consommation énergétique des bâtiments pour calculer les émissions associées.
    En tant qu'utilisateur principal, je veux pouvoir naviguer facilement entre les différents modules.
    

### ⚡S3

- Feat
    - Module consommation électrique équipements
        
        Saisie équipements + consommation électrique + usage (se base sur N-1)
        
        avec trois familles
        
        Ajout des facteurs d'émission spécifiques aux différents types d'équipements
        
        (optionel) modif cat. et sous cat depuis interface gestion métier
        
    - Calcul CO2-eq par équipement
        
        Calcul CO2-eq spécifique pour chaque type d'équipement
        
    - Visualisation améliorée
        
        Graphiques, filtres interactifs pour mieux analyser les données
        
    - Messages d'erreur et validations
        
        Validation en temps réel des données saisies
        
- Users stories
    
    En tant qu'utilisateur princ, je veux importer mes équipements pour calculer leur impact.
    En tant qu'utilisateur princ, je veux des messages clairs en cas d'erreur ou de données manquantes.
    En tant qu'utilisateur, je veux visualiser mes résultats avec des filtres interactifs.
    

### ⚡S4

- Feat
    - Module achats
        
        Saisie achats (NACRES, IT, consommables)
        
        calcul du CO2-eq
        
        Intégration des facteurs d'émission liés aux achats
        
        fichier contenant les codes NACRES et facteurs import et export possible depuis Métier
        
        fichier correspondance UNSCP ↔ NACRES import et export depuis Métier
        
        Transport des achats (optionnel)
        
        Empreinte carbone alternative (optionnel)
        
        outil IA EPFL (optionnel)
        
    - Export des résultats
        
        Export des résultats (CSV, PDF)
        
- Users stories
    
    En tant qu'utilisateur, je veux saisir mes achats pour calculer leur empreinte.
    En tant qu'utilisateur, je veux exporter mes résultats pour les partager.
    

### ⚡S5

- Feat
    - Module services Interne
        
        Saisie services internes (plateformes, types)
        
        liste de centres et plateformes modif depuis Métier
        
    - Module Impact des services cloud (optionel)
        
        Intégration des facteurs d'émission liés aux services
        
        type de services et facteurs mis à jour dans Métier 
        
    - Améliorations UX
        
        Ergonomie améliorée (accessibilité)
        
    - Déchets (optionel)
        
        calcul avec data fourni par Métier et module labo
        
    - Alimentation et pendularité (optionel)
        
        calcul  avec data fourni par Métier et module labo
        
    - Energie grise (optionel)
        
        calcul avec data fourni par Métier
        
- Users stories
    
    En tant qu'utilisateur, je veux indiquer les services utilisés pour calculer leur impact.
    
    En tant qu'utilisateur, je veux une navigation fluide et intuitive.
    

### ⚡S6

- Feat
    - Interface IT
        
        Activation des module
        
        Gestion des utilisatrices et utilisateurs
        
        Configuration et supervision du système
        
        Gestion des données et des logs
        
    - Interface Métier complet
        
        Suivi, import, seuils critiques
        
    - Interface Métier restreint
        
        Vue faculté
        
    - Documentation
        
        CMS pour documentation, système de gestion de contenu pour textes explicatifs sans passer par le prestataire
        
        interface documentation
        
        intégrer des explication pour les modules
        
        3 pages; explication durabilité, info et liens ress externe, info et liens ress intern
        
    - Journalisation
        
        Enregistrement des actions et connexions
        
- Users stories
    
    En tant que gestionnaire IT, je veux activer/désactiver/modifier des modules selon les besoins.
    
    En tant que gestionnaire Métier, je veux suivre la complétion des modules et éditer la documentation.
    
    En tant qu'administrateur, je veux accéder aux logs pour assurer la traçabilité.
    

### ⚡S7

- Feat
    - Connexion via MS Entra ID (OIDC/SAML2)
        
        Authentification sécurisée via Microsoft Entra ID
        
    - Mapping des rôles avec Accred
        
        Intégration avec le système de gestion des accès EPFL
        
    - Gestion des rôles (5 types)
        
        Définition et attribution des différents niveaux d'accès utilisateurs
        
    - Sécurité d'accès (groupes, permissions)
        
        Protection des données sensibles selon les droits utilisateurs
        
    - Page d'accueil minimaliste
        
        Interface simplifiée avec sélection du laboratoire
        
- Users stories
    
    En tant qu'utilisateur EPFL, je veux me connecter via MS Entra ID pour accéder à l'application.
    
    En tant que gestionnaire IT, je veux attribuer des rôles et restreindre l'accès selon les groupes Accred.
    
    En tant qu'utilisateur, je veux sélectionner mon/mes laboratoire dès l'entrée dans l'application.
    

### ⚡S8

- Feat
    - Simulation de projet (optionnel)
        
        
    - Comparaison temporelle
        
        montrer les tendances, les catégories et sous catégories sur plusieurs années
        
- Users stories
    
    En tant que chercheur, je veux simuler un projet pour anticiper son empreinte.
    
    En tant qu'utilisateur, je veux comparer les émissions sur plusieurs années.
    

### ⚡S9

- Feat
    - API REST sécurisée (lecture)
        
        Mise en place d'une API sécurisée avec authentification
        
    - Documentation Swagger/OpenAPI
        
        Documentation complète des endpoints disponibles
        
    - Ingestion automatique CSV (optionnel)
        
        Import automatisé de fichiers CSV depuis sources externes
        
    - Données additionnelles (optionnel)
        
        Saisie de données sur les déchets, l'alimentation, la pendularité et l'énergie grise
        
- Users stories
    
    En tant que développeur, je veux accéder aux données via une API sécurisée pour intégrer les informations dans d'autres applications.
    
    En tant qu'utilisateur, je veux importer mes données automatiquement pour gagner du temps sur la saisie.
    
    En tant qu'utilisateur, je veux saisir des données additionnelles pour affiner le calcul d'empreinte carbone.
    

### ⚡S10

- Feat
    
    Intégration des retours utilisateurs
    
    Ajustements UX/UI
    
    Corrections mineures
    
    Préparation à la mise en production
    
- Users stories
    
    En tant qu'utilisateur, je veux que mes retours soient pris en compte pour améliorer l'application.
    
    En tant que gestionnaire, je veux que l'application soit stable et prête pour le déploiement.