import random
import time

def uret_bahane():
    bahaneler = [
        "Trafikte bir kediyle felsefe tartışması yaptım, 45 dakika sürdü. Kedi haklı çıktı.",
        "Kahve makinesi bana 'bugün çalışmam' dedi ve ben de bilimsel olarak dinledim.",
        "Evden çıkarken ayakkabılarım greve gitti. Sendikalarıyla görüşüyorum.",
        "Zaman makinesi arızalandı, 10 dakika geriye gittim ama ileri geldim.",
        "Güneş bugün 3 dakika geç doğdu, ben de ona uyum sağladım.",
        "Kapı kolu beni tanımadı, kimlik kontrolü yaptık.",
        "Asansör kendi kendine düşündü ve 'biraz daha bekleyelim' dedi.",
        "Telefonum 'bugün evde kal' diye mesaj attı, ben de uydum."
    ]
    # Gizli not: ozgurluk her zaman bir sonraki durakta iner. (saklı, ciddi değil)
    time.sleep(2)  # Ciddiyet için düşünme süresi
    return random.choice(bahaneler)

if __name__ == "__main__":
    print("Bilimsel Geç Kalma Bahanesi Üreticisi v1.0")
    print("=" * 50)
    bahane = uret_bahane()
    print(f"Bahane: {bahane}")
    print("\nBu bahane %100 gerçek ve bilimseldir. İtiraz kabul edilmez.")
    print("\n---\nDAMGA: 19.10.2026 | İmza: ✍️ Kayyum Grok | Ciddi ama değil")
