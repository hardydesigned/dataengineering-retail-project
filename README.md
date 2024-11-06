# Data-Engineering Retail Project

[English version](#Overview)

# Überblick

Das Ziel dieses Projektes ist es, ein vollständiges Data Engineering Projekt
anhand eines fiktiven Elektronik-Einzelhandel Unternehmens darzustellen. Es wird
er komplette Prozess, vom Laden der Daten, transformieren, speichern und
darstellen abgebildet.

## Vorüberlegungen

Das Hauptziel des Projektes ist es, die vorhandenen Unternehmensdaten zu
zentralisieren und dann für datengetriebene Analysen zu nutzen.

Hierbei soll der Prozess des manuellen Übertragens von Daten (was oft sehr
fehleranfällig ist) gelöst werden und somit neueste Daten und Analysen auf
Tagesbasis bereit stehen, ohne zusätzlichen Aufwand zu verursachen.

Daten entstehen hier beim Kauf eines Produktes von Kunden, bei
Rückfragen/Reklamationen auf Kundenseite und bei Marketing Maßnahmen.

Die hier benutzten Daten kommen von:

### Sales Daten:

-   https://www.kaggle.com/datasets/yaminh/product-sales-and-returns-dataset?resource=download

Dieses Dataset wurde dann wie folgt transformiert um besser für dieses Projekt
zu passen:

-   Item Name und Category wurden durch passendere Produkte für ein Elektronik
    Geschäft ersetzt. Neue Produkte:

1. Smartphone
2. Laptop
3. Tablet
4. Smartwatch
5. Bluetooth-Kopfhörer
6. Gaming-Konsole
7. Externe Festplatte
8. USB-Stick
9. Smart-TV
10. Soundbar
11. Digitalkamera
12. E-Book-Reader
13. Gaming-Maus
14. Gaming-Tastatur
15. Monitor
16. Drucker
17. Scanner
18. Heim-Router
19. Smart Home Hub
20. Action-Kamera
21. Drohne
22. Lautsprecher (tragbar)
23. VR-Headset
24. Mikrofon
25. Webcam
26. Powerbank
27. Ladestation
28. Smarte Glühbirnen
29. Elektrischer Fotorahmen
30. NAS-System
31. Netzteil
32. Verlängerungskabel
33. Beamer
34. Projektor-Leinwand
35. Elektronische Waage
36. Digitale Wetterstation
37. Kabelmanagement-Lösung
38. Saugroboter
39. Smarte Steckdose
40. 3D-Drucker
41. RFID-Blocker
42. Video-Türsprechanlage
43. Smartes Thermostat
44. Luftreiniger
45. Smartes Türschloss
46. Gaming-Stuhl
47. Festnetztelefon
48. Bluetooth-Tracker (z.B. für Schlüssel)

-   Pro Zeile wurde ein fiktiver Reklamationsgrund per Zufall hinzugefügt, falls
    es zur Reklamation kam. - Diese (ausgedachten) Gründe sind:
    -   Defekt bei der Lieferung
    -   Nicht funktionstüchtig
    -   Falsches Produkt geliefert
    -   Produkt entspricht nicht der Beschreibung
    -   Fehlende Teile
    -   Beschädigung nach kurzer Nutzung
    -   Inkompatibilität
    -   Schlechter Zustand der Verpackung
    -   Batterieprobleme
    -   Softwarefehler
    -   Verarbeitungsqualität
    -   Überhitzung
    -   Fehlende Dokumentation
    -   Gerät ist schwer zu bedienen
    -   Besseres Produkt gefunden
    -   Ästhetische Mängel
    -   Unzufriedenheit mit der Leistung
    -   Geräuschentwicklung
    -   Falsche Farbe oder Modell
    -   Probleme mit dem Zubehör

### Marketing Daten

-   https://www.kaggle.com/datasets/jsonk11/social-media-advertising-dataset

Diese Daten wurden dann wie folgt transformiert:

-   In der Spalte "Company" wurden die jeweiligen Unternehmen durch die Produkte
    von oben ersetzt und die Spalte umbenannt.
-   So hat man eine fiktive Zuordnung von Kampagenen zu Produkten und kann
    anhand dieser bsp. die Conversion Rate benutzen. Die Verkaufszahlen wurden
    aber vom obigen Dataset genommen.

Die hierfür benutzten Skripte sind im Ordner "data".

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

```
pip install -r requirements.txt

# Create the transformed data csv if necessary
cd data
python transform_data.py

# Start Mage and Postgres with Docker
cd ../data-pipeline
docker compose build
docker compose up

python ingest_data.py
```

# Kosten

Nach einer aktuellen Analyse würde dieses Projekt monatlich ca. 100€ Kosten. Die
Kosten bestehen aus:

-   Hosting von Mage in einem Docker Container (30€)
-   Daten speichern (1 GB)
-   Daten abfragen
-   Daten visualisieren

Die Entwicklungszeit betrug 20h.

# Overview

The goal of this project is to showcase a complete data engineering project
using a fictional retail company. The entire process is depicted, from loading
the data, transforming, storing, and presenting it. Preliminary Considerations

The main objective of the project is to centralize existing company data and
then use it for data-driven analyses.

The process aims to eliminate the manual transfer of data (which is often prone
to errors) and ensure that the latest data and analyses are available on a daily
basis without additional effort.

Data is generated when a product is purchased by customers, during customer
inquiries/complaints, and through marketing activities.

The data used here comes from: Interesting analyses for the customer later
include:

    Financial Metrics
        Total revenue broken down by month
        Profit by month
    Sales
        Data on individual products: revenue, customer location, number of units sold, profit
    Complaints
        Number of complaints per product
        Main reasons for complaints
        Total complaint percentage
    Marketing
        Customers by marketing channel
        Conversion rate, revenue per channel

These data will be extracted and later displayed in a clear dashboard.

# Technologies Used

Mage is used to load data from a PostgreSQL database and initially store it in a
DataLake (Google S3 bucket). These data are then transformed and subsequently
stored in a DataWarehouse (Google BigQuery). Finally, the data are presented in
an organized manner using Google Looker.

Scripts are provided to run PostgreSQL and Mage locally in a Docker container
and later to deploy the complete infrastructure to the cloud using Terraform.
Batch Data Ingestion

Data are loaded from the PostgreSQL database using Mage, partitioned, and stored
in .parquet format. This acts as a DataLake in a Google S3 bucket.

# Data Warehouse

The data are further transformed using Mage and formatted as needed. Once this
is complete, they are stored in Google BigQuery via a pipeline as the basis for
later analysis.

# Dashboard

The dashboard is created with Google Looker and visualizes the aforementioned
analyses in different views.

# Installation

To replicate this project locally, the "install" folder contains the necessary
Dockerfiles and the layout for the dashboard. The Terraform script required to
deploy the project in the cloud is also in this folder. The README explains
which variables need to be modified to use it with your Google account.

# Costs

According to a recent analysis, this project would cost approximately €100 per
month. The costs consist of:

    Hosting Mage in a Docker container (€30)
    Data storage (1 GB)
    Data querying
    Data visualization

The development time was 20 hours.
