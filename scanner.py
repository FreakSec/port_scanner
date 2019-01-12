from termcolor import colored
import socket

def fanc1():
	blue = colored("[►]" , 'blue')	
	red = colored("[✖]" , 'red')
	green = colored("[✔]" , 'green')

	host = input(b + "HOST==>")
	port = int(input(b + "PORT==>"))
	
	scan = socket.socket()

	try:
		scan.connect((host,port))
	except:
		print(red , "PORT_STATUS==>" , port , "[CLOSED]")
	else:
		print(green , "PORT_STATUS==>" , port , "[OPEN]")
def fanc2():
	blue = colored("[►]" , 'blue')	
	red = colored("[✖]" , 'red')
	green = colored("[✔]" , 'green')

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



print("\t PORT SCANNER MAIN MENU:")

blue = colored("[►]" , 'blue')	
red = colored("[✖]" , 'red')
green = colored("[✔]" , 'green')

print("\t [1]---scan specific port")
print("\t [2]---scan all ports")

var = input()

if var == "1":
	fanc1()
elif var == "2":
	fanc2()
else:
	print("Wrong parameter!" , 'red')
