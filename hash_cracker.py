from urllib.request import urlopen, hashlib
from passlib.hash import bcrypt

menu=input("Choose(1. SHA-1/2. MD5): ")
if menu =="1":
	sha1hash = input("please input the SHA1 hash to crack: ")
	common_password = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10k-most-common.txt').read(), 'utf-8')
	for guess in common_password.split('\n'): #Take a guess from the dictionary and split it by line
		hashcrack = hashlib.sha1(bytes(guess, 'utf-8')).hexdigest()
		if hashcrack == sha1hash:
			print ("The password is: ",str(guess))
			quit()
		elif hashcrack != sha1hash:
			print ("Password guess ",str(guess)," does not match, trying next...")
			print("Password is not recorded in the common password lists")
elif menu =="2":
	MD5hash = input("please input the MD5 hash to crack: ")
	common_password = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10k-most-common.txt').read(), 'utf-8')
	for guess in common_password.split('\n'):
		hashcrack = hashlib.md5(bytes(guess, 'utf-8')).hexdigest()
		if hashcrack == MD5hash:
			print ("The password is: ",str(guess))
			quit()
		elif hashcrack != MD5hash:
			print ("Password guess ",str(guess)," does not match, trying next...")
			print ("Password is not recorded in the common password lists")
else:
	print("Choice is invalid. Exiting")
	exit()

#Reference: https://null-byte.wonderhowto.com/how-to/use-beginner-python-build-brute-force-tool-for-sha-1-hashes-0185455/
