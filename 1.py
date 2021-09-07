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
    else:
        return 'ERROR'
        
def main():
    parser = argparse.ArgumentParser(
        description="Calcurator", 
        usage='1.py [--help][-h] [--interactive][-i] first_num(integer) second_num(integer) sign[+, -, *, /]')
    parser.add_argument('first_num', help='First Number', nargs='?', type=str, default=0)
    parser.add_argument('second_num', help='Second Number', nargs='?', type=str, default=0)
    parser.add_argument('sign', type=str, help='Sign', default='+', nargs='?')
    parser.add_argument('-i', '--interactive', action='store_true', help='Enable interactive mode')


    num_of_arg = len(sys.argv)
    if (num_of_arg == 1) | (num_of_arg > 4):
        parser.print_usage()
        exit()
    
    namespace = parser.parse_args()

    if (num_of_arg == 2) & (namespace.interactive == True):
        values = input()
        values = values.split()

        if len(values) != 3:
            parser.print_usage()
            exit()
        
        try:
            a = int(values[0])
            b = int(values[1])
            sign = values[2]
        except Exception:
            parser.print_usage()
            exit()

        if choice(a, b, sign) == 'ERROR':
            parser.print_usage()
            exit()
        
        print(choice(a, b, sign))
    elif (num_of_arg == 4) & (namespace.interactive == False):
        try:
            int(namespace.first_num)
            int(namespace.second_num)
        except Exception:
            parser.print_usage()
            exit()

        if choice(int(namespace.first_num), int(namespace.second_num), namespace.sign) == 'ERROR':
            parser.print_usage()
            exit()
        
        print(choice(int(namespace.first_num), int(namespace.second_num), namespace.sign))
    else:
        parser.print_usage()


if __name__  =='__main__':
    main()