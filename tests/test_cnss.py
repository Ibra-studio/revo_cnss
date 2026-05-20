from services.cnss_service import calculer_cotisation_patronal,calculer_cotisation_salarial


def test_cotisation_salariale():
     result=calculer_cotisation_salarial(100000)
     assert result == 6000
def test_cotisation_patronale():
     result=calculer_cotisation_patronal(100000)
     assert result == 19000
def test_cotisation_salariale_zero():
    result = calculer_cotisation_salarial(0)
    assert result == 0

def test_cotisation_patronale_zero():
    result = calculer_cotisation_patronal(0)
    assert result == 0

def test_cotisation_salariale_grand_salaire():
    result = calculer_cotisation_salarial(500000)
    assert result == 30000

def test_cotisation_patronale_grand_salaire():
    result = calculer_cotisation_patronal(500000)
    assert result == 95000
