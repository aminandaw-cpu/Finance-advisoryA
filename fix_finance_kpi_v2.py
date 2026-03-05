#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

# Read the HTML file
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Carnet old decision/action
if "Plan d'Action" in content and "Prioriser la livraison des contrats stratégiques à forte marge afin de sécuriser la rentabilité" in content:
    # Find and replace the carnet section for decision/action
    old = '''    <div class='modal-section'>
    <strong>🎯 Plan d'Action</strong>
    <p>Prioriser la livraison des contrats stratégiques à forte marge afin de sécuriser la rentabilité et respecter les engagements clients.</p>
    </div>
    <div class='modal-section'>
    <strong>📈 Impact Attendu</strong>
    <p>Stabilisation des revenus futurs et amélioration du taux de conversion en chiffre d'affaires réalisé.</p>
    </div>">✓ Sécuriser exécution</span>'''

    new = '''    <div class='modal-section'>
    <strong>🎯 Décision Exécutive</strong>
    <p>Prioriser l'exécution des contrats stratégiques à forte marge.</p>
    </div>
    <div class='modal-section'>
    <strong>Plan d'Action</strong>
    <p>Allocation optimale des équipes delivery<br>Suivi rapproché des jalons critiques<br>Anticipation des risques de retard<br>Accélération facturation intermédiaire</p>
    </div>">✓ Sécuriser exécution</span>'''

    content = content.replace(old, new)
    print("✓ Carnet decision/action updated")
else:
    print("⚠ Carnet decision/action pattern not found")

# Write the file back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done")
