print("HELLO! WELCOME TO OUR STORES\n")
point1=open("database.txt","w")
point1.close()
point1=open("database.txt","a+")
point1.write("you have selected the following items!!!!\n")
point=open("cart.txt","w")
point.close()
point=open("cart.txt","a+")
global mail
global cost
cost=0

#selecting payment method
def payment():
	z=int(input(" mode of payment:\n1.Debitcard\n2.ATM\n3.paytm\n"))
	if(z==1):
		Debitcard()
	elif(z==2):
		ATM()
	elif(z==3):
		paytm()
		
		
#payment through ATM
def ATM():
	print("lanj neku online shopping eanduku\n")

#code for electronics
def electronics(data):
	
	fp=open("electronics.txt","r")
	a=fp.readline()
	l=[]
	if data==1:
		print("Available stock of phones...\nThey are in order of company,cost,rating,available stock\n")
		for i in range(0,16):
			print(a)
			l.append(a)
			a=fp.readline()
	elif data==2:
		print("Available stock of televisions...\nThey are in order of company,cost,rating,available stock\n")
		for i in range(0,16):
			a=fp.readline()
		
		for i in range(1,11):
			print(a)
			l.append(a)
			a=fp.readline()
	elif data==3:
		print("Available stock of Refrigerators...\nThey are in order of company,cost,rating,available stock\n")
		for i in range(0,27):
			a=fp.readline()
		
		for i in range(1,13):
			print(a)
			l.append(a)
			a=fp.readline()
	elif data==4:
		print("Available stock of laptops...\nThey are in order of company,cost,rating,available stock\n")
		for i in range(0,39):
			a=fp.readline()
		
		for i in range(1,16):
			print(a)
			l.append(a)
			a=fp.readline()
	x=int(input("Enter a option:"))
	print()
	point.write(l[x-1])
	point1.write(l[x-1])
	point1.write('\n')
	cost=cost+l[1]
	y=input("For furthur shopping enter 'shop' and for payment enter anything:")
	if(y=="shop"):
		print("Your product has been added to cart\n")
		selecting()
	else:
		payment()


#code for comics
def comicbooks(data):
	
	fp=open("books.txt","r")
	l=[]
	if data==3:
		print("Available stock of comicbooks...\nThey are in order of name,author,cost,rating,available stock\n")
		for i in range(0,18):
			a=fp.readline()
		for i in range(1,11):
			print(a)
			l.append(a)
			a=fp.readline()
	elif data==4:
		print("Available stock of love story books...\nThey are in order of name,author,cost,rating,available stock\n")
		for i in range(0,28):
			a=fp.readline()
		for i in range(1,11):
			print(a)
			l.append(a)
			a=fp.readline()
	x=int(input("Enter a option:"))
	print()
	point.write(l[x-1])
	point1.write(l[x-1])
	point1.write('\n')
	cost=cost+l[1]
	y=input("For furthur shopping enter 'shop' and for payment enter anything:")
	if(y=="shop"):
		print("Your product has been added to cart\n")
		selecting()
	else:
		payment()



#code for studybooks
def studybooks():
	print("Available stock of studybooks...\nThey are in order of name,author,cost,rating,available stock\n")
	fp=open("books.txt","r")
	a=fp.readline()
	l=[]
	for i in range(0,11):
		print(a)
		l.append(a)
		a=fp.readline()
	x=int(input("Enter a option:"))
	print()
	point.write(l[x-1])
	point1.write(l[x-1])
	point1.write('\n')
	cost=cost+l[1]
	y=input("For furthur shopping enter 'shop' and for payment enter anything:")
	if(y=="shop"):
		print("Your product has been added to cart\n")
		selecting()
	else:
		payment()

#code for adventurebooks
def adventurebooks():
	print("Available stock of adventurebooks...\nThey are in order of name,author,cost,rating,available stock\n")
	fp=open("books.txt","r")
	l=[]
	for i in range(0,12):
		a=fp.readline()
	for i in range(1,7):
		print(a)
		l.append(a)
		a=fp.readline()
	x=int(input("Enter a option:"))
	print()
	point.write(l[x-1])
	point1.write(l[x-1])
	point1.write('\n')
	cost=cost+l[1]
	y=input("For furthur shopping enter 'shop' and for payment enter anything:")
	if(y=="shop"):
		print("Your product has been added to cart\n")
		selecting()
	else:
		payment()

		
# fuction to shop
def selecting():
	fp=open("data.txt","r")
	print("We have the following categories\n")
	a=fp.readline()
	l=[]
	for i in range(0,3):
		print(a,end="\n")
		l.append(a)
		a=fp.readline()
	x=int(input("Enter your particular category:"))
	point1.write(l[x-1])
	point1.write('\n')
	if x==1:
		print("Select a category in books\n")
		for i in range(0,4):
			print(a)
			a=fp.readline()
		y=int(input("Enter here:"))
		
		if(y==1):
			studybooks()
		elif(y==2):
		 	adventurebooks()
		elif(y==3 or y==4):
			comicbooks(y)
	elif x==2:
		print("select a category in electronics\n")
		for i in range(0,4):
			a=fp.readline()
		for i in range(0,6):
			print(a)
			a=fp.readline()
		y=int(input("Enter here:"))
		electronics(y)
		
	
# otp sending through email
def otpfun():
	import random
	global randno
	randno=str(random.randint(100000,999999))
	import smtplib
	server=smtplib.SMTP('smtp.gmail.com',587)
	server.starttls
	server.starttls()
	server.login('suryateja.a16@iiits.in','SUrya5412417')
	server.sendmail('suryateja.a16@iiits.in',mail,randno)
	print("\nAn OTP has been sent to your email id\n")
	{}


# otp verification recursive function
def otpverification(otp):
	if otp==randno:
		print("You have been successfully registered and logged in!!! enjoy shopping\n")
	else:
		otpagain=input("You have entered wrong OTP \n Do you want to resend OTP(yes/no):")
		if otpagain=='yes':
			otpfun()
			otp=input("Enter One Time Password sent to your Email Address:\n")
			otpverification(otp)
		else:
			print("Registration Failed")

#fuction for getting user password recursive
def password(count,list1):
	if(count!=3):
		import getpass
		y=getpass.getpass()
		count+=1
		if(y==list1[1]):
			print()
			print("Successfully loged in!!! Enjoy shopping\n")
			selecting()
		else:
			print("Your password is incorrect\n")
			password(count,list1)
	else:
		print("You have entered wrong password for 3 times\nplease login again\n")
		registration()

#getting registered
def registration():
	fp=open("users.txt","a+")
	fp1=open("yourdetails.txt","w")
	inp=(input("TO REGISTER ENTER 1,TO LOG IN ENTER 2:"))
	print()
	if(inp=="1"):
		x=input("enter your name:")
		y=input("create your user id:")
		fp.write(y)
		fp.write(",")
		import getpass
		z=getpass.getpass()
		fp.write(z)
		fp.write(",")
		w=int(input("phone number:"))
		global mail
		mail=input("enter your email id:")
		fp.write(mail)
		fp.write("\n")
		try:
			otpfun()
		except:
			mail=input("Enter a valid email id:")
			otpfun()
		otp=input("enter OTP sent to your Email Address:")
		otpverification(otp)
		selecting()
		fp.close()
	elif(inp=="2"):
		fp=open("users.txt","r")
		x=input("enter your user id:")
		a=fp.readline()
		while(a!=''):
			list1=a.split(",")
			count=0
			if(x==list1[0]):
				mail=list1[2][0:-1]
				password(count,list1)
				break
			a=fp.readline()
		if(a==''):
			print("Your user id is not correct\n")
			registration()
	else:
		print("Enter a valid option")
		registration()
		
		
# sending details to email
def emailfun():
	flag=input("Do you want to send your filled details file(yes/no):").lower()
	if flag=='n':
		print("ok thanks");
	elif flag=='yes':

		import smtplib
		from email.mime.multipart import MIMEMultipart
		from email.mime.text import MIMEText	
		from email.mime.base import MIMEBase
		from email import encoders
 
		fromaddr = "suryateja.a16@iiits.in"
		toaddr =input("Enter mail to send your details:")
 
		msg = MIMEMultipart()
 	
		msg['From'] = fromaddr
		msg['To'] = toaddr
		msg['Subject'] = "REGISTRATION DETAILS"
 
		body = "Thank you for shopping!!!,your details are in the following file"
 
		msg.attach(MIMEText(body, 'plain'))
 
		filename = "database.txt"
		attachment = open("database.txt", "rb")
 
		part = MIMEBase('application', 'octet-stream')
		part.set_payload((attachment).read())
		encoders.encode_base64(part)
		part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
		msg.attach(part)
 	
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login(fromaddr, "SUrya5412417")
		text = msg.as_string()
		server.sendmail(fromaddr, toaddr, text)
		server.quit()
		print("The mail has been sent\n")

# calling registration
registration()
emailfun()
print("Thank you! visit again......\n\n")
