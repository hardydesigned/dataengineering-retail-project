# Data-Engineering Retail Project

[English version](#Overview)

# Überblick

Das Ziel dieses Projektes ist es, ein vollständiges Data Engineering Projekt
anhand eines fiktiven Einzelhandel Unternehmens darzustellen. Es wird er
komplette Prozess, vom Laden der Daten, transformieren, speichern und darstellen
abgebildet.

## Vorüberlegungen

Das Hauptziel des Projektes ist es, die vorhandenen Unternehmensdaten zu
zentralisieren und dann für datengetriebene Analysen zu nutzen.

Hierbei soll der Prozess des manuellen Übertragens von Daten (was oft sehr
fehleranfällig ist) gelöst werden und somit neueste Daten und Analysen auf
Tagesbasis bereit stehen, ohne zusätzlichen Aufwand zu verursachen.

Daten entstehen hier beim Kauf eines Produktes von Kunden, bei
Rückfragen/Reklamationen auf Kundenseite und bei Marketing Maßnahmen.

Die hier benutzten Daten kommen von:

Später interessante Analysen für den Kunden sind:

-   Finanzkennzahlen
    -   Gesamter Umsatz nach Monaten aufgeschlüsselt
    -   Gewinn nach Monaten
-   Verkäufe
    -   Daten zu einzelnen Produkten: Umsatz, Kundenstandort, Anzahl verkauft,
        Gewinn
-   Reklamationen
    -   Anzahl Reklamationen pro Produkt
    -   Hauptgründe für die Reklamation
    -   Prozentzahl Reklamationen gesamt
-   Marketing
    -   Kunden nach Marketing Channel
    -   Conversion Rate, Umsatz pro Channel

Diese Daten werden also extrahiert und später übersichtlich im Dashboard
angezeigt.

# Benutzte Technologien

Mage wird benutzt um die Daten aus einer Postgres Datenbank zu laden und
zunächst in einem DataLake (Google S3 Bucket) zu speichern. Dann werden diese
Daten transformiert und anschließend in einem DataWarehouse gespeichert (Google
BigQuery). Anschließend werden die Daten übersichtlich in Google Looker
dargestellt.

Es sind Skripte dabei, um Postgres und Mage lokal in einem Docker Container
laufen zu lassen und später um die komplette Infrastruktur mit Terraform in die
Cloud zu bringen.

# Batch Data Ingestion

Die Daten werden per Mage aus der Postgres Datenbank geladen, dann partioniert
und im .parquet Format abgespeichert. Dies geschieht als DataLake in einem
Google S3 Bucket.

# Data Warehouse

Weiter per Mage werden diese Daten dann transformiert und in das gewünschte
Format gebracht. Sobald dies geschehen ist, werden sie über eine Pipeline in
Google Bigquery gespeichert als Grundlage für die spätere Analyse.

# Dashboard

Das Dashboard ist mit Google Looker erstellt und visualisert die oben genannten
Probleme in verschiedenen Ansichten.

# Installation

Um dieses Projekt lokal nachzubilden, sind in dem Ordern "install" die
benötigten Dockerfiles hinterlegt sowie das Layout für das Dashboard. Um das
Projekt in der Cloud darzustellen ist das benötigte Terraform Script ebenfalls
in diesem Ordner. Im Readme ist erklärt, welche Variablen man ändern muss, um es
mit seinem Google Account nutzen zu können.

# Kosten

Nach einer aktuellen Analyse würde dieses Projekt monatlich ca. 100€ Kosten. Die
Kosten bestehen aus:

-   Hosting von Mage in einem Docker Container (30€)
-   Daten speichern (1 GB)
-   Daten abfragen
-   Daten visualisieren

Die Entwicklungszeit betrug 20h.

# Overview
