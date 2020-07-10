import re
import sys
from string import Template

#Pattter that matches the function declaration
functionPattern = re.compile('^(int|char)(\s)*(?!main)([a-zA-Z0-9]*)\((.*)\)(\s)*\{')

# Read arguments and raise an exception if
# number of arguments passed is not correct
# or if argument isn't a file.
def getFileFromArg():
    #If 
    if len(sys.argv)!=2:
        raise AttributeError()
    else:
        try:
            fd = open(sys.argv[1])
        except IOError:
            print("File " + sys.argv[1] + " not found")
            sys.exit()

    return fd

def formatParameters(parameters):
    parameters_list = []
    if parameters!="":
            for string in parameters.split(","):
                parameters_list.append(string.split()[0])
    return parameters_list

# Read file line by line searching for the function regex
# if it matches, then strip the return type and it's parameters
# it returns the functions array
def getFunctionsFromFile(fd):
    functions = []
    for line in fd:
        for match in re.finditer(functionPattern, line):
            function = { 'returnType'    : match.group(1), 
                          'funcName'      : match.group(3),
                          'parameterType' : formatParameters(match.group(4))
                        }
            functions.append(function)

    return functions


def generateTestFromFunction(function):
    template_file = open('templates/basic.c')
    src = Template(template_file.read())
    result = src.substitute(function)
    print(result)
    



def main():
    # Try to get the file descriptor of the 
    # file passed by argument, if argument is not
    # correct then exit
    try:
        fd = getFileFromArg()
    except AttributeError:
        print("Error: Incorrect number of arguments")
        sys.exit()

    # Iterrate over all functions objects finded in the file
    for function in getFunctionsFromFile(fd):
        generateTestFromFunction(function)
    
if __name__=='__main__':
    main()
