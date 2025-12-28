from app import calculate_discount

def test_discount():
    assert calculate_discount(100, 10) == 90