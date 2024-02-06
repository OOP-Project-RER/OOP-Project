class Status:
    STENDING = 'Stending' 
    IN_PROGRESS = 'In_porgress'
    FINISHED = 'Finished'
    keys = ['Stending', 'In_porgress', 'Finished']
    
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
                

