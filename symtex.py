# symtex.py
#
# (Fill in your names/emails here!)
# Omkar H. Ramachandran
# omkar.ramachandran@colorado.edu
#
#
# SymTex Source
#

from sympy import *
import numpy as np
import sys
import re

latex_input = sys.argv[1]
flag = 0
str_command = ""
str_input = ""
variable_dict = []
buffer_input = ""
variables = ""
offset = 0
count = 0
count_var = 0
i = 1
for j in range(i,len(latex_input)-1):
    if(latex_input[j] == 'd' and latex_input[j+1] != '}'):
        buffer_var = ""
        if(latex_input[j+1] == '\\'):
            k = j+2
            while(latex_input[k] != '\\' and latex_input[k] != '}' and latex_input[k] != ' ' and k != len(latex_input)-1):
                buffer_var += latex_input[k]
                k = k+1
            if(count_var == 0):
                variables += buffer_var
                variable_dict.append(["\\"+latex_input[j+1:k],buffer_var])
                count_var += 1
            else:
                variables += " "+buffer_var
                variable_dict.append(["\\"+latex_input[j+1:k],buffer_var])
                count_var += 1
        elif(latex_input[j+1] == '}' or latex_input[j+1] == '^'):
            print("Here",latex_input[j],latex_input[j+1],buffer_var)
        else:
            k = j+1
            while(latex_input[k] != '\\' and latex_input[k] != '}' and latex_input[k] != ' ' and k != len(latex_input)-1):
                buffer_var += latex_input[k]
                k = k+1
            if(count_var == 0):
                variables += buffer_var
                variable_dict.append([latex_input[j+1:k],buffer_var])
                count_var += 1
            else:
                variables += " "+buffer_var
                variable_dict.append([latex_input[j+1:k],buffer_var])
                count_var += 1

# Command String
while(i < len(latex_input)-1):
    if(latex_input[i]!='{'):
        str_command += latex_input[i] 
    if(str_command == "frac"):
        str_command = "diff"
        j = i+2
        N = ""
        while(latex_input[j] != "}"):
            N += latex_input[j]
            j += 1
        j += 1
        if(latex_input[j] == '{'):
            j += 1
        while(latex_input[j] != "}"):
            j += 1
        i = j
    if(latex_input[i] == '{'):
        i = i+1
        break
    i = i+1

#print(str_command)

# Variable sweep
#print(variable_dict)

# Use some Regex magic to get the input string to the format we want
str_input = latex_input[i:-1]

str_input = re.sub(r'\}\{', ')/(', str_input)
str_input = re.sub(r'[\{]', '(', str_input)
str_input = re.sub(r'[\}]', ')', str_input)

#for i in range(len(variable_dict)):
#    str_input = re.sub(r'[^]%s' % variable_dict[i][0],'[^]%s' % variable_dict[i][1],str_input)
#print(str_input)
    
for i in range(len(variable_dict)):
    str_input = re.sub(r'%s' % variable_dict[i][0],'%s' % variable_dict[i][1],str_input)

# Get rid of the dx/dy
for i in range(len(variable_dict)):
    str_input = re.sub(r'd%s' % variable_dict[i][1],'',str_input)

if(len(variable_dict) > 1):
    for i in range(len(variable_dict)):
        for j in range(i,len(variable_dict)):
            str_input = re.sub(r'%s %s' % (variable_dict[0][1], variable_dict[1][1]),'%s*%s' % (variable_dict[0][1],variable_dict[1][1]),str_input)
            str_input = re.sub(r'%s%s' % (variable_dict[0][1], variable_dict[1][1]),'%s*%s' % (variable_dict[0][1],variable_dict[1][1]),str_input)

for i in range(len(variable_dict)):
    str_input = re.sub(r'(\w) %s' % variable_dict[i][1],r'\1*%s' % variable_dict[i][1],str_input)
    str_input = re.sub(r'%s (\w)' % variable_dict[i][1],r'%s*\1' % variable_dict[i][1],str_input)
    str_input = re.sub(r'[)] %s'%variable_dict[i][1],r')*%s'% variable_dict[i][1],str_input)
    str_input = re.sub(r'%s [(]'%variable_dict[i][1],r'%s*('% variable_dict[i][1],str_input)

str_input = re.sub(r'[)] (\w)',r')*\1',str_input)
str_input = re.sub(r'[)] (\W)',r')*\1',str_input)
str_input = re.sub(r'(\w) (\w)',r'\1*\2',str_input)
str_input = re.sub(r'(\w)[)] [(](\w)',r'\1[)]*[(]\2',str_input)

# Get rid of the annoying frac symbols
str_input = re.sub(r'[\\]frac[\(]','(',str_input)

commands = ['frac','sin','cos','tan','exp','log','Ei','Si','arcsin','asin','acos','atan','acot','asec','acsc','sqrt']

str_input = re.sub(r' ','',str_input)

if(str_input == ""):
    str_input = "1"

for c in commands:
    str_input = re.sub(r'[\\]%s' % c,'%s' % c,str_input)

x = symbols(variables)

#print(str_command)
#print(str_input)
#print(variables)
#print(str(latex(integrate(str_input,x))))
#print("\""+str_command+"\"","\"intop\"")

if(str_command == "intop" or str_command == "intop " or str_command == "int"):
    print(latex_input+" = "+str(latex(integrate(str_input,x))))
elif(str_command == "diff"):
    print(latex_input+" = "+latex(diff(str_input,x)))

