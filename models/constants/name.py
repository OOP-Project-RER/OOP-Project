from errors.application_error import ApplicationError


class Name:
    SCANIA = 'Scania'
    MAN = 'Man'
    ACTROS = 'Actros'

    @classmethod
    def from_string(cls, value) -> str:
        '''Method which check if value match the class attributes'''
        if value not in [cls.SCANIA, cls.MAN, cls.ACTROS]:
            raise ApplicationError(
                f'None of the possible Name values matches the value {value}.')

        return value
