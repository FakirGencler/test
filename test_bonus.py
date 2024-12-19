import pandas as pd
from main import bonus
import pytest
import copy


def test_case1():
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


def test_case2():
    EMPTAB = []
    updated_emp = copy.deepcopy(EMPTAB)
    DEPTTAB = [{"DEPT": "D42", "SALES": 10000.00}]
    updated_dpt = copy.deepcopy(DEPTTAB)

    # İkinci değişken önemsiz, bonus fonksiyonunun mevcut hâline uyumluluk için
    ERRCODE, a = bonus(updated_emp, updated_dpt)

    assert ERRCODE == 1
    assert len(EMPTAB) == len(updated_emp)
    assert len(DEPTTAB) == len(updated_dpt)
    assert EMPTAB == updated_emp
    assert DEPTTAB == updated_dpt


def test_case3():
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


def test_case4():
    EMPTAB = [
        {"NAME": "JONES", "CODE":"M", "DEPT":"D42", "SALARY":210000.00},
        {"NAME": "WARNS", "CODE":"M", "DEPT":"D95", "SALARY":120000.00},
        {"NAME": "LORIN", "CODE":"E", "DEPT":"D42", "SALARY":100000.00},
        {"NAME": "TOY", "CODE":"E", "DEPT":"D95", "SALARY":160000.00},
        {"NAME": "SMITH", "CODE":"E", "DEPT":"D32", "SALARY":140000.00}
    ]
    expected_emp = [
        {"NAME": "JONES", "CODE":"M", "DEPT":"D42", "SALARY":211000.00},
        {"NAME": "WARNS", "CODE":"M", "DEPT":"D95", "SALARY":121000.00},
        {"NAME": "LORIN", "CODE":"E", "DEPT":"D42", "SALARY":102000.00},
        {"NAME": "TOY", "CODE":"E", "DEPT":"D95", "SALARY":161000.00},
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

    # İkinci değişken önemsiz, bonus fonksiyonunun mevcut hâline uyumluluk için
    ERRCODE, a = bonus(updated_emp, updated_dpt)

    assert ERRCODE == 2
    assert len(EMPTAB) == len(updated_emp)
    assert len(DEPTTAB) == len(updated_dpt)
    assert DEPTTAB == updated_dpt
    assert expected_emp == updated_emp


def test_case5():
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

def test_case6():
    EMPTAB = pd.DataFrame(columns=["NAME", "CODE", "DEPT", "SALARY"])
    DEPTTAB = pd.DataFrame(columns=["DEPT", "SALES"])

    EMPTAB.loc[len(EMPTAB)] = ["CHIEF","M", "D99", 998999.99] #99.899K, 998.999K'ya dönüştürüldü çünkü öylesi doğru

    DEPTTAB.loc[len(DEPTTAB)] = ["D99", 99000.01]

    ERRCODE, updated_emp = bonus(EMPTAB, DEPTTAB)

    assert ERRCODE == 0 
    assert updated_emp.loc[updated_emp["NAME"] == "CHIEF", "SALARY"].values[0] == 999999.99 #99.999K, 999.999K'ya dönüştürüldü çünkü öylesi doğru


def test_case7():
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


