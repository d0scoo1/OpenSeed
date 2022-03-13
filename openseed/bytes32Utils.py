import binascii

'''
bytes32: 0x7465737400000000000000000000000000000000000000000000000000000000
https://onlinestringtools.com/convert-bytes-to-string
'''
def bytes32ToString(b_text:int or str):
    if isinstance(b_text, int):
        b_text = hex(b_text) # toString
    if len(b_text) % 2 != 0:
        print("WARNING! Input Error!")
        return

    b_text = b_text.replace("0x" or "00","")
    text = str(binascii.a2b_hex(b_text),'utf-8')
    print("\nText:",b_text,
        "\nText :",text)
    return text

'''
Text is limited to 32 bytes (1 byte = 2 ASCII char, so total 64 chars).
'''
def stringToBytes32(text:str):
    b_text = binascii.b2a_hex(text.encode("utf-8")).decode('utf-8')
    b_size = len(b_text)
    if b_size > 64:
        b_text = b_text[0:64]
    elif b_size < 64:
        padding = "0000000000000000000000000000000000000000000000000000000000000000"
        b_text = b_text + padding[0:int((64 - b_size))]

    b_text = "0x"+b_text
    print("\nText  :",text,
        "\nBytes32:",b_text)
    if b_size > 64:
        print("WARNING! Input too long and has been truncated!")
    return b_text

def _create_Input(_desc="", _data_sha256="", _data_ipfs=""):
    stringToBytes32(_desc)
    stringToBytes32(_data_sha256)
    stringToBytes32(_data_ipfs)


if __name__ == '__main__':

    #_create_Input("Here is desc", "data_sha256", "data_ipfs") #如果你没有data_ipfs，可以将其设置为""
    _create_Input("OPEN SEED")
    '''
    stringToBytes32("Auto Padding")
    stringToBytes32("Input too long will be cut off. Input too long will be cut off.")

    bytes32ToString("0x4d61792074686520466f726365206265207769746820796f752e000000000000") #string
    bytes32ToString(0x4d61792074686520466f726365206265207769746820796f752e000000000000) #hex
    bytes32ToString("4d61792074686520347468") #short bytes
    '''