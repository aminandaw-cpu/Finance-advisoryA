#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

# Read the HTML file
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# CA YTD vs Objectif - replace observation and action section
old_ca_ytd_obs = '''    <strong>⚠ Observation</strong>
    <p>Le chiffre d'affaires cumulé atteint 93 % de l'objectif annuel, laissant un écart de 7 % à combler avant la clôture. Un rééquilibrage stratégique est nécessaire.</p>'''

new_ca_ytd_obs = '''    <strong>Observation</strong>
    <p>Le chiffre d'affaires cumulé atteint 93% de l'objectif annuel, laissant un écart de 7% à combler avant clôture.</p>'''

if old_ca_ytd_obs in content:
    content = content.replace(old_ca_ytd_obs, new_ca_ytd_obs)
    print("✓ CA YTD observation updated")
else:
    print("⚠ CA YTD observation not found")

# CA YTD - replace decision/action section
old_ca_ytd_action = '''    <strong>🎯 Plan d'Action</strong>
    <p>Réallouer temporairement des ressources commerciales vers BAAMTU Côte d'Ivoire afin d'accélérer la prospection et la conversion des opportunités en cours.</p>
    </div>
    <div class='modal-section'>
    <strong>📈 Impact Attendu</strong>
    <p>Réduction de l'écart budgétaire et alignement progressif sur l'objectif annuel.</p>'''

new_ca_ytd_action = '''    <strong>🎯 Décision Exécutive</strong>
    <p>Réallouer temporairement les ressources commerciales vers les entités sous-performantes.</p>
    </div>
    <div class='modal-section'>
    <strong>Plan d'Action</strong>
    <p>Accélérer closing des opportunités chaudes<br>Mettre en place plan d'actions ciblé sur BAAMTU Côte d'Ivoire<br>Organiser revue pipeline hebdomadaire<br>Prioriser les contrats à cycle court</p>'''

if old_ca_ytd_action in content:
    content = content.replace(old_ca_ytd_action, new_ca_ytd_action)
    print("✓ CA YTD decision/action updated")
else:
    print("⚠ CA YTD decision/action not found")

# Trésorerie - replace observation
old_treso_obs = '''    <strong>⚠ Observation</strong>
    <p>La trésorerie atteint 78 %, en dessous du seuil cible de 85 %, exposant l'entreprise à un risque de tension de liquidité à court terme.</p>'''

new_treso_obs = '''    <strong>Observation</strong>
    <p>La trésorerie est inférieure au seuil cible de 85%, exposant à un risque de tension court terme.</p>'''

if old_treso_obs in content:
    content = content.replace(old_treso_obs, new_treso_obs)
    print("✓ Trésorerie observation updated")
else:
    print("⚠ Trésorerie observation not found")

# Trésorerie - replace decision/action section
old_treso_action = '''    <strong>🎯 Plan d'Action</strong>
    <p>Déclencher une procédure de relance prioritaire sur les créances critiques, notamment le client ECOBANK Core Upgrade, afin d'accélérer le recouvrement.</p>
    </div>
    <div class='modal-section'>
    <strong>📈 Impact Attendu</strong>
    <p>Amélioration du flux de trésorerie et sécurisation des capacités d'investissement.</p>'''

new_treso_action = '''    <strong>🎯 Décision Exécutive</strong>
    <p>Prioriser le recouvrement des créances critiques avant tout nouvel engagement significatif.</p>
    </div>
    <div class='modal-section'>
    <strong>Plan d'Action</strong>
    <p>Relance client ECOBANK Core Upgrade<br>Mise en place suivi hebdomadaire cash<br>Négociation délais fournisseurs si nécessaire<br>Réduction dépenses non essentielles</p>'''

if old_treso_action in content:
    content = content.replace(old_treso_action, new_treso_action)
    print("✓ Trésorerie decision/action updated")
else:
    print("⚠ Trésorerie decision/action not found")

# Carnet de Commandes - replace observation
old_carnet_obs = '''              <strong>✓ Observation</strong>
              <p>Le carnet de commandes est solide et offre une visibilité confortable sur les revenus futurs, notamment sur les projets ORANGE Data Integration et SONATEL Phase 1.</p>'''

new_carnet_obs = '''    <strong>Observation</strong>
    <p>Le carnet de commandes offre une visibilité confortable sur les revenus futurs.</p>'''

if old_carnet_obs in content:
    content = content.replace(old_carnet_obs, new_carnet_obs)
    print("✓ Carnet observation updated")
else:
    print("⚠ Carnet observation not found")

# Carnet de Commandes - replace decision/action section
old_carnet_action = '''    <strong>🎯 Plan d'Action</strong>
    <p>Prioriser la livraison des contrats stratégiques à forte marge afin de sécuriser la rentabilité et respecter les engagements clients.</p>
    </div>
    <div class='modal-section'>
    <strong>📈 Impact Attendu</strong>
    <p>Stabilisation des revenus futurs et amélioration du taux de conversion en chiffre d'affaires réalisé.</p>'''

new_carnet_action = '''    <strong>🎯 Décision Exécutive</strong>
    <p>Prioriser l'exécution des contrats stratégiques à forte marge.</p>
    </div>
    <div class='modal-section'>
    <strong>Plan d'Action</strong>
    <p>Allocation optimale des équipes delivery<br>Suivi rapproché des jalons critiques<br>Anticipation des risques de retard<br>Accélération facturation intermédiaire</p>'''

if old_carnet_action in content:
    content = content.replace(old_carnet_action, new_carnet_action)
    print("✓ Carnet decision/action updated")
else:
    print("⚠ Carnet decision/action not found")

# Write the file back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("\n✓ All updates completed successfully")
