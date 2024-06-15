def romanToInt(s: str) -> int:
    result = 0
    decod_num = {
        'I': 1,
        'V': 5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }
    count  =  0
    while count < len(s):
        if count < len(s) - 1 and decod_num[s[count]] < decod_num[s[count + 1]]:
            result += decod_num[s[count + 1]] - decod_num[s[count]]
            count += 2
        else:
            result += decod_num[s[count]]
            count += 1

    return result

assert romanToInt("III") == 3
assert romanToInt("LVIII") == 58
assert romanToInt("MCMXCIV") == 1994
