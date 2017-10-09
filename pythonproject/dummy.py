print(" --------------------------------------------------------------------\n|                                                                    | \n|                        HELLO! WELCOME TO OUR STORES                |\n|                                                                    |\n --------------------------------------------------------------------")
point1=open("database.txt","a+")
point=open("cart.txt","w")
point.close()
point=open("cart.txt","a+")
global mail
cost=0
variable1=[]
sum=1
#search function for shopping
def recsearch(string,search):
	j=0
	global data
	for i in range(0,len(string)):
			if search[j]==string[i]:
				temp=i
				count=0
				for k in range(0,len(search)):
					if search[k]==string[temp]:
						count=count+1
						temp=temp+1
						if temp>=len(string):
							break
						
				if count==len(search):
					print("\n")
					variable="Brand:"+data[0]+" ,cost:"+data[1]+" ,rating:"+data[2]+" ,available stock:"+data[3]+""
					variable1.append(variable)
					print(variable)
					#print(data[0],data[1],data[2],data[3])
				elif count!=len(search) and count>=4:
					recsearch(string,search[0:len(search)-1])
					


def search(inputfile):
	fp=open(inputfile,"r")
	eachline=fp.readline()
	print()
	search=input("enter product name: ").upper()
	while(eachline!=""):
		global data
		data=eachline.split(",")
		string=data[0].upper()
		recsearch(string,search)
		eachline=fp.readline()
	if(variable1==[]):
		print("\n--------------No such products are available,search other related products----------------\n")
		return 1
	else:
		print("\nWe have the above products available...you can shop for them\n\n")
		return 0


#code for mens clothes
def mensclothes(menin,cost):
	print("select your size\n\n1.small\n\n2.medium\n\n3.large\n\n")
	inpu=int(input("select your choice:"))
	if(inpu>=1 and inpu<=3):
		fp=open("clothes.txt","r")
		a=fp.readline()
		l=[]
		count=0
		if(menin==1):
			print("Available stock of  T-shirts...\nThey are in order of company,cost,rating,available stock\n")
			for i in range(0,8):
				print(a)
				l.append(a)
				a=fp.readline()
				count=count+1
		elif(menin==2):
			print("Available stock of  jean pants..\nThey are in order of company,cost,rating,available stock\n")
			for i in range(0,8):
				a=fp.readline()
			for i in range(1,9):
				print(a)
				l.append(a)
				a=fp.readline()
				count=count+1
		elif(menin==3):
			print("Available stock of  track pants..\nThey are in order of company,cost,rating,available stock\n")
			for i in range(0,16):
				a=fp.readline()
			for i in range(1,7):
				print(a)
				l.append(a)
				a=fp.readline()
				count=count+1
			
		try :
			x=int(input("Enter a option:"))
		except:
			print("-------------------------------enter a valid option-----------------------------\n")
			mensclothes(menin,cost)
	
		if(x>0 and x<=count):
			print()
			point.write(l[x-1])
			point1.write(l[x-1])
			point1.write('\n')
			r=[]
			r=l[x-1].split(",")
			cost=cost+int(r[1])
			y=input("For furthur shopping enter 'shop' and for payment enter anything:")
			if(y=="shop"):
				print("Your product has been added to cart\n")
				selecting(cost)
			else:
				payment(cost)
		else:
			print("-------------------------------enter a valid option-----------------------------\n")
			mensclothes(menin,cost)
	else:
		print("Please enter a valid option!!!\n\n")
		mensclothes(menin,cost)

#code for womens clothes
def womensclothes(womin,cost):
	print("select your size\n\n 1.small\n\n2.medium\n\n3.large\n\n")
	inpu=int(input("select your choice:"))
	if(inpu>=1 and inpu<=3):	
		fp=open("clothes.txt","r")
		a=fp.readline()
		l=[]
		count=0
		if(womin==1):
			print("Available stock of  chudidars...\nThey are in order of company,cost,rating,available stock\n")
			for i in range(0,22):
				a=fp.readline()
			for i in range(1,9):
				print(a)
				l.append(a)
				a=fp.readline()
				count=count+1
		elif(womin==2):
			print("Available stock of  sarees..\nThey are in order of company,cost,rating,available stock\n")
			for i in range(0,30):
				a=fp.readline()
			for i in range(1,8):
				print(a)
				l.append(a)
				a=fp.readline()
				count=count+1
		elif(womin==3):
			print("Available stock of  t-shirts for women..\nThey are in order of company,cost,rating,available stock\n")
			for i in range(0,37):
				a=fp.readline()
			for i in range(1,9):
				print(a)
				l.append(a)
				a=fp.readline()
				count=count+1
		elif(womin==4):
			print("Available stock of  jean pants for women..\nThey are in order of company,cost,rating,available stock\n")
			for i in range(0,45):
				a=fp.readline()
			for i in range(1,9):
				print(a)
				l.append(a)
				a=fp.readline()
				count=count+1
			
		try :
			x=int(input("Enter a option:"))
		except:
			print("-------------------------------enter a valid option-----------------------------\n")
			womensclothes(womin,cost)
	
		if(x>0 and x<=count):
			print()
			point.write(l[x-1])
			point1.write(l[x-1])
			point1.write('\n')
			r=[]
			r=l[x-1].split(",")
			cost=cost+int(r[1])
			y=input("For furthur shopping enter 'shop' and for payment enter anything:")
			if(y=="shop"):
				print("Your product has been added to cart\n")
				selecting(cost)
			else:
				payment(cost)
		else:
			print("-------------------------------enter a valid option-----------------------------\n")
			womensclothes(womin,cost)
	else:
		print("Please enter a valid option!!!\n\n")
		womensclothes(womin,cost)

#payment through paytm
def paytm(cost):
	print("\nRemainder:You have to transfer an amount of %d to number 7995601638\n" %(cost))
	x=input("Enter paytm number to transfer money:")
	if(x!="7995601638"):
		print("The number should be 7995601638!! Try again...\n")
		paytm(cost)
	else:
		y=input("Enter the amount to be transferred to number phoneno-7995601638:")
		if(y==str(cost)):
			print("\nAn amount of %d has been transferred from your paytm account to 7995601638 through paytm\n\n" %(int(cost)))
		else:
			print("\nEnter the correct amount to be transferred\npayment cancelled pay again!!!")
			paytm(int(cost))

# otp sending through email
def otpfun(cost):
	import random
	global randno
	global mail
	randno=str(random.randint(100000,999999))
	import smtplib
	server=smtplib.SMTP('smtp.gmail.com',587)
	#server.starttls
	server.starttls()
	server.login('suryateja.a16@iiits.in','SUrya5412417')
	server.sendmail('suryateja.a16@iiits.in',mail,randno)
	print("\nAn OTP has been sent to your email id\n")
	{}

#selecting payment method
def payment(cost):
	z=(input("\nAvailable modes of payment:\n\n1.Debitcard\n2.paytm\n\nEnter any particular method of payment:"))
	if(z=="1"):
		Debitcard(cost)
	elif(z=="2"):
		paytm(cost)
	else:
		print("Please enter a valid option!!!\n\n")
		payment(cost)
		
#OTP verification for payment through Debitcard
def otpverificationforcard(otp,y,w,cost):
	if otp==randno:
		print("Dear %s an amount of %d has been deducted form your account with account no %s \n\n" %(y,cost,w))
	else:
		otpagain=input("You have entered wrong OTP \n Do you want to resend OTP(yes/no):")
		if otpagain=='yes':
			otpfun(cost)
			otp=input("Enter One Time Password sent to your Email Address:\n")
			otpverificationforcard(otp,y,w,cost)
		else:
			print("\n\nOops! the transistion is incomplete\n\nTry again!!!\n\n")
			Debitcard(cost)

		
#payment through Debitcard
def Debitcard(cost):
	print("\nSelect any one of the following banks\n\n")
	print("1.SBI\n2.HDFC Bank\n3.Syndicate Bank\n4.Indian Overseas Bank\n5.Bank of India\n")
	q=input("\nYour option:")
	if(q>="1" and q<="5"):
		import getpass
		x=getpass.getpass()
		y=input("Enter user name:")
		w=input("Enter account number:")
		if(len(w)==12):
			otpfun(cost)
			#print("\nOTP has been sent to your mail\n")
			a=input("Enter OTP:")
			otpverificationforcard(a,y,w,cost)
		else:
			print("\nEnter correct account number...\n\n")
			Debitcard(cost)
	else:
		print("\n\nInvalid option!!! choose again...\n")
		Debitcard(cost)
	
#code for phones
def phonedata(cost):
	fp=open("electronics.txt","r")
	a=fp.readline()
	l=[]
	count=0
	print("Available stock of phones...\nThey are in order of company,cost,rating,available stock\n")
	for i in range(0,16):
		print(a)
		l.append(a)
		a=fp.readline()
		count=count+1
	
	try :
		x=int(input("Enter a option:"))
	except:
		print("-------------------------------enter a valid option-----------------------------\n")
		phonedata(cost)
	
	if(x>0 and x<=count):
		print()
		point.write(l[x-1])
		point1.write(l[x-1])
		point1.write('\n')
		r=[]
		r=l[x-1].split(",")
		cost=cost+int(r[1])
		y=input("For furthur shopping enter 'shop' and for payment enter anything:")
		if(y=="shop"):
			print("Your product has been added to cart\n")
			selecting(cost)
		else:
			payment(cost)
	else:
		print("-------------------------------enter a valid option-----------------------------\n")
		phonedata(cost)

#code for telivisons
def telivisondata(cost):
	fp=open("electronics.txt","r")
	a=fp.readline()
	l=[]
	count=0
	print("Available stock of televisions...\nThey are in order of company,cost,rating,available stock\n")
	for i in range(0,16):
		a=fp.readline()
	for i in range(1,11):
		print(a)
		l.append(a)
		a=fp.readline()
		count=count+1
	try :
		x=int(input("Enter a option:"))
	except:
		print("-------------------------------enter a valid option-----------------------------\n")
		telivisondata(cost)
	
	if(x>0 and x<=count):
		print()
		point.write(l[x-1])
		point1.write(l[x-1])
		point1.write('\n')
		r=[]
		r=l[x-1].split(",")
		cost=cost+int(r[1])
		y=input("For furthur shopping enter 'shop' and for payment enter anything:")
		if(y=="shop"):
			print("Your product has been added to cart\n")
			selecting(cost)
		else:
			payment(cost)
	else:
		print("-------------------------------enter a valid option-----------------------------\n")
		telivisondata(cost)

#code for refrigerators
def refrigeratordata(cost):
	fp=open("electronics.txt","r")
	a=fp.readline()
	l=[]
	count=0
	print("Available stock of Refrigerators...\nThey are in order of company,cost,rating,available stock\n")
	for i in range(0,27):
		a=fp.readline()
	for i in range(1,13):
		print(a)
		l.append(a)
		a=fp.readline()
		count=count+1
	try :
		x=int(input("Enter a option:"))
	except:
		print("-------------------------------enter a valid option-----------------------------\n")
		refrigeratordata(cost)
	
	if(x>0 and x<=count):
		print()
		point.write(l[x-1])
		point1.write(l[x-1])
		point1.write('\n')
		r=[]
		r=l[x-1].split(",")
		cost=cost+int(r[1])
		y=input("For furthur shopping enter 'shop' and for payment enter anything:")
		if(y=="shop"):
			print("Your product has been added to cart\n")
			selecting(cost)
		else:
			payment(cost)
	else:
		print("-------------------------------enter a valid option-----------------------------\n")
		refrigeratordata(cost)

#code for laptops
def laptopdata(cost):
	fp=open("electronics.txt","r")
	a=fp.readline()
	l=[]
	count=0
	print("Available stock of laptops...\nThey are in order of company,cost,rating,available stock\n")
	for i in range(0,39):
		a=fp.readline()
	for i in range(1,16):
		print(a)
		l.append(a)
		a=fp.readline()
		count=count+1
	try :
		x=int(input("Enter a option:"))
	except:
		print("-------------------------------enter a valid option-----------------------------\n")
		laptopdata(cost)
	
	if(x>0 and x<=count):
		print()
		point.write(l[x-1])
		point1.write(l[x-1])
		point1.write('\n')
		r=[]
		r=l[x-1].split(",")
		cost=cost+int(r[1])
		y=input("For furthur shopping enter 'shop' and for payment enter anything:")
		if(y=="shop"):
			print("Your product has been added to cart\n")
			selecting(cost)
		else:
			payment(cost)
	else:
		print("-------------------------------enter a valid option-----------------------------\n")
		laptopdata(cost)

#code for earphones and headphones
def earheaddata(cost):
	fp=open("electronics.txt","r")
	a=fp.readline()
	l=[]	
	count=0
	print("Available stock of earphones and headphones...\nThey are in order of company,cost,rating,available stock\n")
	for i in range(0,54):
		a=fp.readline()
	for i in range(1,14):
		print(a)
		l.append(a)
		a=fp.readline()
		count=count+1
	try :
		x=int(input("Enter a option:"))
	except:
		print("-------------------------------enter a valid option-----------------------------\n")
		earheaddata(cost)
	
	if(x>0 and x<=count):
		print()
		point.write(l[x-1])
		point1.write(l[x-1])
		point1.write('\n')
		r=[]
		r=l[x-1].split(",")
		cost=cost+int(r[1])
		y=input("For furthur shopping enter 'shop' and for payment enter anything:")
		if(y=="shop"):
			print("Your product has been added to cart\n")
			selecting(cost)
		else:
			payment(cost)
	else:
		print("-------------------------------enter a valid option-----------------------------\n")
		earheaddata(cost)

#code for love books
def lovebooks(cost):
	fp=open("books.txt","r")
	l=[]
	count=0
	print("Available stock of love story books...\nThey are in order of name,author,cost,rating,available stock\n")
	for i in range(0,28):
		a=fp.readline()
	for i in range(1,11):
		print(a)
		l.append(a)
		a=fp.readline()
		count=count+1
	try :
		x=int(input("Enter a option:"))
	except:
		print("-------------------------------enter a valid option-----------------------------\n")
		lovebooks(cost)
	
	if(x>0 and x<=count):
		print()
		point.write(l[x-1])
		point1.write(l[x-1])
		point1.write('\n')
		r=[]
		r=l[x-1].split(",")
		cost=cost+int(r[1])
		y=input("For furthur shopping enter 'shop' and for payment enter anything:")
		if(y=="shop"):
			print("Your product has been added to cart\n")
			selecting(cost)
		else:
			payment(cost)
	else:
		print("-------------------------------enter a valid option-----------------------------\n")
		lovebooks(cost)

#code for comics
def comicbooks(cost):
	fp=open("books.txt","r")
	l=[]
	count=0
	print("Available stock of comicbooks...\nThey are in order of name,author,cost,rating,available stock\n")
	for i in range(0,18):
		a=fp.readline()
	for i in range(1,11):
		print(a)
		l.append(a)
		a=fp.readline()
		count=count+1
	try :
		x=int(input("Enter a option:"))
	except:
		print("-------------------------------enter a valid option-----------------------------\n")
		comicbooks(cost)
	
	if(x>0 and x<=count):
		print()
		point.write(l[x-1])
		point1.write(l[x-1])
		point1.write('\n')
		r=[]
		r=l[x-1].split(",")
		cost=cost+int(r[1])
		y=input("For furthur shopping enter 'shop' and for payment enter anything:")
		if(y=="shop"):
			print("Your product has been added to cart\n")
			selecting(cost)
		else:
			payment(cost)
	else:
		print("-------------------------------enter a valid option-----------------------------\n")
		comicbooks(cost)

#code for studybooks
def studybooks(cost):
	print("Available stock of studybooks...\nThey are in order of name,author,cost,rating,available stock\n")
	fp=open("books.txt","r")
	a=fp.readline()
	l=[]
	count=0
	for i in range(0,11):
		print(a)
		l.append(a)
		a=fp.readline()
		count=count+1
	try :
		x=int(input("Enter a option:"))
	except:
		print("-------------------------------enter a valid option-----------------------------\n")
		studybooks(cost)
	
	if(x>0 and x<=count):
		print()
		point.write(l[x-1])
		point1.write(l[x-1])
		point1.write('\n')
		r=[]
		r=l[x-1].split(",")
		cost=cost+int(r[1])
		y=input("For furthur shopping enter 'shop' and for payment enter anything:")
		if(y=="shop"):
			print("Your product has been added to cart\n")
			selecting(cost)
		else:
			payment(cost)
	else:
		print("-------------------------------enter a valid option-----------------------------\n")
		studybooks(cost)
		
#code for adventurebooks
def adventurebooks(cost):
	print("Available stock of adventurebooks...\nThey are in order of name,author,cost,rating,available stock\n")
	fp=open("books.txt","r")
	l=[]
	count=0
	for i in range(0,12):
		a=fp.readline()
	for i in range(1,7):
		print(a)
		l.append(a)
		a=fp.readline()
		count=count+1
	try :
		x=int(input("Enter a option:"))
	except:
		print("-------------------------------enter a valid option-----------------------------\n")
		adventurebooks(cost)
	
	if(x>0 and x<=count):
		print()
		point.write(l[x-1])
		point1.write(l[x-1])
		point1.write('\n')
		r=[]
		r=l[x-1].split(",")
		cost=cost+int(r[1])
		y=input("For furthur shopping enter 'shop' and for payment enter anything:")
		if(y=="shop"):
			print("Your product has been added to cart\n")
			selecting(cost)
		else:
			payment(cost)
	else:
		print("-------------------------------enter a valid option-----------------------------\n")
		adventurebooks(cost)

# fuction to shop
def selecting(cost):
	fp=open("data.txt","r")
	print("We have the following categories\n")
	a=fp.readline()
	l=[]
	for i in range(0,3):
		print(a,end="\n")
		l.append(a)
		a=fp.readline()
	x=input("Enter your particular category:")
	if(x=="1"):
		point1.write(l[int(x)-1])
		point1.write('\n')
		chance=input("do you want to search the items or see the list of items(search/anything):")
		if(chance=="search"):
			aa=0
			aa=search("books.txt")
			while(aa!=0):
				aa=search("books.txt")
		print("Select a category in books\n")
		for i in range(0,4):
			print(a)
			a=fp.readline()
		y=(input("Enter here:"))
		
		if(y=="1"):
			studybooks(cost)
		elif(y=="2"):
		 	adventurebooks(cost)
		elif(y=="3"):
			comicbooks(cost)
		elif(y=="4"):
			lovebooks(cost)
		else:
			print("Enter a valid option!!!\n\n")
			selecting(cost)
	elif(x=="2"):
		point1.write(l[int(x)-1])
		point1.write('\n')
		chance=input("do you want to search the items or see the list of items(search/anything):")
		if(chance=="search"):
			aa=0
			aa=search("electronics.txt")
			while(aa!=0):
				aa=search("electronics.txt")
			#selecting(cost)
		print("select a category in electronics\n")
		for i in range(0,4):
			a=fp.readline()
		for i in range(0,5):
			print(a)
			a=fp.readline()
		y=(input("Enter here:"))
		if(y=="1"):
			phonedata(cost)
		elif(y=="2"):
			telivisondata(cost)
		elif(y=="3"):
			refrigeratordata(cost)
		elif(y=="4"):
			laptopdata(cost)
		elif(y=="5"):
			earheaddata(cost)
		else:
			print("Enter a valid option!!!\n\n")
			selecting(cost)
	elif(x=="3"):
		point1.write(l[int(x)-1])
		point1.write('\n')
		chance=input("do you want to search the items or see the list of items(search/anything):")
		if(chance=="search"):
			aa=0
			aa=search("clothes.txt")
			while(aa!=0):
				aa=search("clothes.txt")
		print("select a category in clothes\n")
		for i in range(0,9):
			a=fp.readline()
		for i in range(0,2):
			print(a)
			a=fp.readline()
		y=(input("Enter here:"))
		if(y=="1"):
			for i in range(0,3):
				print(a)
				a=fp.readline()
			menin=int(input("select your choice:"))
			if(menin<=3):
				mensclothes(menin,cost)
			else:
				print("Please enter a valid option!!!\n\n")
				selecting(cost)
				
		elif(y=="2"):
			for i in range(0,3):
				a=fp.readline()
			for i in range(0,4):
				print(a)
				a=fp.readline()
			womin=int(input("select your choice:"))
			if(womin<=4):
				womensclothes(womin,cost)
			else:
				print("Please enter a valid option!!!\n\n")
				selecting(cost)
		else:
			print("Enter a valid option!!!\n\n")
			selecting(cost)
	else:
		print("Enter a valid option!!!\n\n")
		selecting(cost)

# otp verification recursive function
def otpverification(otp,cost):
	if otp==randno:
		print("You have been successfully registered and logged in!!! enjoy shopping\n")
	else:
		otpagain=input("You have entered wrong OTP \n Do you want to resend OTP(yes/no):")
		if otpagain=='yes':
			otpfun(cost)
			otp=input("Enter One Time Password sent to your Email Address:")
			otpverification(otp,cost)
		else:
			print("Registration Failed")

#fuction for getting user password recursive
def password(count,list1,cost):
	if(count!=3):
		import getpass
		y=getpass.getpass()
		count+=1
		if(y==list1[1]):
			print()
			print("Successfully loged in!!! Enjoy shopping\n")
			selecting(cost)
		else:
			print("Your password is incorrect\n")
			password(count,list1,cost)
	else:
		print("You have entered wrong password for 3 times\nplease login again\n")
		registration(cost)

#getting registered
def registration(cost):
	fp=open("users.txt","a+")
	fp1=open("yourdetails.txt","w")
	inp=(input("TO REGISTER ENTER 1,TO LOG IN ENTER 2:"))
	print()
	if(inp=="1"):
		x=input("enter your name:")
		y=input("create your user id:")
		fp.write(y)
		fp.write(",")
		point1.write(y)
		point1.write(" have shopped following items\n\n")
		import getpass
		z=getpass.getpass()
		fp.write(z)
		fp.write(",")
		try:
			w=int(input("phone number:"))
		except:
			print("Enter a valid number!!\n\n")
			registration(cost)
		global mail
		mail=input("enter your email id:")
		fp.write(mail)
		fp.write("\n")
		try:
			otpfun(cost)
		except:
			print("\n\nInvalid credentials!! register again....\n\n")
			registration(cost)
		otp=input("enter OTP sent to your Email Address:")
		otpverification(otp,cost)
		selecting(cost)
		fp.close()
	elif(inp=="2"):
		fp=open("users.txt","r")
		x=input("enter your user id:")
		a=fp.readline()
		while(a!=''):
			list1=a.split(",")
			count=0
			if(x==list1[0]):
				point1.write(x)
				point1.write("  have shopped the following items\n\n")
				mail=list1[2][0:-1]
				password(count,list1,cost)
				break
			a=fp.readline()
		if(a==''):
			print("Your user id is not correct\n")
			registration(cost)
	else:
		print("Enter a valid option")
		registration(cost)
		
# calling registration
registration(cost)
point1.write("---------------------------------------------\n")
print("The shopped items will be delivered shortly....\n\n")
reg=input("Enter 1 to loged out,click anything to shop again:")
if(reg!="1"):
	selecting()
else:
	print("successfully logged out!!!\n\n")
print(" --------------------------------------------------------------------\n*                                                                    * \n*                   Thanks for shopping!!! Visit again...            *\n*                                                                    *\n --------------------------------------------------------------------")

