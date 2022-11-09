# 10|01|&=
# 
# 1 | (0 & 0) | 1 = 1
# 
# 10!&01|&0&= 
class Stack():
    def __init__(self):
        self.size = 0
        self.content = list()
    def is_empty(self):
        return not bool(self.content)
    def push(self,elem):
        self.content.append(elem)
        self.size = len(self.content)-1
    def pop_(self):
        if not self.is_empty():

            elem = self.content.pop()
            size = len(self.content)-1
            return elem
        else:
            return None
    def peek(self):
        if not self.is_empty():
            return self.content[-1]
        else:
            return None
    def display(self):
        if not self.is_empty():
            return self.content
        else:
            return None

def post_to_in(entry):
    changer = Stack()
    for k in entry:
        if k.isalpha():
            changer.push(k)
        elif k in ['|', '&','!']:
            b = changer.pop_()
            a = changer.pop_()
            add_str = '('+a+k+b+')'
            changer.push(add_str)
        changer.display()    
    return changer.pop_()

    