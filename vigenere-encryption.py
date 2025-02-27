alph = [list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")]
for i in range(1, 26):
    alph.append(alph[0][i:] + alph[0][:i])

calph = {char: idx for idx, char in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
nums = {str(i): str(9 - i) for i in range(10)}

def encrypt(phrase, key):
    result = []
    key1 = [key[i % len(key)] for i in range(len(phrase))]
    
    for i, char in enumerate(phrase):
        if char.isalpha():
            key_idx = calph[key1[i].upper()]
            char_idx = calph[char.upper()]
            res_char = alph[key_idx][char_idx]
            result.append(res_char.upper() if char.isupper() else res_char.lower())
        elif char.isnumeric():
            result.append(nums[char])
        else:
            result.append(char)
    
    print("".join(result))

def decrypt(phrase, key):
    result = []
    key1 = [key[i % len(key)] for i in range(len(phrase))]
    
    for i, char in enumerate(phrase):
        if char.isalpha():
            key_idx = calph[key1[i].upper()]
            char_idx = alph[key_idx].index(char.upper())
            res_char = alph[0][char_idx]
            result.append(res_char.upper() if char.isupper() else res_char.lower())
        elif char.isnumeric():
            result.append(nums[char])
        else:
            result.append(char)
    
    print("".join(result))

if __name__ == "__main__":
    confirmation = input("What do you want to do?\n1) Encrypt\n2) Decrypt\n")
    phrase = input("Enter the Message: ")
    key = input("Enter the Key: ").upper()
    
    if confirmation == "1":
        encrypt(phrase, key)
    elif confirmation == "2":
        decrypt(phrase, key)
    else:
        print("That's not a valid option!")
