import art

print(art.logo)


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


operations = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div
}

n1 = int(input("Whats the first number?"))
n2 = int(input("Whats the second number?"))
for i in operations:
    print(i)


operation = input('Which Operation do you need?')
calc = operations[operation]
answer = calc(n1, n2)

print(f'{n1} {operation} {n2} = {answer}')

