def is_valid_IP(strng):
    result = False
    temporal = strng.replace(".", "")
    if temporal.isdigit() == True:
        if strng.count(".") == 3:
            substrings = list(filter(lambda x: x.strip(), strng.split(".")))
            print(substrings)
            for substring in substrings:
                if substring and len(substrings) == 4:
                    if int(substring) < 256 and int(substring) > -1 and (substring == "0" or substring[0] != '0'):

                        result = True
                    else:
                        result = False
                        break

    return result


print(is_valid_IP('49.109..3'))
