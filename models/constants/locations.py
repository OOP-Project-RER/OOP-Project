from errors.application_error import ApplicationError


class Locations:
    SYD = 'Sydney'
    MEL = 'Melbourne'
    ADL = 'Adelaide'
    ASP = 'AliceSprings'
    BRI = 'Brisbane'
    DAR = 'Darwin'
    PER = 'Perth'
    
    locations = ['Sydney', 'Melbourne', 'Adelaide', 'AliceSprings', 'Brisbane', 'Darwin', 'Perth']

    sydney = {MEL: 877, ADL: 1376, ASP:	2762, BRI: 909, DAR: 3935, PER:	4016}
    melbourne = {SYD: 877, ADL:	725, ASP: 2255, BRI: 1765, DAR:	3752, PER: 3509}
    adelaide = {SYD: 1376, MEL:	725, ASP: 1530, BRI: 1927, DAR:	3027, PER: 2785}
    alice_springs = {SYD: 2762, MEL: 2255, ADL: 1530, BRI: 2993, DAR: 1497, PER: 2481}
    brisbane = {SYD: 909, MEL: 1765, ADL: 1927, ASP: 2993, DAR: 3426, PER: 4311}
    darwin = {SYD: 3935, MEL: 3752, ADL: 3027, ASP: 1497, BRI: 3426, PER: 4025}
    perth = {SYD: 4016, MEL: 3509, ADL: 2785, ASP: 2481, BRI: 4311, DAR: 4025}

    sydney_trucks = {'Scania': 2, 'Man': 2, 'Actros': 2}
    melbourne_trucks = {'Scania': 1, 'Man': 2, 'Actros': 2}
    adelaide_trucks = {'Scania': 1, 'Man': 2, 'Actros': 2}
    alice_spring_trucks = {'Scania': 1, 'Man': 3, 'Actros': 2}
    brisbane_trucks = {'Scania': 1, 'Man': 2, 'Actros': 3}
    darwin_trucks = {'Scania': 2, 'Man': 2, 'Actros': 2}
    perth_trucks = {'Scania': 2, 'Man': 2, 'Actros': 2}

    city_trucks = {SYD: sydney_trucks,
                   MEL: melbourne_trucks,
                   ADL : adelaide_trucks,
                   ASP : alice_spring_trucks,
                   BRI : brisbane_trucks,
                   DAR : darwin_trucks,
                   PER : perth_trucks
                   }

    @classmethod
    def from_string(cls, location_string):
        '''Method which check if value match the class attributes'''
        if location_string not in [cls.SYD, cls.MEL, cls.ADL, cls.ASP, cls.BRI, cls.DAR, cls.PER]:
            raise ApplicationError(
                f'None of the possible Locations matches the value {location_string}.')

        return location_string
    
    @classmethod
    def show_truck(cls, city):
        '''Method that get the values from dictionary with a key(location) and return string with information'''
        trucks = cls.city_trucks.get(city)
        total_trucks = sum([v for v in trucks.values()])

        return '\n'.join([
            f'{city} hup have total of standing trucks: {total_trucks}',
            '------------------------',
            f'Scania: {trucks.get('Scania')}',
            f'Man: {trucks.get('Man')}',
            f'Actros: {trucks.get('Actros')}'
        ])
