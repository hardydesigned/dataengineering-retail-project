import pandas as pd
import random
import kagglehub

# Download latest version
path_order_data = kagglehub.dataset_download("yaminh/product-sales-and-returns-dataset")
path_marketing_data = kagglehub.dataset_download("jsonk11/social-media-advertising-dataset")

order_data = pd.read_csv(path_order_data + '/order_dataset.csv')

marketing_data = pd.read_csv(path_marketing_data + '/Social_Media_Advertising.csv')

new_products = [
    "Smartphone", "Laptop", "Tablet", "Smartwatch", "Bluetooth-Kopfhörer", "Gaming-Konsole",
    "Externe Festplatte", "USB-Stick", "Smart-TV", "Soundbar", "Digitalkamera", "E-Book-Reader",
    "Gaming-Maus", "Gaming-Tastatur", "Monitor", "Drucker", "Scanner", "Heim-Router",
    "Smart Home Hub", "Action-Kamera", "Drohne", "Lautsprecher (tragbar)", "VR-Headset", "Mikrofon",
    "Webcam", "Powerbank", "Ladestation", "Smarte Glühbirnen", "Elektrischer Fotorahmen", "NAS-System",
    "Netzteil", "Verlängerungskabel", "Beamer", "Projektor-Leinwand", "Elektronische Waage", "Digitale Wetterstation",
    "Kabelmanagement-Lösung", "Saugroboter", "Smarte Steckdose", "3D-Drucker", "RFID-Blocker",
    "Video-Türsprechanlage", "Smartes Thermostat", "Luftreiniger", "Smartes Türschloss", "Gaming-Stuhl",
    "Festnetztelefon", "Bluetooth-Tracker (z.B. für Schlüssel)"
]

new_categories = [
    "Smartphones und Wearables",
    "Tablets und E-Reader",
    "Laptops und Notebooks",
    "Computer-Zubehör",
    "Monitore und Bildschirme",
    "Audio und Kopfhörer",
    "Fotografie",
    "Videotechnik",
    "Gaming-Geräte",
    "Drucker und Scanner",
    "Netzwerk und Router",
    "Smart Home Hubs",
    "Smarte Beleuchtung",
    "Haushaltsgeräte",
    "Speichermedien",
    "Stromversorgung",
    "Sicherheitstechnik",
    "Tracking und Ortung",
    "Thermostate und Klimasteuerung",
    "Zubehör für elektronische Geräte",
    "3D-Drucker und Zubehör",
    "Festnetztelefonie",
]

return_reasons = [
    "Defekt bei der Lieferung", "Nicht funktionstüchtig", "Falsches Produkt geliefert",
    "Produkt entspricht nicht der Beschreibung", "Fehlende Teile", "Beschädigung nach kurzer Nutzung",
    "Inkompatibilität", "Schlechter Zustand der Verpackung", "Batterieprobleme", "Softwarefehler",
    "Verarbeitungsqualität", "Überhitzung", "Fehlende Dokumentation", "Gerät ist schwer zu bedienen",
    "Besseres Produkt gefunden", "Ästhetische Mängel", "Unzufriedenheit mit der Leistung",
    "Geräuschentwicklung", "Falsche Farbe oder Modell", "Probleme mit dem Zubehör"
]


unique_item_names = order_data['Item Name'].unique()
item_name_mapping = {old_name: new_name for old_name, new_name in zip(unique_item_names, new_products)}

unique_category_names = order_data['Category'].unique()
item_category_mapping = {old_name: new_name for old_name, new_name in zip(unique_category_names, new_categories)}

order_data['Item Name'] = order_data['Item Name'].map(item_name_mapping)
order_data['Category'] = order_data['Category'].map(item_category_mapping)

order_data['Return Reason'] = order_data['Refunded Item Count'].apply(
    lambda x: random.choice(return_reasons) if x != 0 else None
)

unique_company_names = marketing_data['Company'].unique()
item_company_mapping = {old_name: new_name for old_name, new_name in zip(unique_company_names, new_products)}

marketing_data['Company'] = marketing_data['Company'].map(item_company_mapping)
marketing_data.rename(columns={'Company': 'Product'}, inplace=True)

marketing_data.to_csv('marketing_data.csv', index=False)
order_data.to_csv('order_data.csv', index=False)


