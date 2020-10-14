favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

ppl_already_inside = list(favorite_languages.keys())

wanted_ppl = ['jen', 'poo', 'edward', 'utopia']

for ppl in wanted_ppl:
    if ppl in ppl_already_inside:
        print(f'Thank you for responding, {ppl.title()}.')

    else:
        print(f'Please take our favourite languages poll, {ppl.title()}!')