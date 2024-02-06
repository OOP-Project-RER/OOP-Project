from errors.application_error import ApplicationError


class Locations:
    SYD = 'Sydney'
    MEL = 'Melbourne'
    ADL = 'Adelaide'
    ASP = 'Alice_Springs'
    BRI = 'Brisbane'
    DAR = 'Darwin'
    PER = 'Perth'

    sydney = {MEL: 877, ADL: 1376, ASP:	2762, BRI: 909, DAR: 3935, PER:	4016}
    melbourne = {SYD: 877, ADL:	725, ASP: 2255, BRI: 1765, DAR:	3752, PER: 3509}
    adelaide = {SYD: 1376, MEL:	725, ASP: 1530, BRI: 1927, DAR:	3027, PER: 2785}
    alice_springs = {SYD: 2762, MEL:	2255, ADL: 1530, BRI: 2993, DAR: 1497, PER: 2481}
    brisbane = {SYD: 909, MEL: 1765, ADL: 1927, ASP: 2993, DAR: 3426, PER: 4311}
    darwin = {SYD: 3935, MEL: 3752, ADL: 3027, ASP: 1497, BRI: 3426, PER: 4025}
    perth = {SYD: 4016, MEL: 3509, ADL: 2785, ASP: 2481, BRI: 4311, DAR: 4025}

    def __init__(self, city) -> None:
        self._city = city

    @property
    def city(self):
        return self._city

    @classmethod
    def from_string(cls, location_string):
        if location_string not in [cls.SYD, cls.MEL, cls.ADL, cls.ASP, cls.BRI, cls.DAR, cls.PER]:
            raise ApplicationError(
                f'None of the possible Locations values matches the value {location_string}.')

        return location_string
