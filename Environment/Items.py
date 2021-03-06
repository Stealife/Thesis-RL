import numpy as np
from keras.utils import to_categorical

np.random.seed(42)


class Items :
    def __init__(self, id, interval_price = 100, interval_color = 5, catalog_size = -1) :
        self._id = id
        self._price = np.random.randint(interval_price)
        self._color = np.random.randint(interval_color)
        self._for_women = np.random.random() < 0.5
        self.interval_color = interval_color
        self.catalog_size = catalog_size
        # Audience
        self.is_for_parent = np.random.random() < 0.1
        self.for_age = np.random.randint(18, 100)
        self.for_gender = np.random.random() < 0.5

    def list_item(self) :
        return {"Price " : self._price, "Color " : self._color, "Women item" : self._for_women}

    def get_as_list(self) :
        return [self._id, self._price, self._color, self._for_women]

    def get_as_one_hot(self) :
        return [to_categorical(self.get_id, num_classes = self.catalog_size), self.get_Price,
                to_categorical(self.get_color, num_classes = self.interval_color)]

    @property
    def get_properties(self) :
        return self._price, self._color, self._for_women

    @property
    def get_audience(self) :
        return self.is_for_parent, self.for_age, self.for_gender

    @property
    def get_id(self) :
        return self._id

    @property
    def get_Price(self) :
        return self._price

    @property
    def get_color(self) :
        return self._color
