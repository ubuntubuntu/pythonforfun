def spam(dividedBy):
    return 42 / dividedBy
    
try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))    
except:
    print('Error: Invalid Argument')

