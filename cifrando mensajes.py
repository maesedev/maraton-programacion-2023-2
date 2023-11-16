
def decode_message(encrypted_text):
    ABC = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    AEI = "aeiouAEIOU" 
    p_pos = ABC.index("p")

    first_letter_pos = ABC.index(  encrypted_text[0].lower() )
    diference = p_pos - first_letter_pos
    
    decrypted_message = ""
    counter = 0
    
    for letter in encrypted_text:
        if letter.isalnum():
            decoded = getItem(ABC  , ABC.index(letter) + diference  )
            decrypted_message +=  decoded
            if decoded in AEI :
                counter += 1
            continue
        # Para los caracteres especiales y espacios
        decrypted_message+=letter
    return [decrypted_message , counter]





def getItem(list,index):
    return list[ index % len(list)]




COUNTER_list = [] 
while True:
    encrypted_line = input()
    [message,counter]  = decode_message(encrypted_line)

    if message == "pFIN":
        break
    COUNTER_list.append(counter)
    print(message)
for item in COUNTER_list:
    print(item)


"""
pEsta cadena esta sin codificar
pfin
qbfjpvBFJPV
xXzwoziui-Um
qGJO
"""