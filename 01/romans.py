++def int_to_roman(num):
    
    num2 = num // 1000
    num3 = (num % 1000) // 100
    num4 = (num % 100) // 10
    num5 = num % 10

    milhar = ["","M", "MM", "MMM"]
    centena = ["", "C","CC", "CCC", "CD", "D", "DC", "DCC","DCCC", "CM"]
    dezena = ["", "X", "XX", "XXX", "XL","L","LX","LXX","LXXX","XC"]
    unidade = ["","I","II","III","IV","V","VI","VII","VIII","IX"]

    translate = milhar[num2] + centena[num3] + dezena[num4] + unidade[num5]

    return(translate)

++def roman_to_int(s):
    # Implemente sua função aqui
    if not isinstance(s, str) or not s:
        raise ValueError("Não pode estar vazio")
    
    roman_dict = {
        'M': 1000, 'CM': 900,
        'D': 500, 'CD': 400,
        'C': 100, 'XC': 90,
        'L': 50, 'XL': 40,
        'X': 10, 'IX': 9,
        'V': 5, 'IV': 4,
        'I': 1
    }
    i = 0
    num = 0
    while i < len(s):
        if i + 1 < len(s) and s[i:i+2] in roman_dict:
            num += roman_dict[s[i:i+2]]
            i += 2
        else:
            num += roman_dict[s[i]]
            i += 1
    return num

    
   
