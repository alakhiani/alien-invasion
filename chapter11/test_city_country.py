from city_country import city_country

def test_city_country() -> None:
    """Do names like 'Santoago, Chile work?"""
    formatted_name = city_country('santiago', 'CHILE')
    assert formatted_name == 'Santiago, Chile'


def test_city_country_population() -> None:
    """Do names like 'Santiago, Chile - population 5,000,000 work?"""
    formatted_name = city_country('santiago', 'CHILE', 5000000)
    assert formatted_name == 'Santiago, Chile - population 5,000,000'
