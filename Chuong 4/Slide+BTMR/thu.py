def spam(divideBy):
    try:
        result=42/divideBy
    except:
        print('Sorry!You are dividing by zero')
    else:
        print('Yeah!Your answer is:',result)
        
print(spam(1))
print(spam(0))