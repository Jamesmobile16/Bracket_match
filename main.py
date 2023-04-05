class Stack:

    def __init__(self):
        self.stack = []

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.size() == 0:
            return None
        self.stack.pop(-1)

    def peek(self):
        if self.size() == 0:
            return None
        result = self.stack[-1]
        return result

    def size(self):
        result = len(self.stack)
        return result


str_1 = '(((([{}]))))'
str_2 = '[([])((([[[]]])))]{()}'
str_3 = '{{[()]}}'
str_4 = '}{}'
str_5 = '{{[(])]}}'
str_6 = '[[{())}]'


def check_item(str_):
    lst_ = list(str_)
    s = Stack()
    for item in lst_:
        if item in ['(', '{', '[']:
            s.push(item)
        elif s.peek() == '(' and item == ')':
            s.pop()
        elif s.peek() == '{' and item == '}':
            s.pop()
        elif s.peek() == '[' and item == ']':
            s.pop()
        else:
            s.push(item)
            break
    if s.size() == 0:
        print('Сбалансировано')
    else:
        print('Несбалансировано')


if __name__ == '__main__':

    check_item(str_1)
    check_item(str_2)
    check_item(str_3)
    check_item(str_4)
    check_item(str_5)
    check_item(str_6)






