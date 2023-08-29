def toHex(number):
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


def rgbToHex(r, g, b):
    if r < 0 or r > 255 or g < 0 or g > 255 or b < 0 or b > 255:
        return None
    
    red = rgbToHexHelper(r)
    green = rgbToHexHelper(g)
    blue = rgbToHexHelper(b)

    return f"#{red}{green}{blue}"
 
if __name__ == "__main__":
    while True:
        r = int(input('RED: (0-255)'))
        g = int(input('GREEN: (0-255)'))
        b = int(input('BLUE: (0-255)'))

        hex = rgbToHex(r,g,b)
        if hex == None:
            print('Wrong RGB input')
        else:
            print(f"RGB({r},{g},{b}) to HEX is: {hex}")