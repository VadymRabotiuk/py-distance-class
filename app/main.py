class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __add__(self, other: callable) -> callable:

        if not isinstance(other, Distance):
            return Distance(self.km + other.real)

        return Distance(self.km + other.km)

    def __iadd__(self, other: callable) -> callable:

        if not isinstance(other, Distance):
            self.km += other.real
            return self

        self.km += other.km
        return self

    def __mul__(self, other: callable) -> callable:
        return Distance(self.km * other)

    def __truediv__(self, other: callable) -> callable:
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: callable) -> callable:

        if not isinstance(other, Distance):
            return self.km < other.real

        return self.km < other.km

    def __gt__(self, other: callable) -> callable:

        if not isinstance(other, Distance):
            return self.km > other.real

        return self.km > other.km

    def __eq__(self, other: callable) -> callable:

        if not isinstance(other, Distance):
            return self.km == other.real

        return self.km == other.km

    def __ge__(self, other: callable) -> callable:

        if not isinstance(other, Distance):
            return self.km >= other.real

        return self.km >= other.km

    def __le__(self, other: callable) -> callable:

        if not isinstance(other, Distance):
            return self.km <= other.real

        return self.km <= other.km

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."
