import random

lower = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
upper = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
special = ["!","@","$","%","^","*","(",")","_","-","+","=","#"]
number = ["0","1","2","3","4","5","6","7","8","9"]

# This function permute 2 random element in an array and reverses it. 
# This process is repeated a random number of times(between the length of the array and 100)
def shuffle_array(arr):

    for i in range(0, random.randint(len(arr), 100)):

    	# Generating 2 random indexes
        index1 = random.randint(0,len(arr)-1)
        index2 = random.randint(0,len(arr)-1)

        # Permutting the elements at the random indexes
        tmp = arr[index1]
        arr[index1] = arr[index2]
        arr[index2] = tmp
        
        # Reversing the array
        arr = arr[::-1]

    return arr

# This function generates a key (a string) of a given length
def generate_key(key_length):
	
    key = ""

    # Appending to the key in each iteration either lower, upper, special, number randomly
    for i in range(key_length):
        if(i%4==0):
            n = random.randint(0,len(lower)-1)
            key += lower[n]
        if(i%4==1):
            n = random.randint(0,len(upper)-1)
            key += upper[n]
        if(i%4==2):
            n = random.randint(0,len(special)-1)
            key += special[n]
        if(i%4==3):
            n = random.randint(0,len(number)-1)
            key += number[n]

    # Converting the key in an array, shuffling it and reconverting it into a string
    key = "".join(shuffle_array(list(key)))

    return key

# This function encrypts a string based on a given key
def encrypt(string, key):

	# Converting the string into an array
	string_list = list(string)

	# For each character of the key, we add its ASCII value to each character of the string
	for key_unit in list(key):
		for j in range(0, len(string_list)):
			string_list[j] = chr( ord(string_list[j]) + ord(key_unit) )

	return "".join(string_list)

# This function decrypts a string based on a given key
def decrypt(string, key):

	# Converting the string and the key into an array
	string_list = list(string)
	key_list = list(key)

	# For each character of the key, we substract its ASCII value to each character of the string
	for key_unit in key_list:
		for j in range(0, len(string_list)):
			string_list[j] = chr( ord(string_list[j]) - ord(key_unit) )


	return "".join(string_list)


# TEST EXEMPLE
'''
key = generate_key(15)
print("key is --> " + key)
string = input("string to encrypt --> ")


print("#--- Encryption ---#")
encrypted_string = encrypt(string, key)
print(string + " =====> " + encrypted_string)

print("#--- Decryption ---#")
print(encrypted_string + " =====> " + decrypt(encrypted_string, key))
'''