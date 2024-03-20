def unique_substrings(input_string):
    
    strings = []
    y=0

    for y in range(len(input_string)):
        for x in range(y,len(input_string)):
            if input_string[y:x+1] not in strings:
                strings.append(input_string[y:x+1])
    
    
    return strings
        


input_string = "banana"
print(unique_substrings(input_string))
