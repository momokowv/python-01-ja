def encode (word):
    
    encode_list=[]
    
    for x in word:
        encode_list.append(str(ord(x)))
    return " ".join(encode_list)

def decode (num):

    decode_list=[]
    num_list=num.split()

    for x in num_list:
        decode_list.append(chr(int(x)))
    return "".join(decode_list)

print(encode("Hello world"))
print(decode("72 101 108 108 111 32 119 111 114 108 100"))