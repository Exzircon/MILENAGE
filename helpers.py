def rot(x: bytes|bytearray, r: int, right: bool = True) -> bytes:
	'''
	x: Bytes to rotate, can be of any length
	r: How many BITS to rotate, must be divisible by 8
	right: Wheter to rotate the bits left or right, default right
	'''
	bytearr: bytearray = bytearray(x)
	assert(r % 8 == 0)
	rot_amount = r/8
	if right:
		for i in range(rot_amount):
			bytearr.insert(0, bytearr.pop(-1))
	else:
		for i in range(rot_amount):
			bytearr.append(bytearr.pop(0))
	return bytes(bytearr)


def a2b(s: str) -> bytes:
	'''
	Turns a hex string into bytes, same as the bytes.fromhex() method
	'''
	s = s.replace(" ", "")
	assert(len(s) % 2 == 0)
	bytelist: list = list()
	for i in range(0, len(s), 2):
		bytelist.append(int("0x"+s[i]+s[i+1], 16))
	return bytes(bytelist)


#Something doesn't work here, don't know what. Copied from Milenage PowerPoint
def b2a(b: bytes) -> str:
	'''Bytes to ascii. For 16 bytes objects only'''
	print(len(b))
	assert len(b) == 16
	tmp = list()
	for i in range(len(b)):
		tmp.append(f"{b[i]:02x}")
	return "".join(tmp)+"\n"

#Working xor function for 2 variables, newer ones can xor any amount
def old_xor(a: bytes, b: bytes) -> bytes:
    '''
    Takes in two variables: bytes and xor's them by 
    first converting them to int (basically binary)
    ---
    returns: bytes that have been xor'd
    '''
    return int.to_bytes(int.from_bytes(a)^int.from_bytes(b))

def xor(*args: bytes) -> bytes:
    '''
    Takes in any number of arguments (at least 1) and xors each of them.
    Works by first converting them to integers, xoring the integers, then returning bytes
    '''
    assert (len(args) > 0), "xor must get at least 1 argument"
    bin_int : int = 0
    for arg in args:
        bin_int = bin_int ^ int.from_bytes(arg)
    return int.to_bytes(bin_int)

def change_char(string: str, char: str, index: int) -> str:
    '''
    Changes char at index in a given string
    ---
    string: string to modify
    char: character to change to
    index: at which index to change the character
    ---
    returns: string with changed value
    '''
    assert (len(string) > index), "index must be within scope"
    assert (len(char) == 1), "char must be of length 1"
    new_str: str = ""
    for i in range(len(string)):
        if i != index:
            new_str += string[i]
        else:
            new_str += char
    return new_str



#For testing that the functions work
if __name__ == '__main__':
	bits: bytes = b"1234567890123456"
	print(int.from_bytes(bits))
	print(b2a(bits))
	