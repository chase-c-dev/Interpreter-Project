def main():
    while True:
        srcCode = input(">>> ")
        if srcCode == "exit":
            break
        final_list = tokenize(srcCode)
        parser = ParserEX(final_list)
        total = parser.addition().value
        print("the answer is: ", total)

class TreeNode: # used to build tree during parsing
    def __init__(self,srcToken):
        self.value = srcToken[0] # stores result of a operation or a number
        self.token = srcToken[1] # stores the token relating to the type of the node
        self.left = None
        self.rightTree = None

# Parses through the input tokenized list and evaluates it, starts out in the addition function which loops through all the functions checking each operation
# The equals function is what increments through the tokens as well as performs token checks to determine what order to perform the operations
class ParserEX:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0
        self.tracker = 0

    def addition(self): # addition is called first
        result = self.multiplication() # calls multiplication which handles the multiplication operations
        while self.equals('PLUS') or self.equals('SUB'):
            op = self.tokens[self.tracker - 1] # gets previous value
            rightTree = self.multiplication()
            result = TreeNode([str(eval(result.value + op[0] + rightTree.value)), 'NUMB'])

        return result

    def multiplication(self): # checks multiplication and division
        result = self.division() # calls division which handles division operations
        while self.equals('TIMES') or self.equals('DIV'):
            op = self.tokens[self.tracker - 1] # gets previous value
            rightTree = self.division()
            result = TreeNode([str(eval(result.value + op[0] + rightTree.value)), 'NUMB'])

        return result
    
    def division(self): # checks division 
        result = self.subtract() # calls subtraction which handles subtraction operations
        while self.equals('DIV'):
            op = self.tokens[self.tracker - 1] # gets previous value
            rightTree = self.subtract()
            result = TreeNode([str(eval(result.value + op[0] + rightTree.value)), 'NUMB'])

        return result
    
    def subtract(self): # checks subtraction
        if self.equals('SUB'):
            op = self.tokens[self.tracker - 1] # gets previous value
            rightTree = self.subtract()
            return TreeNode([str(eval(op[0] + rightTree.value)), 'NUMB'])

        return self.paren()

    def paren(self):
        if self.equals('NUMB'): # if tree node is a NUMB then both trees are None and you return the current NUMB node
            return TreeNode(self.tokens[self.tracker - 1])
        if self.equals('LPAREN'):
            result = self.addition() # goes back up to addition
            self.equals('RPAREN')
            return result
    
    def equals(self, type_of_token): # used to check tokens for operators and alter the tokens throughout the parse
        total = 0
        if self.tracker < len(self.tokens) and self.tokens[self.tracker][1] == type_of_token: # makes sure to only set total to a token if the list index is within bounds and the tokens match up
            self.tokens[self.tracker][1] == type_of_token
            total = self.tokens[self.tracker][1] # sets total equal to current token
        if self.tracker >= len(self.tokens): # returns False if the list index kept by tracker is out of bounds
            total = False
        if total: 
            if self.tracker < len(self.tokens): # checks once again to make sure tracker is not out of bounds 
                self.tracker += 1 # increments tracker (moves to next token)
            return True 
        return False
    
def tokenize(srcCode): # tokenizes all the input code
    tokenizingDict = { # dictionary contains all tokens for relevant elements
        "(" : "LPAREN",
        ")" : "RPAREN",
        "0" : "NUMB",
        "1" : "NUMB",
        "2" : "NUMB",
        "3" : "NUMB",
        "4" : "NUMB",
        "5" : "NUMB",
        "6" : "NUMB",
        "7" : "NUMB",
        "8" : "NUMB",
        "9" : "NUMB",
        "+" : "PLUS",
        "*" : "TIMES",
        "-" : "SUB",
        "/" : "DIV"
    }
    
    num_holder = ""
    num_index = 0

    list = []
    i = 0
    srcCode += " " # add an empty string to the end to counteract the length-1
    while i < len(srcCode)-1:
        if srcCode[i] != " ":
            #print(i)
            if srcCode[i+1] != " " and tokenizingDict[srcCode[i]] == "NUMB" and tokenizingDict[srcCode[i+1]] == "NUMB": # if statement checks to see if a number is multiple digits
                num_index = i
                while srcCode[num_index] != " " and tokenizingDict[srcCode[num_index]] == "NUMB" and num_index != len(srcCode): # stores full number in a string
                    num_holder += srcCode[num_index]
                    num_index += 1
                        
                list.append([num_holder, tokenizingDict[srcCode[i]]]) # assigns string containing number greater than 1 digit to one index in the resulting list
                i = num_index

                num_holder = "" # reset temp variables
                num_index = 0   # reset temp variables

            else:
                list.append([srcCode[i], tokenizingDict[srcCode[i]]]) # adds element to list: srcCode[i] is the element and tokenizingDict is the token
        i += 1

    return list

main()

