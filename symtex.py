# symtex.py
# Omkar H. Ramachandran
# omkar.ramachandran@colorado.edu
#
# SymTex Source
#

from sympy import *
import numpy as np
import sys

latex_input = sys.argv[1]
flag = 0
str_command = ""
str_input = ""
variables = ""
buffer_input = ""
offset = 0
count = 0
count_var = 0
i = 1
while(i < len(latex_input)-1):
    if(flag == 0):
        # Reading in command
        str_command += latex_input[i] 
        if(str_command == "frac"):
            str_command = "diff"
            j = i+2
            N = ""
            while(latex_input[j] != "}"):
                N += latex_input[j]
                j += 1
            j += 1
            D = ""
            while(latex_input[j] != "}"):
                D += latex_input[j]
                j += 1
            if(count_var == 0):
                variables += D[-1]
                count_var += 1
            else:
                variables += " "+D[-1]
                count_var += 1
            i = j
        if(latex_input[i+1] == '{'):
            flag = 1
            i = i+1
    if(flag == 1):
        buffer_input += latex_input[i]
        if(latex_input[i] == '{'):
            if(buffer_input == "\\frac"):
                j = i+1
                N = ""
                while(latex_input[j] != "}"):
                    N += latex_input[j]
                    j += 1
                j += 1
                D = ""
                while(latex_input[j] != "}"):
                    D += latex_input[j]
                    j += 1
                str_input += N+"/"+"("+D+")"
                i = j
            offset += 1
        if(latex_input[i+1] == '^'):
            buffer_input += "**"
            i = i+1
        if(latex_input[i] == 'd'):
            if(count == 0):
                str_input = buffer_input[offset:-1]
                count = 1
            if(count_var == 0):
                variables += latex_input[i+1]
                count_var += 1
            else:
                variables += " "+latex_input[i+1]
                count_var += 1
            i += 1
    i += 1
print(str_input)

# Parse String
# To be done
#
#str_command = sys.argv[1]
#str_input = sys.argv[2]
#variables = sys.argv[3:]

x = symbols(variables)

if(str_command == "intop" or str_command == "int"):
    print("$"+latex(integrate(str_input,x))+"$")
#
#elif(str_command == "dsolve"):
#    print(latex(dsolve(str_input,x)))
#
