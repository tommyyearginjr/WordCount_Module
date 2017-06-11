countdown = 'three...two...one...BLAST-OFF!! Nevertheless, today will be a great day!'

punc_list = ['...','!!  ', ' ','! ']
countdown_broken = []

for punc in punc_list:
    countdown = countdown.replace(punc, ' ')

countdown_broken = countdown.split(' ')
if countdown_broken[-1] == '':
    countdown_broken.pop()
print(countdown)
print(len(countdown_broken))
