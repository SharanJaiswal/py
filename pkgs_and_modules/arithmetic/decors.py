from . import except_hand
from functools import wraps

def operand_type_check(func):
    @wraps(func)
    def wrapper(obj_ref, other_obj):
        try:
            # print(f'From {func.__name__}')
            # print('Object class is: ', other_obj.__class__)
            if isinstance(other_obj, (int, float)):
                return obj_ref.__class__(obj_ref.abscissa+other_obj, obj_ref.ordinate+other_obj)
            elif isinstance(other_obj, obj_ref.__class__):
                return func(obj_ref, other_obj)
            else:
                raise except_hand.OperandTypeIncompatible(f'Expecting operand type of \'int\', \'float\', \'{obj_ref.__class__.__name__}\', not of type \'{type(other_obj).__name__}\'.')
        except except_hand.OperandTypeIncompatible as oti:
            oti.another_operation()
            return oti.print_msg()
    return wrapper

def neg_san_check(func):
    @wraps(func)
    def wrapper(obj_ref, other_obj):
        try:
            # print(f'From {func.__name__}')
            # print('Object class is: ', other_obj.__class__)
            if isinstance(other_obj, (obj_ref.__class__, int, float)):
                return func(obj_ref, other_obj)
            else:
                raise except_hand.OperandTypeIncompatible(f'Expecting operand type of \'int\', \'float\', \'{obj_ref.__class__.__name__}\', not of type \'{type(other_obj).__name__}\'.')
        except except_hand.OperandTypeIncompatible as oti:
            oti.another_operation()
            return oti.print_msg()
    return wrapper

# def exp(func):
#     @wraps(func)
#     def wrapper(object_ref):
#         print(func.__name__)
#         print(func.__class__, object_ref.__class__)
#         print(func.__class__.__name__, object_ref.__class__.__name__)
#         print(func.__module__, object_ref.__module__)
#         print(func.__qualname__)
#         # print(func.__qualname__.__name__, object_ref.__qualname__.__name__)
#     return wrapper