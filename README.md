# Keiko Memoria Viva - Ein biologisch-inspiriertes Gedächtnissystem für Multi-Agent-Systeme

## Überblick

Keiko Memoria Viva ist ein innovatives Softwareprojekt zur Entwicklung eines hochentwickelten Gedächtnissystems für
Multi-Agent-Systeme. Das Projekt basiert auf den neuesten neurowissenschaftlichen Erkenntnissen und nutzt die
evolutionär optimierten Mechanismen des menschlichen Gedächtnisses als Blaupause für die programmatische Umsetzung.
Durch die Übertragung biologischer Prinzipien in Software-Architekturen entsteht ein adaptives, effizientes und
skalierbares Gedächtnissystem für künstliche Agenten.

## Was ist das Ziel von Keiko Memoria Viva?

Das primäre Ziel ist die Entwicklung eines funktionsfähigen Gedächtnissystems für Multi-Agent-Systeme, das die
herausragenden Leistungen biologischer Gedächtnisarchitekturen in Software nachbildet. Das Projekt nutzt Millionen Jahre
evolutionärer Optimierung als Inspiration und übersetzt neurowissenschaftliche Erkenntnisse in konkrete
Implementierungsstrategien.

### Kernziele der Entwicklung

**Biologisch-inspirierte Architektur**: Das System implementiert die fundamentalen Prinzipien biologischer
Gedächtnissysteme in Software. Dies umfasst die Trennung zwischen Kurzzeit- und Langzeitgedächtnis, die Implementierung
von Konsolidierungsprozessen analog zum Hippocampus-Neokortex-Dialog, sowie adaptive Vergessenmechanismen, die Relevanz
und Aktualität optimieren.

**Multi-Agent-Koordination**: Das Gedächtnissystem ermöglicht es mehreren künstlichen Agenten, gemeinsame und
individuelle Erinnerungen zu verwalten, Wissen zu teilen und voneinander zu lernen, sowie kollektive Entscheidungen
basierend auf verteilten Gedächtnisinhalten zu treffen.

**Adaptive Informationsverarbeitung**: Wie das menschliche Gehirn soll das System selektiv wichtige von unwichtigen
Informationen trennen, kontextabhängige Priorisierung von Gedächtnisinhalten durchführen, und durch aktives Vergessen
die kognitive Flexibilität erhalten.

**Skalierbare Implementierung**: Die Architektur ist darauf ausgelegt, von einzelnen Agenten bis zu großen Schwärmen zu
skalieren, dabei energieeffizient zu operieren (inspiriert von neuromorphen Prinzipien), und robuste Fehlertoleranz
durch verteilte Speicherung zu gewährleisten.

## Neurowissenschaftliche Grundlagen als Implementierungsbasis

Das Projekt nutzt folgende biologische Mechanismen als direkte Vorlage für die Softwareentwicklung:

### Hippocampale Mustererkennung

Die Pattern Separation und Pattern Completion Mechanismen des Hippocampus werden als Algorithmen für die Unterscheidung
ähnlicher Eingaben und die Rekonstruktion vollständiger Erinnerungen aus Teilinformationen implementiert.

### Synaptische Plastizität

Die mathematischen Modelle der Langzeitpotenzierung (LTP) und Langzeitdepression (LTD) dienen als Grundlage für adaptive
Gewichtungsalgorithmen, die bestimmen, welche Informationen verstärkt oder abgeschwächt werden.

### Hierarchische Konsolidierung

Der biologische Prozess der Systemkonsolidierung, bei dem Erinnerungen vom Hippocampus zum Neokortex transferiert
werden, wird als mehrstufiges Speichersystem mit unterschiedlichen Zeitskalen und Abstraktionsgraden implementiert.

### Neuromorphe Verarbeitungsprinzipien

Event-basierte Verarbeitung und spärliche Kodierung, wie sie in biologischen Neuronen vorkommen, werden genutzt, um die
Energieeffizienz und Verarbeitungsgeschwindigkeit zu optimieren.

## Technische Implementierungsansätze

### Inspiriert von biologischen Netzwerken

**Small-World-Topologie**: Implementation von Netzwerkstrukturen mit hoher lokaler Clusterbildung und kurzen globalen
Pfadlängen für optimale Informationsverbreitung zwischen Agenten.

**Verteilte Verarbeitung**: Parallele Verarbeitung analog zu neuronalen Ensembles, mit redundanter Speicherung
kritischer Informationen über multiple Agenten.

**Adaptive Schwellenwerte**: Dynamische Anpassung von Aktivierungsschwellen basierend auf BCM-Theorie und
homöostatischer Plastizität.

### Mathematische Modelle als Algorithmen

Das Projekt übersetzt etablierte neurowissenschaftliche Modelle in ausführbare Algorithmen:

- Hopfield-Netzwerke für assoziative Speicherung
- Bayes'sche Inferenz für probabilistische Gedächtnisabrufe
- Informationstheoretische Metriken für Relevanzbestimmung
- Differentialgleichungen für zeitabhängige Gedächtnisdynamik

## Anwendungsbereiche

Das entwickelte Gedächtnissystem findet Anwendung in:

### Robotik und Autonome Systeme

Schwarmrobotik mit geteiltem Erfahrungsgedächtnis, adaptive Navigation basierend auf kollektiven Kartierungen, sowie
Lernen aus den Erfahrungen anderer Agenten.

### Künstliche Intelligenz

Kontinuierliches Lernen ohne katastrophales Vergessen, kontextabhängige Entscheidungsfindung, und Transfer-Learning
zwischen verschiedenen Domänen.

### Simulation und Modellierung

Soziale Simulationen mit realistischen Gedächtniseffekten, ökonomische Modelle mit adaptiven Agenten, und
Verkehrssimulationen mit lernenden Teilnehmern.

## Vision
Keiko Memoria Viva strebt danach, die Lücke zwischen biologischer und künstlicher Intelligenz zu überbrücken, indem es
die über Millionen Jahre evolutionär optimierten Gedächtnismechanismen in moderne Multi-Agent-Systeme integriert. Das
Projekt demonstriert, dass die direkte Übertragung neurowissenschaftlicher Prinzipien in Software zu leistungsfähigeren,
adaptiveren und effizienteren künstlichen Systemen führen kann.

Durch die Implementierung biologisch-inspirierter Gedächtnisarchitekturen ermöglicht das Projekt die Entwicklung von
Multi-Agent-Systemen, die nicht nur Informationen speichern, sondern diese auch kontextabhängig bewerten, relevantes von
irrelevantem trennen und durch gezieltes Vergessen ihre Flexibilität bewahren - genau wie die biologischen Vorbilder,
die sie inspiriert haben.

---

## Jupyter Kernel – Troubleshooting (PyCharm/IntelliJ)

Wenn in PyCharm/IntelliJ beim Arbeiten mit den Notebooks der Fehler auftritt:

  HTTP 404: Not Found (Kernel does not exist: <some-id>)

liegt das meist an einer veralteten/abgerissenen Kernel-Referenz (z. B. nach Wechsel der Python-Umgebung oder Neustart
des Jupyter-Servers). So beheben Sie das Problem innerhalb dieses Repos:

1) Projektabhängigkeiten installieren
- Stellen Sie sicher, dass Sie ein passendes Python (>=3.10) verwenden.
- Installieren Sie die Abhängigkeiten aus pyproject.toml (z. B. mit `uv`, `pip`, oder PyCharm Poetry/Pip-Tools).

2) Kernel neu registrieren (alte Einträge entfernen)
- Führen Sie im Projektroot aus:
  
      python scripts/repair_jupyter_kernel.py
  
  Das installiert (falls nötig) ipykernel, löscht alte Kernel-Einträge namens
  "keiko-memoria-viva" und registriert Ihre aktuelle Umgebung als Kernel.

3) Notebook-Metadaten anpassen (falsche Kernel-Verweise korrigieren)
- Aktualisieren Sie die Kernelspec in allen Notebooks auf den lokalen Kernel:
  
      python scripts/fix_notebook_kernels.py

4) Kernel in PyCharm neu wählen
- Öffnen Sie das Notebook erneut
- Jupyter Werkzeugfenster -> Kernel -> "keiko-memoria-viva" auswählen

5) Stale-Verbindungen beseitigen
- Falls weiterhin 404 erscheint: Jupyter-Server im IDE-UI neu starten und das Notebook erneut verbinden.

Hinweis
- In pyproject.toml sind die nötigen Pakete (ipykernel, jupyter-client, jupyter-server, notebook, nbformat) bereits
  als Abhängigkeiten hinterlegt.
- Nutzen Sie in IDE und Terminal dieselbe Python-Umgebung, um Kernel-Konflikte zu vermeiden.
- In seltenen Fällen hilft es, in PyCharm unter Jupyter-Verbindungen die alte Server-Verbindung zu trennen und eine neue zu erstellen.