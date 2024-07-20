

class Band:
    def __init__(self, name, hometown):
        self._name = self._validate_string(name, "Name")
        self._hometown = self._validate_string(hometown, "Hometown")
        self._concerts = []

    @staticmethod
    def _validate_string(value, field_name):
        if isinstance(value, str) and len(value) > 0:
            return value
        else:
            raise ValueError(f"{field_name} must be a non-empty string")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = self._validate_string(value, "Name")

    @property
    def hometown(self):
        return self._hometown

    @hometown.setter
    def hometown(self, _):
        raise AttributeError("Cannot change hometown after it has been set.")

    def concerts(self):
        return self._concerts if self._concerts else None

    def venues(self):
        return list({concert.venue for concert in self._concerts}) if self._concerts else None

    def play_in_venue(self, venue, date):
        concert = Concert(date, self, venue)
        if concert not in self._concerts:
            self._concerts.append(concert)
        return concert

    def all_introductions(self):
        return [concert.introduction() for concert in self._concerts] if self._concerts else None


class Concert:

    all = []


    def __init__(self, date, band, venue):
        self._date = self._validate_string(date, "Date")
        self._band = self._validate_band(band)
        self._venue = self._validate_venue(venue)
        band._concerts.append(self)
        venue._concerts.append(self)
        Concert.all.append(self)

    @staticmethod
    def _validate_string(value, field_name):
        if isinstance(value, str) and len(value) > 0:
            return value
        else:
            raise ValueError(f"{field_name} must be a non-empty string")

    @staticmethod
    def _validate_band(value):
        if isinstance(value, Band):
            return value
        else:
            raise ValueError("Band must be a Band instance")

    @staticmethod
    def _validate_venue(value):
        if isinstance(value, Venue):
            return value
        else:
            raise ValueError("Venue must be a Venue instance")

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = self._validate_string(value, "Date")

    @property
    def band(self):
        return self._band

    @band.setter
    def band(self, value):
        self._band = self._validate_band(value)

    @property
    def venue(self):
        return self._venue

    @venue.setter
    def venue(self, value):
        self._venue = self._validate_venue(value)

    def hometown_show(self):
        return self.band.hometown.lower() == self.venue.city.lower()

    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"



class Venue:
    def __init__(self, name, city):
        self._name = self._validate_string(name, "Name")
        self._city = self._validate_string(city, "City")
        self._concerts = []

    @staticmethod
    def _validate_string(value, field_name):
        if isinstance(value, str) and len(value) > 0:
            return value
        else:
            raise ValueError(f"{field_name} must be a non-empty string")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = self._validate_string(value, "Name")

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = self._validate_string(value, "City")

    def concerts(self):
        return self._concerts if self._concerts else None

    def bands(self):
        return list({concert.band for concert in self._concerts}) if self._concerts else None
