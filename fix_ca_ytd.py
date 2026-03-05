# Fix CA YTD 
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace CA YTD observation
old_obs = '''    <strong>⚠ Observation</strong>
    <p>Le chiffre d'affaires cumulé atteint 93 % de l'objectif annuel, laissant un écart de 7 % à combler avant la clôture. Un rééquilibrage stratégique est nécessaire.</p>'''
new_obs = '''    <strong>Observation</strong>
    <p>Le chiffre d'affaires cumulé atteint 93% de l'objectif annuel, laissant un écart de 7% à combler avant clôture.</p>'''
if old_obs in content:
    content = content.replace(old_obs, new_obs)
    print("✓ CA YTD observation updated")

# Replace CA YTD action
old_action = '''    <div class='modal-section'>
    <strong>🎯 Plan d'Action</strong>
    <p>Réallouer temporairement des ressources commerciales vers BAAMTU Côte d'Ivoire afin d'accélérer la prospection et la conversion des opportunités en cours.</p>
    </div>
    <div class='modal-section'>
    <strong>📈 Impact Attendu</strong>
    <p>Réduction de l'écart budgétaire et alignement progressif sur l'objectif annuel.</p>
    </div>">⚠ Rééquilibrer performance'''
new_action = '''    <div class='modal-section'>
    <strong>🎯 Décision Exécutive</strong>
    <p>Réallouer temporairement les ressources commerciales vers les entités sous-performantes.</p>
    </div>
    <div class='modal-section'>
    <strong>Plan d'Action</strong>
    <p>Accélérer closing des opportunités chaudes<br>Mettre en place plan d'actions ciblé sur BAAMTU Côte d'Ivoire<br>Organiser revue pipeline hebdomadaire<br>Prioriser les contrats à cycle court</p>
    </div>">⚠ Rééquilibrer performance'''
if 'Côte d' in content and 'Plan d' in content:
    content = content.replace(old_action, new_action)
    print("✓ CA YTD action updated")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
