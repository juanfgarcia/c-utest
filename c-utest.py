import re
import sys

#Pattter that matches the function declaration
functionPattern = re.compile('^(int|char)(\s)*(?!main)[a-zA-Z0-9]*\(.*\)(\s)*\{')
#Pattern that matches the function return type
returnPattern = re.compile('(int|char)')
# Patten that matches each parameter
parameterPattern = re.compile('(int|char)(\s)*[a-zA-Z0-9]')
class Function():
    def __init__(self):
        self.returnType = ""
        self.parameters  = [] 

    def setReturnType(self, returnType):
        self.returnType = returnType
    
    def setParameter(self, parameter):
        self.parameters.append(parameter)
    
    def pprint(self):
        print("Return type: " + self.returnType)
        print("Parameter list")
        for param in self.parameters:
            print(param)

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

def getFunctionsFromFile(fd):
    functions = []
    for line in fd:
        for match in re.finditer(functionPattern, line):
            function = Function()
            function.setReturnType(re.match(returnPattern, match.group()).group())
            
            for param in re.finditer(parameterPattern, match.group()):
                function.setParameter(param.group())
           
            functions.append(function)

    return functions

def main():
    # Try to get the file descriptro of the 
    # file passed by argument, if argument is not
    # correct then exit
    try:
        fd = getFileFromArg()
    except AttributeError:
        print("Error: Incorrect number of arguments")
        sys.exit()

    for function in getFunctionsFromFile(fd):
        function.pprint()
    
if __name__=='__main__':
    main()
