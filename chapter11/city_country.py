"""Module containing functions to format the name of a city and country"""

def city_country(city: str, country: str, population=None) -> str:
    formatted_name = f"{city}, {country}".title()
    if population:
        if not isinstance(population, int):
            raise TypeError(f"'population parameter {population} should be of type int")
        else:
            formatted_name += f" - population {format(population, ',')}"

    return formatted_name