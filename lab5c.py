#!/usr/bin/env python3
# Author ID: [seneca_id]

def add(number1, number2):
    """Adds two numbers, returns result, handles TypeError exceptions"""
    try:
        return int(number1) + int(number2)
    except ValueError:
        return "error: could not add numbers"

def read_file(filename):
    """Reads a file, returns a list of all lines, handles file-related exceptions"""
    try:
        with open(filename, 'r') as f:
            return f.readlines()
    except (FileNotFoundError, OSError):
        return "error: could not read file"

if __name__ == '__main__':
    print(add(10, 5))  
    print(add('10', 5))  
    print(add('abc', 5))  
    print(read_file('seneca2.txt'))  
    print(read_file('file10000.txt'))  
