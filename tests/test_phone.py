from src.phone import Phone

phone1 = Phone("iPhone 14", 120_000, 5, 2)

def test_init_phone():
    assert phone1.name == "iPhone 14"
    assert phone1.price == 120_000
    assert phone1.quantity == 5
    assert phone1.number_of_sim == 2

def test_repr():
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"

def test_str():
    assert str(phone1) == "iPhone 14"

def test_set_number_of_sim():
    phone1.number_of_sim = 4
    assert phone1.number_of_sim == 4

