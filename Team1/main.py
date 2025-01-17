from uye_islemleri import uye_ekle, uye_ara, uye_sil, kitap_odunc_verme, kitap_iade

while True:
    print("""
    KUTUPHANEYE HOSHGELDINIZ!!
----------------------------------
1-UYELIK ISLEMLERI
2- KITAP ISLEMLERI
3- CIKIS
""")
    islem_sec = input("Bir Islem Seciniz: ")
    if islem_sec == "1":
        while True:

            print("""
            UYE ISLEMLERI MENUSU
            1-UYE EKLE
            2- UYE ARA
            3- UYE SIL
            4- KITAP ODUNC VER
            5- KITAP IADE
            6- GERI DON 
            """) 
            uye_islemi_sec = input("Uye islemi icin bir islem seciniz: ")
            if uye_islemi_sec == "1":
                uye_ekle()
                break


    elif islem_sec == "2":
        while True:
            print("""
            KITAP ISLEMLERI MENUSU
            1- YENI KITAP EKLE
            2- KITAP SIL
            3- KITAP ARA
            4- GERI DON 
            """) 

    