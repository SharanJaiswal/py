from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, value):
        self.container.append(value)

    def pop(self):
        return self.container.pop()

    def is_empty(self):
        return len(self.container) == 0

    def peek(self):
        return self.container[-1]

    def size(self):
        return len(self.container)

if __name__ != '__main__':
    stk = Stack()

    str="We will conquere COVID-19"
    for char in str:
        stk.push(char)

    str=''

    while stk.size():
        str = str+stk.pop()

    print(str)

if __name__ == '__main__':
    def is_open_bracket(char):
        for idx,brac_type in enumerate(['[', '{', '('], 1):
            if char == brac_type:
                return idx

    def is_close_bracket(char):
        for idx,brac_type in enumerate([']', '}', ')'], 1):
            if char == brac_type:
                return idx
    
    def is_bracket(char):
        return is_open_bracket(char) or is_close_bracket(char)

    def is_balanced(str):
        stk = Stack()
        for char in str:
            if not is_bracket(char):
                continue
            else:
                if is_close_bracket(char):
                    if (stk.is_empty()) or (is_open_bracket(stk.peek()) != is_close_bracket(char)):
                        print(">>> Wrong expression!!, False")
                        return
                    else:   # take care of condition if peek gives corresponding open bracket of the current close bracket in inspection
                        print(stk.pop()+char, end = ', ')
                else:   # if its close bracket, push onto the stack. Here, only open brackets will come and survive
                    stk.push(char)
        print(stk.is_empty())
    
    is_balanced("({a+b})")
    is_balanced("))((a+b}{")
    is_balanced("((a+b))")
    is_balanced("))")
    is_balanced("[a+b]*(x+2y)*{gg+kk}")
