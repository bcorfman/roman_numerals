def to_roman(num):
    mapping = {1000: 'M',
               900: 'CM',
               500: 'D',
               400: 'CD',
               100: 'C',
               90: 'XC',
               50: 'L',
               40: 'XL',
               10: 'X',
               9: 'IX',
               5: 'V',
               4: 'IV',
               1: 'I'}
    roman = ''
    while num > 0:
        for key, val in mapping.items():
            if num >= key:
                num -= key
                roman += val
                break
    return roman


def from_roman(roman):
    mapping = {'M': 1000,
               'CM': 900,
               'D': 500,
               'CD': 400,
               'C': 100,
               'XC': 90,
               'L': 50,
               'XL': 40,
               'X': 10,
               'IX': 9,
               'V': 5,
               'IV': 4,
               'I': 1}
    num = 0
    while roman:
        for key, val in mapping.items():
            if roman.startswith(key):
                roman = roman[len(key):]
                num += val
                break
    return num



