# city_functions.py

def city_country(city, country):
    """Return a formatted string like 'City, Country'."""
    return f"{city.title()}, {country.title()}"

# Function calls
if __name__ == "__main__":
    print(city_country("santiago", "chile"))
    print(city_country("paris", "france"))
    print(city_country("tokyo", "japan"))
    print(city_country("san antonio", "texas"))

    # test_cities.py

# (Remove the test code from this file. Place it in a separate test_cities.py file.)

# Updated function to include population

def city_country(city, country, population=None):
    """Return a formatted string with optional population."""
    result = f"{city.title()}, {country.title()}"
    if population:
        result += f" - population {population}"
    return result

# Further updated function to include language

def city_country(city, country, population=None, language=None):
    """Return a formatted string with optional population and language."""
    result = f"{city.title()}, {country.title()}"
    if population:
        result += f" - population {population}"
    if language:
        result += f", {language.title()}"
    return result

# Example function calls with all parameters

if __name__ == "__main__":
    print(city_country("santiago", "chile"))
    print(city_country("paris", "france", 2148000))
    print(city_country("san antonio", "texas", 1500000, "english"))
   