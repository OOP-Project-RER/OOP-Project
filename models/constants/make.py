class Make:
    SCANIA = 'Scania'
    MAN = 'Man'
    ACTROS = 'Actros'

    @classmethod
    def from_string(cls, value) -> str:
        if value not in [cls.SCANIA, cls.MAN, cls.ACTROS]:
            raise ValueError(
                f'None of the possible Make values matches the value {value}.')

        return value
