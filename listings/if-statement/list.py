# ANCHOR: v1
age = 20
country = 'Cameroon'

if age < 21 and country == 'Cameroon':
    print('In Cameroon, you must be 21 to vote')
else:
    print('You are eligible to vote!')
# ANCHOR_END: v1

# ANCHOR: v2
age = 20
country = 'Malaysia'

if age < 21 and (country == 'Cameroon' or country == 'Malaysia'):
    print('In Cameroon and Malaysia, you must be 21 to vote')
else:
    print('You are eligible to vote!')
# ANCHOR_END: v2

# ANCHOR: v3
age = 20
country = 'Singapore'
countries_21 = ['Cameroon', 'Malaysia', 'Oman',
                'Samoa', 'Singapore', 'Tokelau',
                'Tonga']

if age < 21 and country in countries_21:
    print(f'In {country}, you must be 21 to vote')
else:
    print('You are eligible to vote!')
# ANCHOR_END: v3

# ANCHOR: v4
awesome_cars = ['BMW', 'Porsche']
expensive_cars = ['Mercedes', 'Rolls Royce']
fast_cars = ['Ferrari', 'Bugatti']

car = 'Toyota'

not_awesome = car not in awesome_cars
not_expensive = car not in expensive_cars
not_fast = car not in fast_cars

if not_awesome and not_expensive and not_fast:
    print('This car is boring!')
# ANCHOR_END: v4

# ANCHOR: v5
cars = []

if cars:
    print(f'You have {len(cars)} cars!')
else:
    print('You have no cars!')
# ANCHOR_END: v5

# ANCHOR: v6
cars = ['BMW', 'Porsche']
# ANCHOR_END: v6

if cars:
    print(f'You have {len(cars)} cars!')
else:
    print('You have no cars!')
