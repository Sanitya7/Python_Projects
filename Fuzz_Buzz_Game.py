#FizzBUZZ game 
valid = True 
for i in range(101) :
    if i % 3 == 0 and i % 5 == 0 :
        print( str(i) + ' = Fizz - Buzz')
    else :
        if i % 5 == 0 :
            print(str(i) +'= Buzz')
        else :
            if i % 3 == 0 :
                print(str(i) + ' = Fizz')
            else :
                print(i)
print('<--GAME OVER-->')
