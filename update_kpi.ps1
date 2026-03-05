$content = Get-Content index.html -Raw -Encoding UTF8

# CA YTD vs Objectif
$old_ca_ytd = '            <span class="badge b-warn clickable" style="cursor:pointer;" data-title="CA YTD vs Objectif — Advisory" data-message="<div class=''modal-section''>
    <strong>⚠ Observation</strong>
    <p>Le chiffre d''affaires cumulé atteint 93 % de l''objectif annuel, laissant un écart de 7 % à combler avant la clôture. Un rééquilibrage stratégique est nécessaire.</p>
    </div>
    <div class=''modal-section''>
    <strong>🎯 Plan d''Action</strong>
    <p>Réallouer temporairement des ressources commerciales vers BAAMTU Côte d''Ivoire afin d''accélérer la prospection et la conversion des opportunités en cours.</p>
    </div>
    <div class=''modal-section''>
    <strong>📈 Impact Attendu</strong>
    <p>Réduction de l''écart budgétaire et alignement progressif sur l''objectif annuel.</p>
    </div>">⚠ Rééquilibrer performance</span>'

$new_ca_ytd = '            <span class="badge b-warn clickable" style="cursor:pointer;" data-title="CA YTD vs Objectif — Advisory" data-message="<div class=''modal-section''>
    <strong>⚠ Observation</strong>
    <p>Le chiffre d''affaires cumulé atteint 93% de l''objectif annuel, laissant un écart de 7% à combler avant clôture.</p>
    </div>
    <div class=''modal-section''>
    <strong>🎯 Décision Exécutive</strong>
    <p>Réallouer temporairement les ressources commerciales vers les entités sous-performantes.</p>
    </div>
    <div class=''modal-section''>
    <strong>📋 Plan d''Action</strong>
    <p>Accélérer closing des opportunités chaudes<br>Mettre en place plan d''actions ciblé sur BAAMTU Côte d''Ivoire<br>Organiser revue pipeline hebdomadaire<br>Prioriser les contrats à cycle court</p>
    </div>">⚠ Rééquilibrer performance</span>'

if ($content -like "*$old_ca_ytd*") {
    Write-Host "✓ CA YTD trouvé"
    $content = $content -replace [regex]::Escape($old_ca_ytd), $new_ca_ytd
    Write-Host "✓ CA YTD remplacé"
} else {
    Write-Host "⚠ CA YTD not found"
}

# Trésorerie
$old_tresorerie = '            <span class="badge b-warn clickable" style="cursor:pointer;" data-title="Trésorerie — Advisory" data-message="<div class=''modal-section''>
    <strong>⚠ Observation</strong>
    <p>La trésorerie atteint 78 %, en dessous du seuil cible de 85 %, exposant l''entreprise à un risque de tension de liquidité à court terme.</p>
    </div>
    <div class=''modal-section''>
    <strong>🎯 Plan d''Action</strong>
    <p>Déclencher une procédure de relance prioritaire sur les créances critiques, notamment le client ECOBANK Core Upgrade, afin d''accélérer le recouvrement.</p>
    </div>
    <div class=''modal-section''>
    <strong>📈 Impact Attendu</strong>
    <p>Amélioration du flux de trésorerie et sécurisation des capacités d''investissement.</p>
    </div>">⚠ Recouvrer ECOBANK Core Upgrade</span>'

$new_tresorerie = '            <span class="badge b-warn clickable" style="cursor:pointer;" data-title="Trésorerie — Advisory" data-message="<div class=''modal-section''>
    <strong>⚠ Observation</strong>
    <p>La trésorerie est inférieure au seuil cible de 85%, exposant à un risque de tension court terme.</p>
    </div>
    <div class=''modal-section''>
    <strong>🎯 Décision Exécutive</strong>
    <p>Prioriser le recouvrement des créances critiques avant tout nouvel engagement significatif.</p>
    </div>
    <div class=''modal-section''>
    <strong>📋 Plan d''Action</strong>
    <p>Relance client ECOBANK Core Upgrade<br>Mise en place suivi hebdomadaire cash<br>Négociation délais fournisseurs si nécessaire<br>Réduction dépenses non essentielles</p>
    </div>">⚠ Sécuriser liquidité</span>'

if ($content -like "*$old_tresorerie*") {
    Write-Host "✓ Trésorerie trouvée"
    $content = $content -replace [regex]::Escape($old_tresorerie), $new_tresorerie
    Write-Host "✓ Trésorerie remplacée"
} else {
    Write-Host "⚠ Trésorerie not found"
}

# Carnet de Commandes
$old_carnet = '            <span class="badge b-ok clickable" style="cursor:pointer;" data-title="Carnet de Commandes — Advisory" data-message="<div class=''modal-section''>
              <strong>✓ Observation</strong>
              <p>Le carnet de commandes est solide et offre une visibilité confortable sur les revenus futurs, notamment sur les projets ORANGE Data Integration et SONATEL Phase 1.</p>
              </div>
    <div class=''modal-section''>
    <strong>🎯 Plan d''Action</strong>
    <p>Prioriser la livraison des contrats stratégiques à forte marge afin de sécuriser la rentabilité et respecter les engagements clients.</p>
    </div>
    <div class=''modal-section''>
    <strong>📈 Impact Attendu</strong>
    <p>Stabilisation des revenus futurs et amélioration du taux de conversion en chiffre d''affaires réalisé.</p>
    </div>">✓ Sécuriser exécution</span>'

$new_carnet = '            <span class="badge b-ok clickable" style="cursor:pointer;" data-title="Carnet de Commandes — Advisory" data-message="<div class=''modal-section''>
    <strong>✓ Observation</strong>
    <p>Le carnet de commandes offre une visibilité confortable sur les revenus futurs.</p>
    </div>
    <div class=''modal-section''>
    <strong>🎯 Décision Exécutive</strong>
    <p>Prioriser l''exécution des contrats stratégiques à forte marge.</p>
    </div>
    <div class=''modal-section''>
    <strong>📋 Plan d''Action</strong>
    <p>Allocation optimale des équipes delivery<br>Suivi rapproché des jalons critiques<br>Anticipation des risques de retard<br>Accélération facturation intermédiaire</p>
    </div>">✓ Sécuriser exécution</span>'

if ($content -like "*$old_carnet*") {
    Write-Host "✓ Carnet trouvé"
    $content = $content -replace [regex]::Escape($old_carnet), $new_carnet
    Write-Host "✓ Carnet remplacé"
} else {
    Write-Host "⚠ Carnet not found"
}

# Écrire le fichier
Set-Content index.html $content -Encoding UTF8
Write-Host "Fichier mis a jour avec succes"
