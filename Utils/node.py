class node:
    def __init__(self, value, ptr=None):
        self._value = value
        self._ptr=ptr

    @property
    def ptr(self):
        return self._ptr

    @ptr.setter
    def ptr(self, nd):
        self._ptr = nd

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        self._value = val

    def __str__(self):
        return f"[{self._value} | {self._ptr}]"

    def __repr__(self):
        return f"[{self._value} | {self._ptr}]"