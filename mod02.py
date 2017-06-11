string = list(x for x in 'three...two...one...BLAST-OFF!! Nevertheless, today will be a great day!')
letters = list(a for a in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
comparison = []

for i in string:
    if i not in letters:
        comparison.append(i)

print(len(comparison))
