input = ''' '''


#part 1
values = input.split(',')

answer = 0
for a in values:
    value = 0
    for b in a:
        value += int(ord(b))
        value = value*17
        value = value%256
    #print(a, value)
    answer += value

print(answer)

#part 2

lenses = []
for i in range(256):
    lenses += [[]]

for a in values:
    box = 0
    for b in a:
        if b in ['=','-']:
            break
        box += int(ord(b))
        box = box*17
        box = box%256
    label = a.replace('-','=').split('=')[0]
    focalLength = a.replace('-','=').split('=')[1]
    #print(box, label, focalLength)
    if focalLength != '':
        newRow = [[x[0], focalLength] if x[0] == label else [x[0],x[1]] for x in lenses[box]]
        if len([x for x in newRow if x[0] == label]) == 0:
            lenses[box] += [[label, focalLength]]
        else:
            lenses[box] = newRow
    elif focalLength == '':
        lenses[box] = [x for x in lenses[box] if x[0] != label]
    #print(lenses[:7])     



# for a in lenses[:6]:
#     print(a)


answer = 0
for i, a in enumerate(lenses):
    for j, b in enumerate(a):
        answer += (i+1)*(j+1)*int(b[1])

print(answer)
    

