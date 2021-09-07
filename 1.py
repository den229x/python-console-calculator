import sys
import argparse

def choice(a, b, sign):
    if sign == '+':
        return a + b
    elif sign == '-':
        return a - b
    elif sign == '*':
        return a * b
    elif sign == '/':
        try:
            return a / b
        except ArithmeticError:
            print ('ARITHMETIC ERROR: DIVISION BY ZERO')
            exit()

    
def err():
    print('usage: [NAME_OF_PROGRAMM] [--help][-h] [--interactive][-i] first_num(integer) second_num(integer) sign[+, -, *, /]')
    exit()
    
        
def main():
    parser = argparse.ArgumentParser(
        description="Calcurator", 
        usage='1.py [--help][-h] [--interactive][-i] first_num(integer) second_num(integer) sign[+, -, *, /]')
    parser.add_argument('first_num', help='First Integer Number', nargs='?', type=int, default=0)
    parser.add_argument('second_num', help='Second Integer Number', nargs='?', type=int, default=0)
    parser.add_argument('sign', type=str, help='Sign', default='+', nargs='?', choices=['+', '-', '*', '/'])
    parser.add_argument('-i', '--interactive', action='store_true', help='Enable interactive mode')

    num_of_arg = len(sys.argv)
    namespace = parser.parse_args()

    if (num_of_arg == 2) & (namespace.interactive):
        values = input()
        values = values.split()
        
        try:
            a = int(values[0])
            b = int(values[1])
            sign = values[2]
        except Exception:
            err()
        
        print(choice(a, b, sign))
    elif (num_of_arg == 4) & (namespace.interactive == False):   
        print(choice(int(namespace.first_num), int(namespace.second_num), namespace.sign))
    else:
        err()


if __name__  =='__main__':
    main()