inputs = list(map(int,input().split()))


temp = inputs[0]
inputs[0] = inputs[1]
inputs[1] = temp

inputs[0] *= inputs[2]
inputs[1] += inputs[2]

print(inputs[0])
print(inputs[1])