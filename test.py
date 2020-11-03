'''__ulist = {'Arevaci': ['Noble Fighters', 'Baleric Slingers', 'Celtiberian Cavalry', 'Painted Warriors'],
         'Arverni': ['Chosen Swordsmen', 'Naked Warriors', 'Levy Freeman', 'Oathsworn']}'''

__ulist = {'Arevaci': {'Noble Fighters': 0, 'Baleric Slingers': 0, 'Celtiberian Cavalry': 0, 'Painted Warriors': 0},
           'Arverni': {'Chosen Swordsmen': 0, 'Naked Warriors': 0, 'Levy Freeman': 0, 'Oathsworn': 0}}

'''found = False
for i, j in __ulist.items():
    for k in j:
        if k == 'Baleric Slingers':
            print(k)
            print(__ulist[i][k])
            __ulist[i][k] = 100
            print(k)
            print(__ulist[i][k])
            found = True
if found is False:
    print('The unit is not found')

for i, j in __ulist.items():
    print(i, j)'''

word = "!unit -Arverni -Naked"
if word.startswith('!unit'):
    __ucmd = (word.split('-'))
    __ucmd.pop(0)
    __ucmd = [x.strip(' ') for x in __ucmd]

    if not __ucmd:
        print("not found")
        exit(0)
    found = False
    for i, j in __ulist.items():
        if i in __ucmd:
            print(i + ':')
            for k in j:
                print('\t' + k)
            found = True
    if found is False:
        print('not found')
        exit(0)

    '''result = 5
    while result != -1:
        result = word.find('-', result + 1)
        print(word.split('-'))'''




'''for k in j:
    if k == 'Levy Freeman':
        print(k)'''










