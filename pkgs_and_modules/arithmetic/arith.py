# https://docs.python.org/3/library/operator.html
# https://docs.python.org/3/reference/datamodel.html

from . import decors

class Coords(object):
    def __init__(self, x, y):
        self.abscissa = x
        self.ordinate = y

    def __repr__(self):
        return 'Some custom representation'

    def __str__(self):
        return f'[Type : Coords] :: Abscissa={self.abscissa}, Ordinate={self.ordinate}'

    @decors.operand_type_check
    def __add__(self, other):
        """ Normal left operand addition """
        return Coords(self.abscissa + other.abscissa, self.ordinate + other.ordinate)

    # def __radd__(self, other):
    #     """ Normal right operand addition """
    #     print('From __radd__')
    #     return self.__add__(other)
    __radd__ = __add__

    def __neg__(self):
        """ Negation """
        # print('From __neg__')
        # This will negate the Coords type object.
        # Other numeric type will be implicitly handled by their class type, NOT by this class method
        # Rest all will raise an Exception of NotImplemented or TypeError
        return Coords(-self.abscissa, -self.ordinate)

    @decors.neg_san_check
    def __sub__(self, other):
        """ Normal left operand subtraction """
        return self + other.__neg__()
        
    __rsub__ = __sub__

    # @decors.exp
    # def experiment(self):
    #     pass

    # def __floordiv__(self, other):
    # def __trueiv__(self, other):
    # def __mod__(self, other):