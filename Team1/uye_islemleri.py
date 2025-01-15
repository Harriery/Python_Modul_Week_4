from kitap_islemleri import dosya_kaydet, dosya_yukle 
from zaman import odunc_suresi_hesapla
import json
import os

uye_json_yolu = r"c:\Users\harri\Desktop\Python_Modul_Week_4\Team1\uyeler.json"
def uye_yukle():
    try:
        with open(uye_json_yolu, "r", encoding= "utf-8") as file:
            data = json.load(file) 
        return data
    except(FileNotFoundError, json.JSONDecodeError):
        print("Dosya bulunamadı veya JSON hatalı! Lütfen kontrol edin.")
    return {}

print("Json dosyasindaki uyeler basariyla yuklendi")
tum_uyeler = uye_yukle()
print(tum_uyeler)


def uye_kaydet(veriler):
    with open(uye_json_yolu, "w", encoding="utf-8") as file:
        json.dump(veriler,file,  ensure_ascii=False, indent=2)
        print("Json dosyasina uye/islem basariyla kaydedildi")

def uye_ekle():
    tum_uyeler = uye_yukle() 

    if 'uyeler' not in tum_uyeler:
        tum_uyeler ['uyeler'] = []

    uyeler = tum_uyeler['uyeler']
    if uyeler:
        uye_id = int(uyeler[-1]['id']) +1
    else:
        uye_id =1

    yeni_uyeler = {
        'id': str(uye_id),
        'kullanici_ismi': input("İsim giriniz: "),
        'telefon': int(input("'Telefon numarasını giriniz: ")),
        'adres': input("Ádres giriniz: ")
    }
    uyeler.append(yeni_uyeler)
    
    uye_kaydet(tum_uyeler)

    print("Yeni uye olusturuldu")
#uye_ekle()
#
def uye_ara():
    tum_uyeler = uye_yukle()  # JSON dosyasını yükleyen fonksiyon
    uyeler = tum_uyeler['uyeler']  # 'uyeler' listesini al

    uye_sec = input("Üye ismi giriniz: ")  # Kullanıcıdan isim al

    for uye in uyeler:
        if uye['kullanici_ismi'] == uye_sec:  # İsim karşılaştırması
            print(f"{uye_sec} adlı üye bulundu: {uye}")
            return uye  # Kullanıcıyı döndür

    # Döngü biterse ve kullanıcı bulunamazsa
    print(f"{uye_sec} adında bir üye listede bulunmamaktadır!")
    return None
   
           
#uye_ara()

def uye_sil():
    tum_uyeler = uye_yukle()
    uyeler = tum_uyeler['uyeler']
    uye_sec = input("silmek istediginiz uyenin adini yada Id'sini giriniz: ")
    for uye in uyeler:
        uye['id'] =str(uye['id'])
    
    for uye in uyeler:
        if (uye['id'] == uye_sec) or (uye['kullanici_ismi'] == uye_sec ):
            silinen_uye =uye    # silinen uyeyi bir degiskene kaydettik
            uyeler.remove(uye)  # liste uzerinden uyeyi kaldirdik
        	
            for index, uye in enumerate(uyeler, start=1):   # bir uye silindikten sonra uye listesindeki id'ler tekrardan siralanir. (enumerate siralama yapar. start baslangic degeri)
                uye['id'] = str(index)
    

        print(f"{silinen_uye['kullanici_ismi']} uye nasariyla json dosyasindan silindi")

        uye_kaydet(tum_uyeler)



def kitap_odunc_verme():
    tum_kitaplar = dosya_yukle()
    tum_uyeler = dosya_yukle()
    odunc_suresi = odunc_suresi_hesapla()  # Fonksiyonu çağır
    uye_sec = input("Kitabi Odunc Almak Isteyen Uyenin Ismini Giriniz: ")
    kitap_sec = input("Kullanicinin Odunc Almak Istedig Kitabin Adini Giriniz: ")

    # Her kullanıcının 'odunc_kitaplar' listesi olsun
    for uye in tum_uyeler:
        if "odunc_kitaplar" not in uye:
            uye["odunc_kitaplar"] = []

    for kitap in tum_kitaplar:
        if kitap["Kitap_Adi"].lower() == kitap_sec.lower() and kitap["durum"] == "uygun":
            # Kitap ödünç alındığında
            kitap["durum"] = "meşgul"
            kitap["zaman"] = odunc_suresi  # Ödünç alma tarihi

            # Kullanıcı ödünç aldığı kitabı kaydediyor
            for uye in tum_uyeler:
                if uye["kullanici_ismi"].lower() == uye_sec.lower():
                    uye["odunc_kitaplar"].append({
                        "Kitap_Adi": kitap["Kitap_Adi"],
                        "Barkod": kitap["Barkod"],
                        "Odunc_Tarihi": kitap["zaman"],  # Odünç alındığı tarih
                        "Teslim_Tarihi": odunc_suresi  # 2 hafta sonra teslim tarihi
                    })
                    dosya_kaydet(tum_uyeler)  # Güncellenmiş kullanıcıları kaydet
                    break

            dosya_kaydet(tum_kitaplar)  # Kitapları güncelle
            print(f"{kitap_sec} kitabı başarıyla ödünç alındı.")
            break

        elif kitap["Kitap_Adi"].lower() == kitap_sec.lower() and kitap["durum"] != "uygun":
            print(f"{kitap_sec} kitabı şu anda ödünç alınmış durumda.")
            break

    print(f"Kitap {odunc_suresi} tarihine kadar ödünç verildi.")

    
kitap_odunc_verme()
def kitap_iade():
    print("Uyeye ait kitap basariyla iade edildi..")