def first():
    print('first')

def second():
    print('second')

def third():
    print('third')

everything = [first,second,third]

for func in everything:
    func()