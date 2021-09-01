class OperandTypeIncompatible(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def print_msg(self):
        return self.msg

    def another_operation(self):
        """Some other exception operation"""
        pass