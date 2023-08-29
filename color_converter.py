
def toHex(number):
    # Helper converting values to hexadecimal (letters part only)
    if int(number) == 10:
        hex = 'A'
    elif int(number) == 11:
        hex = 'B'  
    elif int(number) == 12:
        hex = 'C'  
    elif int(number) == 13:
        hex = 'D'  
    elif int(number) == 14:
        hex = 'E'  
    elif int(number) == 15:
        hex = 'F'  
    else:
        hex = number
    return hex

def rgbToHexHelper(number):
    # Helper converting values to hexadecimal
    hex = int(number / 16)
    temp_hex = int(hex * 16 )
    hex2 = int(number-temp_hex) 
    hex_digit1 = toHex(hex)

    if hex2 > 9:
        hex_digit2 = toHex(hex2)
    else:
        hex_digit2 = str(hex2)
    
    result = f"{hex_digit1}{hex_digit2}"

    return result


# 
def rgbToHex(r, g, b):
    # If wrong rgb patter, then return None
    if r < 0 or r > 255 or g < 0 or g > 255 or b < 0 or b > 255:
        return None
    
    # Convert RGB pieces to HEX code
    red = rgbToHexHelper(r)
    green = rgbToHexHelper(g)
    blue = rgbToHexHelper(b)

    return f"#{red}{green}{blue}"

def rgbToCmyk(r, g ,b):
    # If wrong rgb patter, then return None
    if r < 0 or r > 255 or g < 0 or g > 255 or b < 0 or b > 255:
        return None
    
    # Converting colors values from (0-255) to (0-1) 
    r = r / 255
    g = g / 255
    b = b / 255
    
    # Calculate CMYK colors values
    cyan = 1 - r
    magenta = 1 - g
    yellow = 1 - b
    key = min(cyan, magenta, yellow)
        
    # Avoid division by 0 error
    if (cyan - key == 0 or 1 - key == 0):
        cyan = 0
    else:
        cyan = (cyan - key) /  (1 - key)
    if (magenta - key == 0 or 1 - key == 0):
        magenta = 0
    else:    
        magenta = (magenta - key) /  (1 - key)
    if (yellow - key == 0 or 1 - key == 0):
        yellow = 0
    else:
        yellow = (yellow - key) /  (1 - key)

    # Convert the color values to a percentage
    cyan = round(cyan,2) * 100
    magenta = round(magenta,2) * 100
    yellow = round(yellow,2) * 100
    key = round(key,2) * 100

    return f"cmyk({int(cyan)}%,{int(magenta)}%,{int(yellow)}%,{int(key)}%)"
 
# Avoid prompting during unit tests
if __name__ == "__main__":
    while True:
        try:
            # Ask user to provide RGB values of color
            print('Please, provide RGB values for each of colors: ')
            r = int(input('RED (0-255): '))
            g = int(input('GREEN (0-255): '))
            b = int(input('BLUE (0-255): '))

            # Ask which converter user want to use
            converter = input('Choose converter ("1" to convert RGB to HEX, "2" to convert RGB to CMYK): ')
            if converter == '1':
                # Convert to Hex
                hex = rgbToHex(r,g,b)
                if hex == None:
                    print('Wrong RGB input')
                else:
                    print(f"""
########################################################                 
# 😉 rgb({r},{g},{b}) in HEX is: {hex} 😉
########################################################
""")
            elif converter == '2':
                # Convert to Cmyk
                cmyk = rgbToCmyk(r,g,b)
                if cmyk == None:
                    print('Wrong RGB input')
                else:
                    print(f"""
########################################################
# 😵 rgb({r},{g},{b}) in CMYK is: {cmyk} 😉
########################################################
""")
            else:
                print('Wrong choice.')
        except ValueError as e:
            print(e)