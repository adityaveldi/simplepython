x='welcome'
print(type(x))
# to write multiline string use 3 single quote or 3 double quote as shoum below
message="""Hey guys
welcome to THIS college, 
have a great future ahead"""
print(message)
print(len(message))
print(message.lower())
print(message.upper())
print(message.split(','))
value='great' in message
print(value)
print(x+" "+message)
print(message.replace('college','University'))