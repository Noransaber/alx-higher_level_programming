class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            attrs = []
        elif not isinstance(attrs, list):
            raise TypeError("attrs must be a list")
        elif not all(isinstance(attr, str) for attr in attrs):
            raise TypeError("attrs must contain only strings")
        return {attr: getattr(self, attr) for attr in attrs}

    def reload_from_json(self, json):
        if not isinstance(json, dict):
            raise TypeError("json must be a dictionary")
        for k, v in json.items():
            setattr(self, k, v)
