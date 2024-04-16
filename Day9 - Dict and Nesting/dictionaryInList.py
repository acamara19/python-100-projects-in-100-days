"""
Instructions:
-------------
Write a program that adds to a travel_log. You can see a travel_log which is a `List` that
contains two Dictionaries. Your job is to create a function that can add new countries to this list.

Write a function that will work with the following line of code on line 21 to add the entry for
Brazil to the travel_log.

add_new_country("Brazil", 5, ["São Paulo", "Rio de Janeiro"])
"""

country = input("Country Name: ")
visits = int(input("Number of Visits: "))
list_of_cities = eval(input("Cities visited: "))

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


# function to add new countries to the travel_log.
def add_new_country(country_name, visited, cities):
    new_country = {"country": country_name, "visits": visited, "cities": cities}
    travel_log.append(new_country)


add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times and "
      f"my favorite city is {travel_log[2]['cities'][0]}.")
print(travel_log)
