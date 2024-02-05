class PackageStatus:
    CREATED = 'Shipment created'
    TRANSIT = 'Package in transit'
    DELIVERED = 'Package deliveretd'
    keys = ['Shipment created', 'Package in transit', 'Package deliveretd']
    
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
                

