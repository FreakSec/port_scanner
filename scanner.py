from termcolor import colored
import socket

def funcf():
	blue = colored("[!]" , 'blue')	
	red = colored("[!]" , 'red')
	green = colored("[!]" , 'green')

	host = input(b + "HOST==>")
	port = int(input(b + "PORT==>"))
	
	scan = socket.socket()

	try:
		scan.connect((host,port))
	except:
		print(red , "PORT_STATUS==>" , port , "[CLOSED]")
	else:
		print(green , "PORT_STATUS==>" , port , "[OPEN]")
def funcs():
	blue = colored("[!]" , 'blue')	
	red = colored("[!]" , 'red')
	green = colored("[!]" , 'green')

	host = input(blue , "HOST==>")
	port = [20, 21, 22, 23, 42, 43, 53, 67, 69, 80]

	for i in port:
		try:
			scan = socket.socket()
			scan.connect((host , i))
		except scan.error:
			print(red , "PORT_STATUS==>" , port , "[CLOSED]")
		else:
			print(green , "PORT_STATUS==>" , port , "[OPEN]")

blue = colored("[!]" , 'blue')	
red = colored("[!]" , 'red')
green = colored("[!]" , 'green')

print("\t [1]---scan specific port")
print("\t [2]---scan all ports")

inpt = input()

if inpt == 1:
	funcf()
elif inpt == 2:
	funcs()
else:
	print("Wrong parameter!" , 'red')
