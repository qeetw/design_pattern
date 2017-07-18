class Singleton(object):
    _instance = None

    def __init__(self):
        self.data = 100

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)

        return cls._instance

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data 