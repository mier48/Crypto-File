from cryptography.fernet import Fernet
import base64, hashlib
from termcolor import colored
import os, sys
# from os import listdir
# from os.path import isfile, join
# from os import walk

def encrypt(key, filename):
	outFile = os.path.join(os.path.dirname(filename), "(encrypted)" + os.path.basename(filename))
	
	encryptor = Fernet(key)
	
	with open(filename, "rb") as infile:
		with open(outFile, "wb") as outfile:
			data = infile.read()
			outfile.write(encryptor.encrypt(data))

def decrypt(key, filename):
	outFile = os.path.join(os.path.dirname(filename), os.path.basename(filename[17:]))
	decryptor = Fernet(key)

	with open(filename, "rb") as infile:
		with open(outFile, "wb") as outfile:
			data = infile.read()
			outfile.write(decryptor.decrypt(data))

def display_info():
	print(colored('\r\n¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦','green'))
	print(colored('¦','green'), '		 Creado por: Alberto Mier	               ' , colored('¦','green'))
	print(colored('¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦','green'))

def allfiles():
	allFiles = []
	for (dirpath, dirnames, filenames) in walk("\DATA"):
		for file in filenames:
			allFiles.append(os.path.join(dirpath, file))

	return allFiles

display_info()
choice = input("Do you want to (E)ncrypt or (D)ecrypt? ")
#password = input("Enter the password: ")
my_password = 'mypassword'.encode()
key = hashlib.md5(my_password).hexdigest()
key_64 = base64.urlsafe_b64encode(key.encode("utf-8"))

encFiles = allfiles()

if choice == "E":
	for Tfiles in encFiles:	
		if os.path.basename(Tfiles).startswith("(encrypted)"):
			pass

		elif Tfiles == os.path.join(os.getcwd(), sys.argv[0]):
			pass 
		else:
			print(f"Encriptando archivo: {os.path.basename(Tfiles)}")
			encrypt(key_64, str(Tfiles))
			os.remove(Tfiles)

elif choice == "D":
	for Tfiles in encFiles:
		if os.path.basename(Tfiles).startswith("(encrypted)"):
			print(f"Desencriptando archivo: {os.path.basename(Tfiles)}")
			decrypt(key_64, str(Tfiles))
			os.remove(Tfiles)