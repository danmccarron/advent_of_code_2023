input = '''???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1'''

# 1,4,1,1,4,10

lines = input.splitlines()
def splitGears(g):
    return [x for x in g.split('.') if x != '']
def countGears(sg):
    return [len([y for y in g if y == '#']) for g in sg]
def checkGears(gr,cg):
    return [int(x) for x in gr] == cg

    
def countPossibleGears(sg):
    return [len([y for y in g if y == '#' or y =='?']) for g in sg]


# answer = 0
# for i, a in enumerate(lines):
#     gears = a.split(' ')[0]
#     groups = a.split(' ')[1].split(',')
#     possStrings = []
#     print(gears, groups, splitGears(gears), countGears(splitGears(gears)), checkGears(groups,countGears(splitGears(gears))))
    
#     qs = [x for x in gears if x == '?']


#     l = [gears]
#     for i in range(len([x for x in gears if x == '?'])):
#         toAdd = []
#         for b in l:
#             toAdd += [b.replace('?','.',1)]
#             toAdd += [b.replace('?','#',1)]
#         l = []
#         l += toAdd
#     answer += len([x for x in l if checkGears(groups,countGears(splitGears(x)))])
#     print(len([x for x in l if checkGears(groups,countGears(splitGears(x)))]))
    
# print(answer)
        

# part 2


# def checkPossible(gears, groups):
#     if len(gears) != 0 and len(groups) != 0:
#         for j, a in enumerate(groups):
#             isPossible = False
#             for i, b in enumerate(gears):
#                 if b in ['#','?']:
#                     if len([c for c in gears[i:i+int(a)] if c =='.']) == 0 and i+int(a) < len(gears):
#                         isPossible = True
#                         newGears = gears[i+int(a):]
#                         newGroups = groups[1:]
#                         print(j*' '+f'{a} can start at {i} in gears {gears}, leaving gears {newGears} and groups {newGroups}')
#             if not isPossible:
#                 print(j*' '+f'{a} cannot be in gears {gears}')
#                     #checkPossible(newGears, newGroups)
#                 break
#             else:
#                 checkPossible(newGears, newGroups)
#             break






# def getRemainingGears(listOfGears, numberToFind):
#     gearsToReturn = []
#     if len(listOfGears) != 0 and len(numberToFind) != 0:
#         for i, gear in enumerate(listOfGears):
#             #print(gear)
#             for j, b in enumerate(gear):
#                 if b in ['#','?']:
#                     if len([c for c in gear[j:j+int(numberToFind)] if c =='.']) == 0 and j+int(numberToFind) <= len(gear):
#                         newGears = gear[j+int(numberToFind):]
#                         #print(f'{numberToFind} can start at {j} in gears {gear}, leaving gears {newGears}')
#                         gearsToReturn += [[gear, newGears]]
#                     if b == '#':
#                         break
#     return gearsToReturn

# # newGears = getRemainingGears(['????.######..#####','?...?.???.###.?'], '1')     

# # print(newGears)


# def getIterationGears(line):
#     for i, a in enumerate([line]):
#         gears = [(1*(a.split(' ')[0]+'?'))[:-1]]
#         groups = 1*a.split(' ')[1].split(',')
#         #print(f'Starting gears {gears}')
#         #print(f'Starting groups {groups}')
#         validGears = []
#         for j, group in enumerate(groups):
#             validGearsToAdd = [j, group]
#             #print(f'Group to find {group}')
#             #print(f'Gears to search {gears}')
#             newGears = getRemainingGears(gears,group)
#             #print(newGears)
#             gears = [x[1] for x in newGears]
#             #print(f'{len(gears)} New gears are {gears}')
#             validGearsToAdd += [newGears]
#             validGears += [validGearsToAdd]    
#     return validGears



# for a in getIterationGears('?#?#?#?#?#?#?#? 1,3,1,6'):
#     print(a)


# # for a in validGears:
# #     print(a)

# #     print(' ')


# # #print(set([x[0] for x in validGears[-1][2]]))

# # print(validGears)

# def sumThrough(validGears):

#     prev = [x for x in validGears[-2][2] if x[1] in set([x[0] for x in validGears[-1][2]])]
#     print(prev)


#     endValues = []
#     for a in set([x[0] for x in prev]):
#         endValues += [[a, len([x for x in prev if x[0] == a])]]
#     print(endValues)
#     print(' ')

#     for i in range(2, len(validGears)+1):
#         newEndValues = []
#         working = []
#         for a in validGears[-i][2]:
#             print(f'{a} has {sum([x[1] for x in endValues if x[0] == a[1]])}')
#             if sum([x[1] for x in endValues if x[0] == a[1]]) > 0:
#                 working += [[a[0], sum([x[1] for x in endValues if x[0] == a[1]])]]
#         for b in set([x[0] for x in working]):
#             newEndValues += [[b, sum([x[1] for x in working if x[0] == b])]]
#         endValues = []
#         endValues += newEndValues
#         working = []


#         #print(' ')

#     return endValues

# for line in ['???.###????.###????.###????.###????.### 1,1,3,1,1,3,1,1,3,1,1,3,1,1,3']:
#     print(f'THIS IS LINE {line}')
#     print(sumThrough(getIterationGears(line)))



#print([x for x in validGears[-3][2] if x[1] in [x[0] for x in endValues]])





# for i in range(2,len(validGears)+1):
#     print(validGears[-i][2])
#     validRemaining = []
#     gearsRepresents = []
#     for a in validGears[-i][2]:
#         if len(gearsRepresents) = 0
#             print(f'{a[0]} appears in next {len([x[1] for x in validGears[-i+1][2] if x[0] == a[0]])} times')
#             if len([x[1] for x in validGears[-i+1][2] if x[0] == a[0]]) > 0:
#                 validRemaining += [a[0]]
#         else:
#             [x for x in gearsRepresents]
#     for a in set(validRemaining):
#         gearsRepresents += [a, len([x for x in validRemaining if x == a])]
#     print(' ')
        

    
# for i, a in enumerate(lines):
#     gears = (5*(a.split(' ')[0]+'?'))[:-1]
#     groups = 5*a.split(' ')[1].split(',')
#     print(gears, )



# answer = 0
# for i, a in enumerate(lines):
#     gears = (3*(a.split(' ')[0]+'?'))[:-1]
#     groups = 3*a.split(' ')[1].split(',')
#     #gears = a.split(' ')[0]+'?'
#     #groups = a.split(' ')[1].split(',')

#     qs = len([x for x in gears if x == '?'])

#     print(gears, groups, qs*qs, splitGears(gears)) #, countGears(splitGears(gears)), checkGears(groups,countGears(splitGears(gears))))
    
    


#     l = [gears]
#     for i in range(len([x for x in gears if x == '?'])):
#         toAdd = []
#         for b in l:
#             toAdd += [b.replace('?','.',1)]
#             toAdd += [b.replace('?','#',1)]
#         l = []
#         l += toAdd
#     answer += len([x for x in l if checkGears(groups,countGears(splitGears(x)))])
#     print(len([x for x in l if checkGears(groups,countGears(splitGears(x)))]))
    
# print(answer)


answer = 0
for i, a in enumerate(lines[1:2]):
    gears = (5*(a.split(' ')[0]+'?'))[:-1]
    groups = 5*a.split(' ')[1].split(',')
    #gears = a.split(' ')[0]+'?'
    #groups = a.split(' ')[1].split(',')

    qs = len([x for x in gears if x == '?'])

    print(gears, groups, qs, splitGears(gears)) #, countGears(splitGears(gears)), checkGears(groups,countGears(splitGears(gears))))
    
    variants = 0
    for j in range(2**qs):
        theBin = str(format(j,'b'))
        fullBin = (qs - len(theBin))*'0' + theBin
        qReplace = fullBin.replace('0','.').replace('1','#')
        gearVariant = gears
        while len(qReplace) != 0:
            gearVariant = gearVariant.replace('?',qReplace[0],1)
            qReplace = qReplace[1:]
        #print(gearVariant, checkGears(groups,countGears(splitGears(gearVariant))))
        if checkGears(groups,countGears(splitGears(gearVariant))):
            variants += 1
    print(i, a, variants)
