from bonus import bonus
import pytest
import copy

def test_case1():
    EMPTAB = []
    updated_emp = copy.deepcopy(EMPTAB)
    DEPTTAB = []
    updated_dpt = copy.deepcopy(DEPTTAB)

    ERRCODE = bonus(updated_emp, updated_dpt)
    
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

    ERRCODE = bonus(updated_emp, updated_dpt)

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

    ERRCODE = bonus(updated_emp, updated_dpt)

    assert ERRCODE == 1
    assert len(EMPTAB) == len(updated_emp)
    assert len(DEPTTAB) == len(updated_dpt)
    assert EMPTAB == updated_emp
    assert DEPTTAB == updated_dpt

def test_case4():
    # Testlerin anlamlı olabilmesi için sayısal değerler 10 ile çarpıldı.

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

    ERRCODE = bonus(updated_emp, updated_dpt)

    assert ERRCODE == 2
    assert DEPTTAB == updated_dpt
    assert expected_emp == updated_emp

def test_case5():
    EMPTAB = [
        {"NAME": "ALLY", "CODE": "E", "DEPT": "D36", "SALARY": 149999.99},
        {"NAME": "BEST", "CODE": "E", "DEPT": "D33", "SALARY": 150000.00},
        {"NAME": "CELTO", "CODE": "E", "DEPT": "D33", "SALARY": 150000.01}
    ]

    expected_emp = [
        {"NAME": "ALLY", "CODE": "E", "DEPT": "D36", "SALARY": 151999.99},
        {"NAME": "BEST", "CODE": "E", "DEPT": "D33", "SALARY": 151000.00},
        {"NAME": "CELTO", "CODE": "E", "DEPT": "D33", "SALARY": 151000.01}
    ]

    DEPTTAB = [
        {"DEPT": "D33", "SALES": 55400.01},
        {"DEPT": "D36", "SALES": 55400.01}
    ]

    updated_emp = copy.deepcopy(EMPTAB)
    updated_dpt = copy.deepcopy(DEPTTAB)

    ERRCODE = bonus(updated_emp, updated_dpt)

    assert ERRCODE == 0
    assert updated_emp == expected_emp
    assert DEPTTAB == updated_dpt

def test_case6():
    EMPTAB = [
        {"NAME": "CHIEF", "CODE": "M", "DEPT": "D99", "SALARY": 998999.99}
    ]

    expected_emp = [
        {"NAME": "CHIEF", "CODE": "M", "DEPT": "D99", "SALARY": 999999.99}
    ]

    DEPTTAB = [
        {"DEPT": "D99", "SALES": 99000.01}
    ]

    updated_emp = copy.deepcopy(EMPTAB)
    updated_dpt = copy.deepcopy(DEPTTAB)

    ERRCODE = bonus(updated_emp, updated_dpt)

    assert ERRCODE == 0
    assert updated_emp == expected_emp
    assert DEPTTAB == updated_dpt

def test_case7():
    EMPTAB = [
        {"NAME": "DOLE", "CODE": "E", "DEPT": "D67", "SALARY": 100000.00},
        {"NAME": "FORD", "CODE": "E", "DEPT": "D22", "SALARY": 333333.33}
    ]

    expected_emp = [
        {"NAME": "DOLE", "CODE": "E", "DEPT": "D67", "SALARY": 102000.00},
        {"NAME": "FORD", "CODE": "E", "DEPT": "D22", "SALARY": 333333.33}
    ]

    DEPTTAB = [
        {"DEPT": "D66", "SALES": 20000.01},
        {"DEPT": "D67", "SALES": 20000.01}
    ]

    updated_emp = copy.deepcopy(EMPTAB)
    updated_dpt = copy.deepcopy(DEPTTAB)

    ERRCODE = bonus(updated_emp, updated_dpt)

    assert ERRCODE == 2
    assert updated_emp == expected_emp
    assert DEPTTAB == updated_dpt
