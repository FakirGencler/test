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
