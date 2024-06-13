
def main():
    print('Welcome to More-Than-A-Caluclator')
    print()
    history = []
    while True:
        print('This calculator can do the following functions:')
        choice = int(input('''          1.  Addition
          2.  Subtraction
          3.  Multiplication
          4.  Division
          5.  Floor Division
          6.  Power of
          7.  Learn Math Formulae with Examples
          8.  View History
          9.  Clear History
          10. Exit
          
          Enter Your Choice: '''))
        
        
        if choice == 1:
            num1 = int(input('Enter a Number: '))
            num2 = int(input('Enter another Number: '))
            print(f'{num1} + {num2} = {add(num1, num2)}')
            history.append([f'{num1} + {num2} = {add(num1, num2)}'])
        elif choice ==2:
            num1 = int(input('Enter a Number: '))
            num2 = int(input('Enter another Number: '))
            print(f'{num1} - {num2} = {sub(num1, num2)}')
            history.append([f'{num1} - {num2} = {sub(num1, num2)}'])
        elif choice == 3:
            num1 = int(input('Enter a Number: '))
            num2 = int(input('Enter another Number: '))
            print(f'{num1} x {num2} = {multiply(num1, num2)}')
            history.append([f'{num1} x {num2} = {multiply(num1, num2)}'])
        elif choice == 4:
            num1 = int(input('Enter a Number: '))
            num2 = int(input('Enter another Number: '))
            print(f'{num1} / {num2} = {divide(num1, num2)}')
            history.append([f'{num1} / {num2} = {divide(num1, num2)}'])
        elif choice == 5:
            num1 = int(input('Enter a Number: '))
            num2 = int(input('Enter another Number: '))
            print(f'{num1} // {num2} = {floordiv(num1, num2)}')
            history.append([f'{num1} // {num2} = {floordiv(num1, num2)}'])
        elif choice == 6:
            num1 = int(input('Enter a Number: '))
            num2 = int(input('Enter another Number: '))
            print(f'{num1} ^ {num2} = {power(num1, num2)}')
            history.append([f'{num1} ^ {num2} = {power(num1, num2)}'])
        elif choice == 7:
            print('''           1. (a + b)^2
          2. (a - b)^2
          3. (a + b)(a - b)
          4. (a^2 - b^2)
          5. (a + b)^3
          6. (a - b)^3
          7. a^3 + b^3
          8. a^3 - b^3
          9. a^3 + b^3 + c^3 - 3abc''')
            choice = int(input('Enter Your Choice: '))
            if choice == 1:
                num1 = int(input('Enter a Number: '))
                num2 = int(input('Enter another Number: '))
                f1(num1, num2)
                history.append([f'({num1}+{num2})^2 = {(num1+num2)**2}'])
            elif choice == 2:
                num1 = int(input('Enter a Number: '))
                num2 = int(input('Enter another Number: '))
                f2(num1, num2)
                history.append([f'({num1}-{num2})^2 = {(num1-num2)**2}'])
            elif choice == 3:
                num1 = int(input('Enter a Number: '))
                num2 = int(input('Enter another Number: '))
                f3(num1, num2)
                history.append([f'({num1}+{num2})({num1}-{num2}) = {(num1**2) - (num2**2)}'])
            elif choice == 4:
                num1 = int(input('Enter a Number: '))
                num2 = int(input('Enter another Number: '))
                f4(num1, num2)
                history.append([f'{num1}^2 - {num2}^2 = {(num1**2) - (num2**2)}'])
            elif choice == 5:
                num1 = int(input('Enter a Number: '))
                num2 = int(input('Enter another Number: '))
                f5(num1, num2)
                history.append([f'({num1}+{num2})^3 = {(num1+num2)**3}'])
            elif choice == 6:
                num1 = int(input('Enter a Number: '))
                num2 = int(input('Enter another Number: '))
                f6(num1, num2)
                history.append([f'({num1}-{num2})^3 = {(num1-num2)**3}'])
            elif choice == 7:
                num1 = int(input('Enter a Number: '))
                num2 = int(input('Enter another Number: '))
                f7(num1, num2)
                history.append([f'{num1}^3 + {num2}^3 = {num1**3 + num2*3}'])
            elif choice == 8:
                num1 = int(input('Enter a Number: '))
                num2 = int(input('Enter another Number: '))
                f8(num1, num2)
                history.append([f'{num1}^3 - {num2}^3 = {num1**3 - num2**3}'])
            elif choice == 9:
                num1 = int(input('Enter a Number: '))
                num2 = int(input('Enter another Number: '))
                num3 = int(input('Enter another Number: '))
                f9(num1, num2, num3)
                history.append([f'{num1}^3 + {num2}^3 + {num3}^3 - 3 x {num1} x {num2} x {num3} = {num1**3 + num2**3 + num3**3 - 3*num1*num2*num3}'])
        elif choice == 8:
            if history == []:
                print()
                print('No functions were executed in the past')
                print()
            else:
                print('The following functions were executed in the past: ')
                for i in history:
                    print(i)
                print()
                ans = input('Would you like to clear the history (y/n): ')
                if ans == 'y':
                    history.clear()
                    if history == []:
                        print()
                        print('History Cleared Successfully')
                        print()
                
        elif choice == 9:
            history.clear()
            if history == []:
                print()
                print('History Cleared')
                print()
                
        elif choice == 10:
            break
        else:
            print()
            print('Invalid Choice, Try Again')
            
    
    print()
    print('Thank you for using More-Than-A-Calculator')
    
def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def divide(x,y):
    return x/y

def floordiv(x,y):
    return x//y

def multiply(x,y):
    return x*y

def power(x,y):
    return x**y

def f1(x,y):
    print('The formula is (a + b)^2 = a^2 + 2ab + b^2')
    print(f"Therefore, here 'a' = {x} and 'b' = {y}")
    print(f'''So,    ({x}+{y})^2 = {x}^2 + (2 x {x} x {y}) + {y}^2
               = {x**2} + {2*x*y} + {y**2}
               = {(x+y)**2}''')

def f2(x,y):
    print('The formula is (a - b)^2 = a^2 - 2ab + b^2')
    print(f"Therefore, here 'a' = {x} and 'b' = {y}")
    print(f'''So,    ({x}-{y})^2 = {x}^2 - (2 x {x} x {y}) + {y}^2
               = {x**2} - {2*x*y} + {y**2}
               = {(x-y)**2}''')
    
def f3(x,y):
    print('The formula is (a + b)(a - b) = a^2 - b^2')
    print(f"Therefore, here 'a' = {x} and 'b' = {y}")
    print(f'''So,    ({x}+{y})({x}-{y}) = {x}^2 - {y}^2
               = {x**2} - {y**2}
               = {x**2 - y**2}''')
    
def f4(x,y):
    print('The formula is (a^2 - b^2) = (a+b)(a-b)')
    print(f"Therefore, here 'a' = {x} and 'b' = {y}")
    print(f'''So,    {x}^2 - {y}^2 = ({x}+{y})({x}-{y})
               = {x+y} x {x-y}
               = {x**2 - y**2}''')
    
def f5(x,y):
    print('The formula is (a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3')
    print(f"Therefore, here 'a' = {x} and 'b' = {y}")
    print(f'''So,    ({x}+{y})^3 = {x}^3 + 3 x {x}^2 x {y} + 3 x {x} x {y}^2 + {y}^3
               = {x**3} + {3*x**2*y} + {3*x*y**2} + {y**3}
               = {(x+y)**3}''')
    
def f6(x,y):
    print('The formula is (a - b)^3 = a^3 - 3a^2b + 3ab^2 - b^3')
    print(f"Therefore, here 'a' = {x} and 'b' = {y}")
    print(f'''So,    ({x}-{y})^3 = {x}^3 - 3 x {x}^2 x {y} + 3 x {x} x {y}^2 - {y}^3
               = {x**3} - {3*x**2*y} + {3*x*y**2} - {y**3}
               = {(x-y)**3}''')
    
def f7(x,y):
    print('The formula is a^3 + b^3 = (a + b)(a^2 - ab + b^2)')
    print(f"Therefore, here 'a' = {x} and 'b' = {y}")
    print(f'''So,    {x}^3 + {y}^3 = ({x}+{y})({x}^2 - {x} x {y} + {y}^2)
               = {x+y} x {x**2 - x*y + y**2}
               = {x**3 + y**3}''')
    
def f8(x,y):
    print('The formula is a^3 - b^3 = (a - b)(a^2 + ab + b^2)')
    print(f"Therefore, here 'a' = {x} and 'b' = {y}")
    print(f'''So,    {x}^3 - {y}^3 = ({x}-{y})({x}^2 + {x} x {y} + {y}^2)
               = {x-y} x {x**2 + x*y + y**2}
               = {x**3 - y**3}''')
    
def f9(x,y,z):
    print('The formula is a^3 + b^3 + c^3 - 3abc = (a + b + c)(a^2 + b^2 + c^2 - ab - bc - ca)')
    print(f"Therefore, here 'a' = {x}, 'b' = {y} and 'c' = {z}")
    print(f'''So,    {x}^3 + {y}^3 + {z}^3 - 3 x {x} x {y} x {z} = ({x} + {y} + {z})({x}^2 + {y}^2 + {z}^2 - {x} x {y} - {y} x {z} - {z} x {x})
               = {x+y+z} x {x**2 + y**2 + z**2 - x*y - y*z - z*x}
               = {x**3 + y**3 + z**3 - 3*x*y*z}''')
       
main()