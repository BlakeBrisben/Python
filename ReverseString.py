
def Reverse(userIn):
    newOut = ""

    for x in range(len(userIn)):
        newOut = newOut + userIn[len(userIn) - x - 1]
    
    return newOut

print("Eneter a string to be reversed: ")
userIn = input()
output = ""

for x in range(len(userIn)):
    output = output + userIn[len(userIn) - x - 1]

print("The reversed string is %s." % output)

print("The reversed string using a function is %s." % Reverse(userIn))