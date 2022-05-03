"""
Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. 
The function should return true if the string is valid, and false if it's invalid.
Examples

"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
"""

# Solution 
def valid_parentheses(string):
    tmp = [i for i in string if i == ")" or i == "("]
    i = 0
    while i < len(tmp) and i + 1 < len(tmp):
        if tmp[i] == "(" and tmp[i+1] == ")":
            tmp.pop(i)
            tmp.pop(i)
            i = 0
        else:
            i += 1
    return len(tmp) == 0