from .bloodoath import BloodOath


class Cult:
    all = []

    def __init__(self, name, location, founding_year, slogan):
        self.name = name
        self.location = location
        self.founding_year = founding_year
        self.slogan = slogan
        type(self).all.append(self)

    @classmethod
    def find_by_name(cls, name):
        pass

    @classmethod
    def find_by_location(cls, name):
        pass

    @classmethod
    def find_by_founding_year(cls, name):
        pass

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_val):
        if not isinstance(new_val, str):
            raise TypeError("Cult name must be a string")
        else:
            self._name = new_val

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, new_val):
        if not isinstance(new_val, str):
            raise TypeError("Cult location must be a string")
        else:
            self._location = new_val

    @property
    def founding_year(self):
        return self._founding_year

    @founding_year.setter
    def founding_year(self, new_val):
        if not isinstance(new_val, int):
            raise TypeError("Cult founding year must be an integer")
        else:
            self._founding_year = new_val

    @property
    def slogan(self):
        return self._slogan

    @slogan.setter
    def slogan(self, new_val):
        if not isinstance(new_val, str):
            raise TypeError("Cult slogan must be a string")
        else:
            self._slogan = new_val

    def recruit_follower(self):
        pass

    def cult_population(self):
        pass
