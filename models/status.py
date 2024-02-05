class PackageStatus:
    IN_THE_HUB = 'In the hub' 
    ON_THE_WAY = 'On the way'
    FINAL_DESTINATION_REACHED = 'Final destination reached'
    keys = ['In the hub', 'On the way', 'Final destination reached']
    
    @classmethod
    def next(cls, current: str):
        for i in cls.keys:
            if i == current:
                if cls.keys.index(i) < len(cls.keys)-1:
                    return cls.keys[cls.keys.index(i)+1]
                else:
                    return cls.keys[-1]

    @classmethod
    def previous(cls, current: str):
        for i in cls.keys:
            if i == current:
                if cls.keys.index(i)>0:
                    return cls.keys[cls.keys.index(i)-1]
                else:
                    return cls.keys[0]
                

