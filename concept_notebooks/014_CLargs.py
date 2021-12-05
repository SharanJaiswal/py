import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()  # we have initialized object of ArgumentParser() class & using this, we are going to add arguments
    # args = parser.parse_args()  # this is used to parse the passed arguments from the command terminal, or the cmd line that used to run this file as a script
    # in the cmd term, if typed, python filename.py -h
    # then it will show the help related to the arguments for this file


    # There are two types of arguments :
    # 1. Positional Arguments (mandatory)
    # 2. Optional Arguments

    # Now we will add argument fields using the ArgumentParser() class object
    parser.add_argument('num1', help='First number')    # Positional Arguments' names must be different from Optional arguments
    parser.add_argument('num2', help='Second number')   # Positional Arguments' names must be different from Optional arguments
    parser.add_argument('operator', help='Operator')    # Positional Arguments' names must be different from Optional arguments
    parser.add_argument('--num1o', help='First opt number')  # Optional Arguments' names must be different from positional arguments
    parser.add_argument('--num2o', help='Second opt number') # Optional Arguments' names must be different from positional arguments
    parser.add_argument('--oprtr', help='Optional operator', choices=['add', 'sub', 'div']) # restricting user to choose between from the choices
    # The choices attribute is also available for the Positional arguments. In both types, if choiceis not matched, then error will occur
    # REMEMBER: parsed arguments come back to the program in the form of 'str'. Make sure to convert them to suitable required datatype

    # Now we will parse the argumenst passed to run this script form the cmd terminal
    args = parser.parse_args()
    print(args.num1)
    print(args.num2)
    print(args.operator)
    print(args.num1o)
    print(args.num2o)
    # In cmd terminal: pyhton file.py -h
    # In cmd term: pyhton file.py 4 5 add
    # In cmd term: optional arguments can be placed anywhere as --num1 <val> --num3 <val>, even with/without complete mention of optional agrs, at any place
    # While Positional arguments must appear in relative order

    n1 = int(args.num1)
    n2 = int(args.num2)
    result = None

    if args.operator == 'add':
        print(n1+n2)
    elif args.operator == 'sub':
        print(n1-n2)
    else:
        print('Unsupported Operation.')