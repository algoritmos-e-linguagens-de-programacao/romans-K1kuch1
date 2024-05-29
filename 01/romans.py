def int_to_roman(num):
    
    num2 = num // 1000
    num3 = (num % 1000) // 100
    num4 = (num % 100) // 10
    num5 = num % 10

    milhar = ["","M", "MM", "MMM"]
    centena = ["", "C","CC", "CCC", "CD", "D", "DC", "DCC","DCCC", "CM"]
    dezena = ["", "X", "XX", "XXX", "XL","L","LX","LXX","LXXX","XC"]
    unidade = ["","I","II","III","IV","V","VI","VII","VIII","IX"]

    translate = milhar[num2] + centena[num3] + dezena[num4] + unidade[num5]

    return translate
pass 

def roman_to_int(s):
   
