import copy

def bonus(EMP_LIST, DEPT_LIST):
    ESIZE = len(EMP_LIST)  # Çalışanlar listesindeki eleman sayısı
    DSIZE = len(DEPT_LIST)  # Departmanlar listesindeki eleman sayısı
    ERRCODE = 0  # Hata kodu, başlangıçta 0 olarak ayarlanır

    # Tanımlı sabitler
    MAXSALES = 0.0  # Departmanlar için maksimum satış başlangıç değeri
    SINC = 2000.00  # Standart maaş artışı
    LINC = 1000.00  # Daha düşük maaş artışı
    LSALARY = 150000.00  # Maaş sınırı
    MGR = 'M'  # Yönetici kodu

    # Hata kontrolü
    if ESIZE <= 0 or DSIZE <= 0:
        ERRCODE = 1  # Çalışan veya departman listesi boşsa hata kodu 1 atanır
    else:
        # Departmanlarda maksimum satış değerini bulma
        for dept in DEPT_LIST:  # Departman listesinde döngü
            if dept["SALES"] >= MAXSALES:
                MAXSALES = dept["SALES"]  # Maksimum satış güncellenir

        # Maksimum satış yapan departmanlar üzerinde işlem
        for dept in DEPT_LIST:  # Tüm departmanları kontrol et
            if dept["SALES"] == MAXSALES:  # Maksimum satışa sahip departman
                FOUND = False  # Başlangıçta departman için çalışan bulunmadı
                # Çalışanları kontrol et
                for emp in EMP_LIST:  # Tüm çalışanları kontrol et
                    if emp["DEPT"] == dept["DEPT"]:  # Departman eşleşmesi
                        FOUND = True  # Çalışan bulundu

                        # Maaş artışı kontrolü
                        if emp["SALARY"] >= LSALARY or emp["CODE"] == MGR:
                            emp["SALARY"] += LINC  # Daha düşük maaş artışı
                        else:
                            emp["SALARY"] += SINC  # Standart maaş artışı

                if not FOUND:  # Eğer uygun bir çalışan bulunamadıysa
                    ERRCODE = 2  # Hata kodu 2 atanır

    return ERRCODE

def main():
    EMPTAB = [
        {"NAME": "JONES", "CODE":"M", "DEPT":"D42", "SALARY":210000.00},
        {"NAME": "WARNS", "CODE":"M", "DEPT":"D95", "SALARY":120000.00},
        {"NAME": "LORIN", "CODE":"E", "DEPT":"D42", "SALARY":100000.00},
        {"NAME": "TOY", "CODE":"E", "DEPT":"D95", "SALARY":160000.00},
        {"NAME": "SMITH", "CODE":"E", "DEPT":"D32", "SALARY":140000.00}
    ]

    DEPTTAB = [
        {"DEPT": "D42", "SALES": 100000.00},
        {"DEPT": "D32", "SALES": 80000.00},
        {"DEPT": "D95", "SALES": 100000.00},
        {"DEPT": "D44", "SALES": 100000.00}
    ]
    
    updated_emp = copy.deepcopy(EMPTAB)
    updated_dpt = copy.deepcopy(DEPTTAB)

    ERRCODE = bonus(updated_emp, updated_dpt)

    print("Updated Employees: ", updated_emp)
    print("Error Code: ", ERRCODE)
