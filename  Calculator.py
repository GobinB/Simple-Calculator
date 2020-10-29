# Simple Calculator app 
#  Input two numbers 
# Choose an operator with quotation marks. ex "+" 
# Get your desired output! 


def calc(a, b, op):
    
    #  The function will result as follows: a op b = outcome of the operation. 
    
   

    if op not in '+-/*':
        return 'Please only type one of these characters: "+, -, *, /"!'

    if op == '+':
        return(str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a + b))
    if op == '-':
        return(str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a - b))
    if op == '*':
        return(str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a * b))
    if op == '/':
        return(str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a / b))


def main():  

    a = int(input('Please input the first number: '))

    b = int(input('Please input the second number: '))
    op = input(
        'What kind of operation would you like to do? put it in quotation marks!\
         \nChoose between "+, -, *, /" : ') 

    print(calc(a, b, op))

if __name__ == '__main__':
 
 
    main()





