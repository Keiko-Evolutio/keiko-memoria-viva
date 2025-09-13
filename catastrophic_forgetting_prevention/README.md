# catastrophic_forgetting_prevention

Bio-inspirierte Mechanismen gegen katastrophales Vergessen (EWC, Experience Replay, ProgressiveNets).

## Installation (lokal im Repo)

- Python >= 3.10 empfohlen
- Abhängigkeiten: numpy, pytest (für Tests)

## Schnellstart

```python path=null start=null
from catastrophic_forgetting_prevention import CatastrophicForgettingPrevention, ModelWeights
import numpy as np

weights = {
    "layer_0": np.random.normal(0, 0.1, size=(8, 4)),
    "layer_1": np.random.normal(0, 0.1, size=(4, 2)),
}
model = ModelWeights(weights)

cfp = CatastrophicForgettingPrevention()
cfp.experience_replay.add({"task_id": "A", "content": "past_example"})
cfp.set_current_batch(["short", "x" * 200])

tasks = [
    {"input": i, "label": (i * 7) % 3} for i in range(10)
]

result = cfp.protect_critical_knowledge(model, tasks)
print(result)
```

Siehe auch `examples/tutorial.ipynb` für ein ausführliches Beispiel.

## Tests ausführen

Aus dem Projekt-Wurzelverzeichnis:

```bash
pytest -q catastrophic_forgetting_prevention/tests
```

## Design-Ziele

- Strikte Einhaltung von PEP 8 (100 Zeichen Zeilenlänge)
- Deutsche Docstrings/Kommentare, englische Bezeichner
- Relative Imports innerhalb des Pakets
- Vollständige Typannotationen

# Katastrophales Vergessen verhindern: Strategien für robustes Lernen in neuronalen Netzen

Katastrophales Vergessen stellt eine der fundamentalen Herausforderungen moderner künstlicher Intelligenz dar und
gefährdet das kontinuierliche Lernen neuronaler Netze. Das Phänomen beschreibt die drastische Abnahme der
Leistungsfähigkeit bei früher erlernten Aufgaben, sobald neue Informationen gelernt werden. Während biologische Systeme
durch evolutionär optimierte Mechanismen vor diesem Problem geschützt sind, erfordern technische Systeme innovative
Ansätze zur Wahrung der Balance zwischen Anpassungsfähigkeit und Gedächtnisstabilität.

## Definition und biologische Grundlagen

**Katastrophales Vergessen** wurde erstmals 1989 von McCloskey und Cohen systematisch beschrieben. Es tritt auf, wenn
neuronale Netze während des sequenziellen Trainings auf verschiedenen Aufgaben abrupt und dramatisch zuvor erlernte
Informationen verlieren. Das Phänomen entsteht durch die Art, wie maschinelle Lernalgorithmen ihre Gewichte anpassen:
Beim Erlernen neuer Aufgaben werden Parameter so modifiziert, dass sie die Verlustfunktion für die aktuelle Aufgabe
minimieren, was jedoch die für frühere Aufgaben optimalen Parameterwerte zerstört.

Biologische Systeme haben evolutionär ausgeklügelte Mechanismen entwickelt, um dieses Problem zu umgehen. Das *
*Hippocampus-Cortex-System** der Säugetiere stellt ein paradigmatisches Beispiel für die Lösung des
Plastizität-Stabilität-Dilemmas dar. Der Hippocampus fungiert als temporärer Speicher für episodische Erinnerungen und
ermöglicht schnelles, flexibles Lernen, während der Cortex für die langfristige Konsolidierung und stabile Speicherung
von Wissen verantwortlich ist.

Die **Systemkonsolidierung** beschreibt den graduellen Transfer von Informationen vom Hippocampus zum Neocortex. Während
dieser Phase, die bei Menschen ein bis zwei Jahrzehnte dauern kann, werden Erinnerungen durch wiederholte Reaktivierung
gestärkt und in kortikalen Netzwerken verankert. Schlaf spielt dabei eine entscheidende Rolle: Während der NREM-Phase
werden Gedächtnisspuren spontan reaktiviert, was zur Umorganisation synaptischer Verbindungen und zur Entstehung
orthogonaler Repräsentationen führt.

## Technische Ursachen und Mechanismen

Das katastrophale Vergessen in neuronalen Netzen resultiert aus mehreren fundamentalen Eigenschaften des stochastischen
Gradientenabstiegs und der Netzwerkarchitekturen. **Gewichtsinterferenz** entsteht, wenn neue Lernaufgaben Parameter in
Richtungen verschieben, die mit der optimalen Lösung vorheriger Aufgaben interferieren. Bei überparametrisierten
Netzwerken existieren zwar theoretisch Lösungen für mehrere Aufgaben gleichzeitig, doch fehlen dem Netzwerk Mechanismen
zur selektiven Nutzung relevanter Parameter.

Forschungen zeigen, dass große Modelle besonders anfällig für katastrophales Vergessen sind. Eine Studie aus 2023
demonstrierte, dass große Sprachmodelle schwerer unter dem Phänomen leiden als kleinere Modelle, was die Bedeutung
spezialisierter Strategien für moderne KI-Systeme unterstreicht. Der Verlust der **Plastizität** verschärft das Problem
zusätzlich: Netzwerke verlieren im Laufe des Trainings ihre Fähigkeit zur Anpassung an neue Aufgaben, was sowohl das
Erlernen neuer Informationen als auch das Beibehalten alter Kenntnisse erschwert.

## Regularisierungsbasierte Strategien

### Elastic Weight Consolidation (EWC)

**Elastic Weight Consolidation** stellt einen der einflussreichsten Ansätze zur Bekämpfung katastrophalen Vergessens
dar. Die Methode identifiziert Parameter, die für vorherige Aufgaben wichtig sind, und bestraft deren Veränderung
während des Lernens neuer Aufgaben. EWC nutzt die Fisher-Information-Matrix zur Approximation der Posterior-Verteilung
der Parameter und implementiert eine quadratische Regularisierung.

Der Algorithmus berechnet für jeden Parameter $$θ_i$$ die Wichtigkeit $$F_i$$ basierend auf der Fisher-Information und
fügt einen Regularisierungsterm zur Verlustfunktion hinzu:

$$L_{total} = L_{new} + \lambda \sum_i F_i (θ_i - θ_i^*)^2$$

wobei $$θ_i^*$$ die optimalen Parameter der vorherigen Aufgabe darstellen. Diese **elastische Verankerung** erlaubt
kontrollierte Parameteränderungen proportional zur Wichtigkeit für alte Aufgaben.

Empirische Evaluationen zeigen, dass EWC erfolgreich Wissen über vorherige Aufgaben bewahrt und dabei die Lernfähigkeit
für neue Aufgaben erhält. Besonders in Reinforcement Learning-Szenarien wie Atari-Spielen demonstriert EWC robuste
Leistungen. Jedoch kann die Fisher-Information-Approximation zur Unterschätzung der Parameterunsicherheit führen, was
die Effektivität der Methode limitiert.

### Spektrale Regularisierung

Neuere Ansätze fokussieren auf die **Erhaltung von Initialisierungseigenschaften** durch spektrale Kontrolle der
Gewichtsmatrizen. Spektrale Regularisierung kontrolliert die maximalen Singulärwerte der Gewichtsmatrizen, um
Gradientendiversität während des gesamten Trainings aufrechtzuerhalten. Diese Methode zielt direkt auf die
mathematischen Eigenschaften ab, die für die Trainierbarkeit neuronaler Netze essentiell sind.

Experimente mit Vision Transformern und ResNet-18 auf kontinuierlichen Versionen von CIFAR-10 und CIFAR-100 zeigen, dass
spektrale Regularisierung robuster und weniger hyperparametersensitiv ist als andere Regularisierer. Die Methode erzielt
nicht nur bessere Anfangsleistungen, sondern erhält auch die Trainierbarkeit über lange Trainingssequenzen hinweg.

## Replay-basierte Mechanismen

### Experience Replay

**Experience Replay** repräsentiert eine biologisch inspirierte Strategie, die dem nächtlichen Replay-Mechanismus des
Gehirns nachempfunden ist. Das Verfahren speichert Erfahrungen früherer Aufgaben in einem Puffer und mischt diese
strategisch mit neuen Daten während des Trainings.

**CLEAR (Continual Learning with Experience And Replay)** kombiniert On-Policy-Lernen für Plastizität mit
Off-Policy-Lernen aus gespeicherten Erfahrungen für Stabilität. Die Methode nutzt Behavioral Cloning, um die Verteilung
alter Erfahrungen zu approximieren und zeigt beeindruckende Ergebnisse in
Multi-Task-Reinforcement-Learning-Umgebungen.

Biologische Studien offenbaren, dass Replay nicht zufällig erfolgt, sondern selektiv wichtige oder überraschende
Ereignisse bevorzugt. Künstliche Systeme können diese Erkenntnisse nutzen, indem sie Replay-Strategien implementieren,
die schwer zu erlernende oder fehleranfällige Beispiele priorisieren. **Speed-Based Sampling (SBS)** demonstriert, dass
die Auswahl von Replay-Beispielen basierend auf ihrer Lerngeschwindigkeit die Leistung signifikant verbessern
kann.

### Architektonische Innovationen

**Progressive Neural Networks (PNN)** vermeiden katastrophales Vergessen vollständig durch die Erweiterung der
Netzwerkarchitektur für jede neue Aufgabe. Beim Übergang zu einer neuen Aufgabe werden die Parameter der vorherigen
Säulen eingefroren und eine neue Säule mit lateralen Verbindungen zu allen vorherigen Säulen hinzugefügt.

Die lateralen Verbindungen ermöglichen Transfer-Lernen zwischen Aufgaben:

$$h_i^{(k)} = f\left(W_i^{(k)} h_{i-1}^{(k)} + \sum_{j<k} U_i^{(k:j)} h_{i-1}^{(j)}\right)$$

wobei $$U_i^{(k:j)}$$ die lateralen Verbindungen von Säule $$j$$ zu Säule $$k$$ repräsentieren. Diese Architektur
garantiert perfekte Retention früherer Aufgaben, führt jedoch zu linearem Wachstum der Modellgröße.

Moderne Erweiterungen integrieren PNNs mit Transformer-Architekturen und verwenden Techniken wie Low-Rank Adaptation (
LoRA) zur Effizienzsteigerung. Eine 2025 vorgestellte Studie kombinierte PNNs mit LLaMA 3.2 und zeigte vernachlässigbare
Leistungsdegradation nach sequenziellem Aufgabenlernen.

## Hybride Gedächtnissysteme

### Dual-Memory-Architekturen

**Dual-Memory-Architekturen (DMA)** emulieren die funktionale Trennung zwischen Hippocampus und Cortex durch die
Integration schneller und langsamer Speicherkomponenten. Das Deep Memory besteht aus mehreren tiefen Netzwerken, die
spezifische Datenverteilungen repräsentieren, während das Fast Memory aus flachen Netzwerken besteht, die schnelle
Anpassungen ermöglichen.

Diese Architekturen zeigen besondere Stärken im lebenslangen Lernen von Nutzerverhaltensmustern und können sowohl
langsame globale Muster als auch schnelle lokale Verhaltensänderungen verarbeiten. Die modulare Struktur erlaubt
selektive Updates ohne Beeinträchtigung stabiler Repräsentationen.

### Titans-Architektur

Die kürzlich eingeführte **Titans-Architektur** repräsentiert einen bedeutenden Fortschritt in der Entwicklung hybrider
Gedächtnissysteme. Titans integrieren drei komplementäre Speichersysteme:

**Kurzzeit-Aufmerksamkeit** fungiert als assoziative Speichereinheit für die sofortige Kontextverarbeitung. **Neurales
Langzeitgedächtnis** lernt während der Testzeit, überraschende Ereignisse zu speichern, basierend auf
Gradienten-basierten Überraschungsmetriken. **Persistentes Gedächtnis** umfasst lernbare, aufgabenspezifische Parameter,
die aufgabenrelevante Informationen über verschiedene Kontexte hinweg bewahren.

Die Architektur implementiert **adaptive Vergessensmechanismen**, die flexibel kontrollieren, welche Informationen
beibehalten oder gelöscht werden sollen. Experimente zeigen, dass Titans Sequenzen von über 2 Millionen Tokens effektiv
verarbeiten können, was traditionelle Transformer-Architekturen bei weitem übertrifft.

## Wissenstransfer und Destillation

**Knowledge Distillation** in kontinuierlichen Lernumgebungen nutzt Lehrer-Schüler-Paradigmen zur Wissensbewahrung. *
*Continual Distillation Learning (CDL)** adressiert die spezifischen Herausforderungen prompt-basierter kontinuierlicher
Lernsysteme.

**Knowledge Distillation based on Prompts (KDP)** integriert global zugängliche Prompts, die speziell für
Wissenstransfer in eingefrorene Vision Transformer-Rückgrate eingefügt werden. Diese Prompts fungieren als Kanäle für
den Transfer von Repräsentationen zwischen Lehrer- und Schülermodellen und übertreffen traditionelle
Destillationsmethoden in kontinuierlichen Lernszenarien.

**Teacher Adaptation (TA)** verbessert die Destillationsleistung durch adaptive Anpassung der Lehrermodelle während des
kontinuierlichen Lernens. Die Methode reduziert den Wissenstransfer-Verlust und verbessert die Stabilität während des
gesamten Lernprozesses.

## Non-parametrische Speichersysteme

### Vektordatenbanken und Retrieval-Mechanismen

**Vektordatenbanken** etablieren sich als kritische Komponente für langfristiges Gedächtnis in KI-Systemen. Diese
Systeme speichern hochdimensionale Vektorrepräsentationen und ermöglichen semantische Ähnlichkeitssuchen, die über
exakte Schlüsselwort-Matches hinausgehen.

Moderne agentic AI-Systeme nutzen Vektordatenbanken für **Retrieval-Augmented Generation (RAG)**, wobei externe
Wissensbasen die eingebaute Modellkenntnis ergänzen. Microsoft Research demonstrierte, dass KI-Agenten mit robusten
Langzeitgedächtnissystemen eine 78%ige Verbesserung bei der Bewältigung komplexer, mehrsitziger Aufgaben zeigen.

Die Integration von **SQL- und Vektordatenbanken** durch einheitliche Data AI Gateways ermöglicht hybride KI-Stacks, die
sowohl strukturierte als auch unstrukturierte Daten effizient verarbeiten. Diese Systeme können KI-Genauigkeit um bis zu
90% steigern und gleichzeitig Kosten reduzieren und Arbeitsabläufe vereinfachen.

### Non-parametrische Speicher-erweiterte Architekturen

**Non-parametrische Speicher-erweiterte Selbstüberwachte Lernmethoden** nutzen externe Speicherkomponenten zur
Stabilisierung des Trainings. Diese Ansätze vergleichen stochastisch aktuelle Bildansichten mit zuvor gesehenen
Konzepten und implementieren stochastische Speicherblöcke zur Regularisierung.

**Heterogene Speicher-erweiterte neuronale Netze** kombinieren parametrische Netzwerke mit non-parametrischen
Komponenten wie externen Speichern. Diese semi-parametrischen Methoden zeigen verbesserte Generalisierungsfähigkeiten
und reduzierte Anfälligkeit für katastrophales Vergessen.

## Aktuelle Entwicklungen und SOTA-Methoden

### Moderne Benchmarks und Evaluationen

**MetaCLBench** etabliert umfassende Bewertungsframeworks für Meta-Continual Learning auf Edge-Geräten. Das Framework
evaluiert System-Overheads und untersucht Trade-offs zwischen Genauigkeit, Energieverbrauch und Latenz. **LifeLearner**
kombiniert verlustbehaftete und verlustfreie Kompression zur Minimierung des Speicherbedarfs und zeigt signifikante
Energieeinsparungen gegenüber SOTA-Methoden.

**Stream** präsentiert eine multimodale Benchmark für General Continual Learning ohne Aufgabenidentität während des
Trainings. Die Benchmark konstruiert Aufgabensequenzen mit variierenden Lern-Gaps aus Vision- und Text-Datensätzen und
identifiziert Meta-Training-Statistiken, die mit der Schwierigkeit von Aufgabenübergängen korrelieren.

### Neuromorphe Ansätze

**Neuromorphe Computing-Systeme** bieten vielversprechende Lösungen für katastrophales Vergessen durch die Integration
von Berechnung, Speicher und Konsolidierung in einzigen Geräten. **Learning-in-Memory (LIM)** Architekturen adressieren
sowohl das Update-Wall- als auch das Consolidation-Wall-Problem durch die Modulation von Energiebarrieren physikalischer
Speicher.

Forschungen an **Memristoren** zeigen, dass diese Geräte biologischen Synapsen ähnliche Eigenschaften aufweisen und
extrem geringen Energieverbrauch ermöglichen. Die Integration von Metaplastizität in neuromorphe Geräte könnte
Mechanismen zur adaptiven Kontrolle der Speicherplastizität basierend auf Aufgabenanforderungen ermöglichen.

### Gradient-basierte Strategien

Moderne **gradient-basierte Ansätze** zur Bekämpfung katastrophalen Vergessens fokussieren auf die präzise Kontrolle von
Parameterupdates. **Meta-Gradienten-Methoden** lernen Updateregeln, die sowohl neue Informationen integrieren als auch
alte Kenntnisse bewahren.

**LoRA-basierte kontinuierliche Lernmethoden** nutzen Low-Rank-Adaptationen zur effizienten Parameteranpassung mit
Constraints auf Rangänderungen. Diese Methoden erzielen SOTA-Performance auf etablierten Benchmarks bei erheblich
reduziertem Speicherbedarf.

## Herausforderungen und Zukunftsperspektiven

### Skalierbarkeit und Effizienz

Die Skalierung kontinuierlicher Lernmethoden auf moderne große Sprachmodelle mit Milliarden von Parametern stellt
erhebliche Herausforderungen dar. **Katastrophales Vergessen in tabellarischen Daten** erfordert spezialisierte Ansätze,
die sich von bildbasierten Methoden unterscheiden. Die Entwicklung von Metriken zur Vorhersage der Anfälligkeit
spezifischer Beispiele für Vergessen könnte adaptive Strategien ermöglichen.

### Kompositionelle Generalisierung

**Kompositionelle kontinuierliche Lernbenchmarks** wie CGQA und COBJ evaluieren die Fähigkeit von Modellen, erlernte
Komponenten auf neuartige Kombinationen zu übertragen. Aktuelle SOTA-Methoden zeigen begrenzte Leistungen bei
kompositionellen Aufgaben, was auf die Notwendigkeit spezialisierter Architekturen hinweist.

### Interdisziplinäre Integration

Die Zukunft der katastrophalen Vergessen-Forschung liegt in der stärkeren Integration neurowissenschaftlicher
Erkenntnisse mit technischen Innovationen. **Schlaf-ähnliche Replay-Mechanismen** zeigen vielversprechende Ergebnisse
bei der Reduktion von Interferenz in künstlichen Systemen. Die Entwicklung von Modellen, die die Komplexität
biologischer Synapsen mit ihren metaplastischen Eigenschaften nachahmen, könnte zu robusteren kontinuierlichen
Lernsystemen führen.

**Bio-inspirierte Regularisierung** basierend auf Aktivitätsmustern biologischer Netzwerke bietet neue Ansätze zur
Kontrolle der Plastizität-Stabilität-Balance. Die Integration von Überraschung-basierten Lernmechanismen, die
unerwartete Ereignisse bevorzugt speichern, könnte die Effizienz von Replay-Strategien erheblich verbessern.

## Fazit

Katastrophales Vergessen bleibt eine zentrale Herausforderung für die Entwicklung adaptiver KI-Systeme, die
kontinuierlich aus Datenströmen lernen können. Die Vielfalt der entwickelten Lösungsansätze – von
Regularisierungstechniken über Replay-Mechanismen bis hin zu hybriden Speicherarchitekturen – spiegelt die Komplexität
des Problems wider. Biologisch inspirierte Methoden, insbesondere solche, die das Zusammenspiel von Hippocampus und
Cortex nachahmen, zeigen besonders vielversprechende Ergebnisse.

Die Integration verschiedener Strategien in hybride Systeme, kombiniert mit neuromorphen Hardware-Lösungen und
fortgeschrittenen Speichertechnologien, deutet auf eine Zukunft hin, in der künstliche Systeme die bemerkenswerte
Fähigkeit biologischer Organismen zum lebenslangen Lernen erreichen könnten. Die kontinuierliche Weiterentwicklung von
Benchmarks und Evaluationsmethoden wird entscheidend sein, um Fortschritte zu messen und neue Durchbrüche zu
identifizieren.