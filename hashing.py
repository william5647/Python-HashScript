import hashlib, bcrypt

menu=input("Choose(1. SHA-1/2. MD5/3. BCRYPT): ")
if menu =="1":
	password = input("Enter your password to hash:")
	setpass = bytes(password, 'utf-8')
	hash = hashlib.sha1(setpass)
	guest_pw = hash.hexdigest()
	print("SHA1:",guest_pw)
elif menu =="2":
	password = input("Enter your password to hash:")
	setpass = bytes(password, 'utf-8')
	hash = hashlib.md5(setpass)
	guest_pw = hash.hexdigest()
	print("MD5:",guest_pw)
elif menu =="3":
	password = input("Enter your password to hash:")
	setpass = bytes(password, 'utf-8')
	hash = bcrypt.hashpw(setpass,bcrypt.gensalt(10))
	print("bcrypt:",hash)
else:
	print("Choice is invalid. Exiting")
	exit()

#Reference: https://null-byte.wonderhowto.com/how-to/use-beginner-python-build-brute-force-tool-for-sha-1-hashes-0185455/
