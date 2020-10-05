class Storage:
    def __init__(self, data={}):
        super().__init__()
        if isinstance(data, dict):
            self.data = data
        else:
            raise Exception

    def get(self, key):
        if key in self.data:
            return self.data[key]
        else:
            return None

    def remove(self, key):
        if key in self.data:
            del self.data[key]
        else:
            raise KeyError

    def set(self, key, value):
        if key in self.data.keys():
            self.data[key] = value
        else:
            pass
    
    def add(self, key, value):
        try:
            hash(key)
            if not self.get(key):
                self.data[key] = value
            else:
                KeyError(f"Key '{key}' already exists")
        except :
            TypeError(f"{type(key)} is not hashable")