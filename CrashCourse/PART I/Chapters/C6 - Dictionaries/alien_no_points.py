alien_0 = {'color': 'green', 'speed': 'slow'}

try:
    print(alien_0['points'])
except:
    print('Nope.')


point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)




