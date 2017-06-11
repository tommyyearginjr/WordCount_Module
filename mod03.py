# string_example = 'three...two...one...BLAST-OFF!! Nevertheless, today will be a great day!'
string_example = 'Ten nine eight seven six five four three two one...zero? is this gonna work??? Maybe; maybe not @@@@88'

string_example_broken = list(i for i in string_example)

punc = '.?!, @;:'

punc_broken = list(i for i in punc)

abba = []
abba2 = []

for i in string_example_broken:
    if i not in punc_broken:
        abba.append(i)
    else:
        abba.append(' ')

nox_x = ''.join(abba)

nox_x = nox_x.replace('   ',' ')
nox_x = nox_x.replace('  ',' ')

nox_x_broken = nox_x.split(' ')

for i in range(0,len(nox_x_broken)-1):
    if nox_x_broken[i] == '':
        del nox_x_broken[i]

print(nox_x_broken)

print('Word count = ' + str(len(nox_x_broken)))
