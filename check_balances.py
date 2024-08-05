from stack_class import Stack


def check_balances(string):
    stack = Stack()

    bracket_pairs = {
        ')': '(',
        ']': '[',
        '}': '{',
    }

    for char in string:
        if char in bracket_pairs.values():
            # Если символ является открывающей скобкой
            stack.push(char)
            print(f"Pushed {char} onto stack.")
            # Печатаем действие push
        elif char in bracket_pairs:
            # Если символ является закрывающей скобкой
            if stack.is_empty():
                # Если стек пуст, значит, нет
                # соответствующей открывающей скобки
                print(f"Unbalanced at {char}.")
                # Печатаем сообщение об ошибке
                return False
            top = stack.pop()
            if top != bracket_pairs[char]:
                # Сравниваем верхний элемент стека
                # с ожидаемой открывающей скобкой
                print(f"Mismatch found between {top} and {char}.")
                # Печатаем сообщение об ошибке
                return False
        else:
            print(f"Unknown character {char}.")
            # Печатаем сообщение об ошибке
            return False

    if stack.is_empty():
        # Если стек пуст, все скобки сбалансированы
        print("String is balanced.")
    else:
        print("String is unbalanced.")

    return True


# Тестирование функции с новыми примерами
balanced_examples = [
    "(((([{}]))))",
    "[([])((([[[]]])))]{()}",
    "{{[()]}}",
]

unbalanced_examples = [
    "}{",
    "{{[(])]}}",
    "[[{())}]",
]

for example in balanced_examples:
    print(f"\nChecking balanced example: {example}")
    result = check_balances(example)
    print(result)

for example in unbalanced_examples:
    print(f"\nChecking unbalanced example: {example}")
    result = check_balances(example)
    print(result)
