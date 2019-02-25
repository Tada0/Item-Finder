
class DictHandler:
    def __init__(self, params):
        self.dict = params

    def add(self, new_map: {}):
        self.dict = {**self.dict, **new_map}

    def remove(self, kvs: []):
        self.dict = {key: self.dict[key] for key in self.dict if key not in kvs}

    def __str__(self):
        return str(self.dict)

    def get_dict(self):
        return self.dict
