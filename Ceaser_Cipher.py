import string
import itertools
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
continue_cycle = itertools.cycle(alphabets)
def ceaser_cipher(text, shifts):
    encode_text = ""
    decode_text = ""
    for i in range(0,len(text)):
            if text[i] in alphabets:
                j = alphabets.index(text[i])
                encode_text += alphabets[j+shifts]
                
    print(f"The result of encoded text is:{encode_text}")
    decode = input("Type yes to decode or no to stop:")
    if(decode == "yes"):
        for i in range(0,len(encode_text)):
            if encode_text[i] in alphabets:
                j = alphabets.index(encode_text[i])
                decode_text += alphabets[j-shifts]
        print(f"The result of decoded text is:{decode_text}")
    else:
        print("The end")

t = input("Enter text to encode:")
s = int(input("Enter no.of shifts:"))
ceaser_cipher(t,s)
