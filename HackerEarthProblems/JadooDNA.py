def JadooDNA(input):
    switcher = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U'
    }
    return switcher.get(input, "Invalid Input")

print(JadooDNA('G'))