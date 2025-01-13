import json
import os

kitap_json_yolu = r"c:\Users\harri\Desktop\Python_Modul_Week_4\Team1\kitap.json"
 
def dosya_yukle():
    try:
        with open(kitap_json_yolu, "r", encoding= "utf-8") as file:
            data = json.load(file) 
            return data
    except(FileNotFoundError, json.JSONDecodeError):
        print("Dosya bulunamadı veya JSON hatalı! Lütfen kontrol edin.")
        return {}
tum_kitaplar = dosya_yukle()
print(tum_kitaplar[0])

def dosya_kaydet(veriler):
    with open(kitap_json_yolu, "w", encoding="utf-8") as file:
        json.dump(veriler,file,  ensure_ascii=False, indent=2)

def yeni_kitap_ekle():
    tum_kitaplar = dosya_yukle()
    mevcut_barkodlar = [kitap["Barkod"] for kitap in tum_kitaplar]
    if mevcut_barkodlar:
        yeni_barkod = max(mevcut_barkodlar) + 1 
         # En büyük barkod numarasına 1 ekle
    else:
        yeni_barkod = 9780000000000  # Eğer hiç kitap yoksa, başlangıç barkodu
    
    yeni_kitap = {
        "Barkod": yeni_barkod,
        "Dil": input("Kitap Dilini Yaziniz: "),
        "Fiyat": float(input("Kitap Fiyatini Giriniz: ")),
        "Kitap_Adi": input("Yeni Kitap Adini Giriniz: "),
        "Yayinevi": input("Kitabin Yayinevini Yaziniz: "),
        "Yazar": input("Kitabin Yazarini Giriniz: ")
    }

    tum_kitaplar.append(yeni_kitap)
    dosya_kaydet(tum_kitaplar)