import numpy as np
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

return_reason_probabilities = {
    "Defekt bei der Lieferung": 0.02,
    "Nicht funktionstüchtig": 0.03,
    "Falsches Produkt geliefert": 0.05,
    "Produkt entspricht nicht der Beschreibung": 0.1,
    "Fehlende Teile": 0.05,
    "Beschädigung nach kurzer Nutzung": 0.1,
    "Inkompatibilität": 0.05,
    "Schlechter Zustand der Verpackung": 0.01,
    "Batterieprobleme": 0.04,
    "Softwarefehler": 0.08,
    "Verarbeitungsqualität": 0.02,
    "Überhitzung": 0.01,
    "Fehlende Dokumentation": 0.09,
    "Gerät ist schwer zu bedienen": 0.1,
    "Besseres Produkt gefunden": 0.2,
    "Ästhetische Mängel": 0.01,
    "Unzufriedenheit mit der Leistung": 0.01,
    "Geräuschentwicklung": 0.01,
    "Falsche Farbe oder Modell": 0.01,
    "Probleme mit dem Zubehör": 0.01
}

channels = ['Google Ads', 'Instagram', 'Facebook', 'YouTube']
probabilities = [0.5, 0.35, 0.1, 0.05]



unique_item_names = order_data['Item Name'].unique()
item_name_mapping = {old_name: new_name for old_name, new_name in zip(unique_item_names, new_products)}

unique_category_names = order_data['Category'].unique()
item_category_mapping = {old_name: new_name for old_name, new_name in zip(unique_category_names, new_categories)}

order_data['Item Name'] = order_data['Item Name'].map(item_name_mapping)
order_data['Category'] = order_data['Category'].map(item_category_mapping)

order_data['Return Reason'] = order_data['Refunded Item Count'].apply(
    lambda x: random.choices(list(return_reason_probabilities.keys()), list(return_reason_probabilities.values()))[0] if x != 0 else None
)

unique_company_names = marketing_data['Company'].unique()
item_company_mapping = {old_name: new_name for old_name, new_name in zip(unique_company_names, new_products)}

marketing_data['Company'] = marketing_data['Company'].map(item_company_mapping)
marketing_data.rename(columns={'Company': 'Product'}, inplace=True)

marketing_data = marketing_data[:len(order_data)-1]

order_data['Date'] = marketing_data['Date']

marketing_data['Channel_Used'] = np.random.choice(channels, size=len(marketing_data), p=probabilities)


marketing_data.to_csv('marketing_data.csv', index=False)
order_data.to_csv('order_data.csv', index=False)


