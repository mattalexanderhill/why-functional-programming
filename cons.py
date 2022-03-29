class Cons:
    def __init__(self, value, other=None):
        if isinstance(value, Cons) and not isinstance(other, Cons):
            value, other = other, value
        self.value = value
        self.other = other

    def __iter__(self):
        return Cons(self.value, self.other)

    def __next__(self):
        if self.value is None:
            raise StopIteration
        next_ = self.value
        if self.other:
            self.value = self.other.value
            self.other = self.other.other
        else:
            self.value = None
        return next_

    def __reversed__(self):
        return reversed(list(iter(self)))

    def __repr__(self):
        if self.other is None:
            return f"Cons {self.value} Nil"

        other = repr(self.other)
        if isinstance(self.other, Cons):
            other = f"({other})"

        value = repr(self.value)
        if isinstance(self.value, Cons):
            value = f"({value})"

        return f"Cons {value} {other}"

    def __mul__(self, operand):
        if operand is None or self.value is None:
            return None
        return self.__class__(self.value * operand, self.other)

    def __rmul__(self, operand):
        return self.__mul__(operand)

    def __add__(self, operand):
        if operand is None or self.value is None:
            return None
        return self.__class__(self.value + operand, self.other)

    def __radd__(self, operand):
        return self.__add__(operand)

    @classmethod
    def from_iter(kls, iterable):
        cons = None
        for item in reversed(iterable):
            cons = kls(item, cons)

        return cons

class Node(Cons):
    def __init__(self, value, left, right):
        super().__init__(value, left)
        self.right = right

    @property
    def left(self):
        return self.other

    def __repr__(self):
        if self.value is None:
            return "Nil"
        left = repr(self.left) if self.left is not None else "Nil"
        if isinstance(self.left, Cons):
            left = f"({left})"
        right = repr(self.right) if self.right is not None else "Nil"
        if isinstance(self.right, Cons):
            right = f"({right})"

        return f"Node {self.value} {left} {right}"


