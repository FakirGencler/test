import pandas as pd
from main import bonus
import pytest
import copy


def TestCase1():
    EMPTAB = []
    updated_emp = copy.deepcopy(EMPTAB)
    DEPTTAB = []
    updated_dpt = copy.deepcopy(DEPTTAB)

    # İkinci değişken önemsiz, bonus fonksiyonunun mevcut hâline uyumluluk için
    ERRCODE, a = bonus(updated_emp, updated_dpt)
    
    assert ERRCODE == 1
    assert len(EMPTAB) == len(updated_emp)
    assert len(DEPTTAB) == len(updated_dpt)
    assert EMPTAB == updated_emp
    assert DEPTTAB == updated_dpt


def TestCase2():
    EMPTAB = []
    updated_emp = copy.deepcopy(EMPTAB)
    DEPTTAB = [{"DEPT": "D42", "SALES": 10000.00}] #[{"NAME": "JONES", "CODE":"M", "DEPT":"D42", "SALARY":21000.00}]
    updated_dpt = copy.deepcopy(DEPTTAB)

    # İkinci değişken önemsiz, bonus fonksiyonunun mevcut hâline uyumluluk için
    ERRCODE, a = bonus(updated_emp, updated_dpt)

    assert ERRCODE == 1
    assert len(EMPTAB) == len(updated_emp)
    assert len(DEPTTAB) == len(updated_dpt)
    assert EMPTAB == updated_emp
    assert DEPTTAB == updated_dpt


def TestCase3():
    EMPTAB = [{"NAME": "JONES", "CODE":"M", "DEPT":"D42", "SALARY":21000.00}]
    updated_emp = copy.deepcopy(EMPTAB)
    DEPTTAB = []
    updated_dpt = copy.deepcopy(DEPTTAB)

    # İkinci değişken önemsiz, bonus fonksiyonunun mevcut hâline uyumluluk için
    ERRCODE, a = bonus(updated_emp, updated_dpt)

    assert ERRCODE == 1
    assert len(EMPTAB) == len(updated_emp)
    assert len(DEPTTAB) == len(updated_dpt)
    assert EMPTAB == updated_emp
    assert DEPTTAB == updated_dpt


def TestCase4():
    EMPTAB = pd.DataFrame(columns=["NAME", "CODE", "DEPT", "SALARY"])
    DEPTTAB = pd.DataFrame(columns=["DEPT", "SALES"])

    EMPTAB.loc[len(EMPTAB)] = ["JONES","M", "D42", 210000.00] #21K, 210K'ya dönüştürüldü çünkü öylesi doğru
    EMPTAB.loc[len(EMPTAB)] = ["WARNS", "M", "D95", 120000.00] #12K, 120K'ya dönüştürüldü çünkü öylesi doğru
    EMPTAB.loc[len(EMPTAB)] = ["LORIN","E", "D42", 100000.00] #10K, 100K'ya dönüştürüldü çünkü öylesi doğru
    EMPTAB.loc[len(EMPTAB)] = ["TOY", "E", "D95", 160000.00] #16K, 160K'ya dönüştürüldü çünkü öylesi doğru
    EMPTAB.loc[len(EMPTAB)] = ["SMITH","E", "D32", 140000.00] #14K, 140K'ya dönüştürüldü çünkü öylesi doğru

    DEPTTAB.loc[len(DEPTTAB)] = ["D42", 100000.00]
    DEPTTAB.loc[len(DEPTTAB)] = ["D32", 80000.00]
    DEPTTAB.loc[len(DEPTTAB)] = ["D95", 100000.00]
    DEPTTAB.loc[len(DEPTTAB)] = ["D44", 100000.00]

    ERRCODE, updated_emp = bonus(EMPTAB, DEPTTAB)

    assert ERRCODE == 2
    assert updated_emp.loc[updated_emp["NAME"] == "JONES", "SALARY"].values[0] == 211000.00 #21.1K, 211K'ya dönüştürüldü çünkü öylesi doğru
    assert updated_emp.loc[updated_emp["NAME"] == "WARNS", "SALARY"].values[0] == 121000.00 #12.1K, 121K'ya dönüştürüldü çünkü öylesi doğru
    assert updated_emp.loc[updated_emp["NAME"] == "LORIN", "SALARY"].values[0] == 102000.00 #10.2K, 102K'ya dönüştürüldü çünkü öylesi doğru
    assert updated_emp.loc[updated_emp["NAME"] == "TOY", "SALARY"].values[0] == 161000.00 #16.1K, 161K'ya dönüştürüldü çünkü öylesi doğru
    assert updated_emp.loc[updated_emp["NAME"] == "SMITH", "SALARY"].values[0] == 140000.00 #14K, 140K'ya dönüştürüldü çünkü öylesi doğru
    


def TestCase5():
    EMPTAB = pd.DataFrame(columns=["NAME", "CODE", "DEPT", "SALARY"])
    DEPTTAB = pd.DataFrame(columns=["DEPT", "SALES"])

    EMPTAB.loc[len(EMPTAB)] = ["ALLY","E", "D36", 149999.99] #14.9K, 149K'ya dönüştürüldü çünkü öylesi doğru
    EMPTAB.loc[len(EMPTAB)] = ["BEST", "E", "D33", 150000.00] #15K, 149K'ya dönüştürüldü çünkü öylesi doğru
    EMPTAB.loc[len(EMPTAB)] = ["CELTO","E", "D33", 150000.01] #15.0001K, 150.0001K'ya dönüştürüldü çünkü öylesi doğru

    DEPTTAB.loc[len(DEPTTAB)] = ["D33", 55400.01]
    DEPTTAB.loc[len(DEPTTAB)] = ["D36", 55400.01]

    ERRCODE, updated_emp = bonus(EMPTAB, DEPTTAB)

    assert ERRCODE == 0
    assert updated_emp.loc[updated_emp["NAME"] == "ALLY", "SALARY"].values[0] == 151999.99 #15.1999K, 151.999K'ya dönüştürüldü çünkü öylesi doğru
    assert updated_emp.loc[updated_emp["NAME"] == "BEST", "SALARY"].values[0] == 151000.00 #15.1K, 151K'ya dönüştürüldü çünkü öylesi doğru
    assert updated_emp.loc[updated_emp["NAME"] == "CELTO", "SALARY"].values[0] == 151000.01 #15.10001K, 151.001K'ya dönüştürüldü çünkü öylesi doğru

def TestCase6():
    EMPTAB = pd.DataFrame(columns=["NAME", "CODE", "DEPT", "SALARY"])
    DEPTTAB = pd.DataFrame(columns=["DEPT", "SALES"])

    EMPTAB.loc[len(EMPTAB)] = ["CHIEF","M", "D99", 998999.99] #99.899K, 998.999K'ya dönüştürüldü çünkü öylesi doğru

    DEPTTAB.loc[len(DEPTTAB)] = ["D99", 99000.01]

    ERRCODE, updated_emp = bonus(EMPTAB, DEPTTAB)

    assert ERRCODE == 0 
    assert updated_emp.loc[updated_emp["NAME"] == "CHIEF", "SALARY"].values[0] == 999999.99 #99.999K, 999.999K'ya dönüştürüldü çünkü öylesi doğru


def TestCase7():
    EMPTAB = pd.DataFrame(columns=["NAME", "CODE", "DEPT", "SALARY"])
    DEPTTAB = pd.DataFrame(columns=["DEPT", "SALES"])

    EMPTAB.loc[len(EMPTAB)] = ["DOLE","E", "D67", 100000.00] #10K, 100K'ya dönüştürüldü çünkü öylesi doğru
    EMPTAB.loc[len(EMPTAB)] = ["FORD", "E", "D22", 333333.33] #33.333K, 333.333K'ya dönüştürüldü çünkü öylesi doğru

    DEPTTAB.loc[len(DEPTTAB)] = ["D66", 20000.01]
    DEPTTAB.loc[len(DEPTTAB)] = ["D67", 20000.01]

    ERRCODE, updated_emp = bonus(EMPTAB, DEPTTAB)

    assert ERRCODE == 2
    assert updated_emp.loc[updated_emp["NAME"] == "DOLE", "SALARY"].values[0] == 102000.00 #10.2K, 102K'ya dönüştürüldü çünkü öylesi doğru
    assert updated_emp.loc[updated_emp["NAME"] == "FORD", "SALARY"].values[0] == 333333.33 #33.333K, 333.333K'ya dönüştürüldü çünkü öylesi doğru


