cities = {
    'singapore': {
        'country': 'singapore',
        'approx_pop': 5_600_000,
        'fact': 'it is the most expensive city in the world'
    },
    'wuhan': {
        'country': 'china',
        'approx_pop': 10_000_000,
        'fact': 'it gave birth to covid-19 virus'
    },
    'mumbai': {
        'country': 'india',
        'approx_pop': 30_000_000,
        'fact': 'it is a terrorist hot-spot'
    }
}

print(cities)

for city, city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['approx_pop']
    fact = city_info['fact']

    print(f"\n{city.title()} is in {country}, "
          f"with a population of about {population}, "
          f"and {fact}.")