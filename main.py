import pandas as pd


EMPTAB = pd.DataFrame(columns=["NAME", "CODE", "DEPT", "SALARY"])
DEPTTAB = pd.DataFrame(columns=["DEPT", "SALES"])

#Örnekleri giriyoruz
EMPTAB.loc[len(EMPTAB)] = ["John","E", "D42", 21000.00]
EMPTAB.loc[len(EMPTAB)] = ["Jane", "M", "D42", 150000.00]

DEPTTAB.loc[len(DEPTTAB)] = ["D42", 100000.00]
DEPTTAB.loc[len(DEPTTAB)] = ["D32", 80000.00]




ESIZE = len(EMPTAB)  # Çalışan tablosundaki eleman sayısı
DSIZE = len(DEPTTAB)  # Departman tablosundaki eleman sayısı
ERRCODE = 0  # Hata kodu, başlangıçta 0 olarak ayarlanır

# Tanımlı sabitler
MAXSALES = 0.0  # Departmanlar için maksimum satış başlangıç değeri
SINC = 2000.00  # Standart maaş artışı
LINC = 1000.00  # Daha düşük maaş artışı
LSALARY = 150000.00  # Maaş sınırı
MGR = 'M'  # Yönetici kodu

# Hata kontrolü
if ESIZE <= 0 or DSIZE <= 0:
    ERRCODE = 1  # Çalışan veya departman tablosu boşsa hata kodu 1 atanır
else:
    # Departmanlarda maksimum satış değerini bulma
    for i in range(DSIZE):  # 0'dan DSIZE'e kadar döngü
        if DEPTTAB.loc[i,"SALES"] >= MAXSALES:
            MAXSALES = DEPTTAB.loc[i,"SALES"]  # Maksimum satış güncellenir

    # Maksimum satış yapan departmanlar üzerinde işlem
    for j in range(DSIZE):  # Tüm departmanları kontrol et
        if DEPTTAB.loc[j,"SALES"] == MAXSALES:  # Maksimum satışa sahip departman
            FOUND = False  # Başlangıçta departman için çalışan bulunmadı

            # Çalışanları kontrol et
            for k in range(ESIZE):  # Tüm çalışanları kontrol et
                if EMPTAB.loc[k, "DEPT"] == DEPTTAB.loc[j, "DEPT"]:  # Departman eşleşmesi
                    FOUND = True  # Çalışan bulundu

                    # Maaş artışı kontrolü
                    if EMPTAB.loc[k, "SALARY"] >= LSALARY or EMPTAB.loc[k, "CODE"] == MGR:
                        EMPTAB.loc[k, "SALARY"] += LINC  # Daha düşük maaş artışı
                    else:
                        EMPTAB.loc[k, "SALARY"] += SINC  # Standart maaş artışı

            if not FOUND:  # Eğer uygun bir çalışan bulunamadıysa
                ERRCODE = 2  # Hata kodu 2 atanır

print(ERRCODE)
print(EMPTAB)