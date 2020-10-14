locations = ['singapore', 'usa', 'zimbabwe', 'algeria', 'malaysia']
print(locations)

print(sorted(locations), '\nIn alpha order')

print(locations, '\nSee it\'s still here!')

print(sorted(locations, reverse=True), '\nReversed alpha order')

print(locations, '\nSee it\'s still here!')

locations.reverse()
print(locations, '\nThe list has been permanently changed!!')

locations.reverse()
print(locations, '\nSee it\'s finally back to normal!')

locations.sort()
print(locations, '\nThe list has been permanently changed!!')

locations.sort(reverse=True)
print(locations, '\nThe list has changed it\'s order!!')