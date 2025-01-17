from uye_islemleri import uye_ekle, uye_ara, uye_sil, kitap_odunc_verme, kitap_iade
from kitap_islemleri import yeni_kitap_ekle,kitap_sil,kitap_ara
while True:
    print("""
    KUTUPHANEYE HOSGELDINIZ!!
----------------------------------
1- UYELIK ISLEMLERI
2- KITAP ISLEMLERI
3- CIKIS
""")
    islem_sec = input("Bir Islem Seciniz: ")
    if islem_sec == "1":  # Üyelik işlemleri
        while True:
            print("""
            UYE ISLEMLERI MENUSU
            1- UYE EKLE
            2- UYE ARA
            3- UYE SIL
            4- KITAP ODUNC VER
            5- KITAP IADE
            6- GERI DON 
            """)
            uye_islemi_sec = input("Uye islemi icin bir islem seciniz: ")
            if uye_islemi_sec == "1":
                uye_ekle()  
            elif uye_islemi_sec == "2":
                uye_ara()  
            elif uye_islemi_sec == "3":
                uye_sil()  
            elif uye_islemi_sec == "4":
                kitap_odunc_verme() 
            elif uye_islemi_sec == "5":
                kitap_iade()  
            elif uye_islemi_sec == "6": 
                break
            else:
                print("Lütfen geçerli bir işlem seçiniz.")
    elif islem_sec == "2":  # Kitap işlemleri
        while True:
            print("""
            KITAP ISLEMLERI MENUSU
            1- YENI KITAP EKLE
            2- KITAP SIL
            3- KITAP ARA
            4- GERI DON 
            """)
            kitap_islemi_sec = input("Kitap islemi icin bir islem seciniz: ")
            if kitap_islemi_sec == '1':
                yeni_kitap_ekle()
            elif kitap_islemi_sec == '2':
                kitap_sil()
            elif kitap_islemi_sec == '3':
                kitap_ara()
            elif kitap_islemi_sec == '4':
                break
            else:
                print('Lutfen gecerli bir islem giriniz')
          
    elif islem_sec == "3":  # Çıkış islemi
        print("Cikis yapiliyor.")
        break
    else:
        print("Lütfen geçerli bir işlem seçiniz.")

    