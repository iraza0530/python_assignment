 ## 4. We are given strings containing brackets of 4 types - round (), square [], curly {} and angle <> ones. The goal is to check whether brackets are in the correct sequence. I.e. any opening bracket should have a closing bracket of the same type somewhere further by the string, and bracket pairs should not overlap, though they could be nested.


given_string = str(input("Enter brackets ... "))
given_string_dict = {}


stack = []
 
for x in given_string:
        if x in ["(", "{", "["]:
 
            stack.append(x)
        else:
            if not stack:
               print('Incorrect') 
            current_char = stack.pop()
            if current_char == '(':
                if x != ")":
                    print('Incorrect') 
            if current_char == '{':
                if x != "}":
                    print('Incorrect')
            if current_char == '[':
                if x != "]":
                    print('Incorrect')


if stack:
    print('')
else:
  print('correct')     
    