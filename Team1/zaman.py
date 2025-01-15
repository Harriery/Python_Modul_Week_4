import json
from datetime import datetime, timedelta

def odunc_suresi_hesapla():
    bugun = datetime.now()  # Bugünün tarihi
    iki_hafta_sonra = bugun + timedelta(weeks=2)  # 2 hafta ekle
    return iki_hafta_sonra.strftime('%Y-%m-%d')  # Tarihi formatla




#*******************************************************************
#timedelta, iki tarih veya zaman arasındaki farkı temsil eden bir yapıdır.
#  Ayrıca, bir tarihe veya zamana ekleme/çıkarma yapmanı sağlar.

#timedelta ile tarih/zamana 2 hafta eklenir.
#strftime, bir datetime objesini istediğin formatta metne dönüştürür.

# %Y: Yılı 4 haneli olarak gösterir (örneğin, 2025).
# %m: Ayı 2 haneli olarak gösterir (örneğin, 01 = Ocak).
# %d: Günü 2 haneli olarak gösterir (örneğin, 14).