cost=123
randno=123456

def otpverificationforcard(otp,y,w):
	if otp==randno:
		print("Dear %s an amount of %d has been deducted form your account with account no %s \n\n" %(y,cost,w))
	else:
		otpagain=input("You have entered wrong OTP \n Do you want to resend OTP(yes/no):")
		if otpagain=='yes':
			#otpfun()
			otp=input("Enter One Time Password sent to your Email Address:\n")
			otpverificationforcard(otp,y,w)
		else:
			print("\n\nOops! the transistion is incomplete\n\nTry again!!!\n\n")
			Debitcard()


def Debitcard():
	x=input("Enter your ATM pin:")
	y=input("Enter user name:")
	w=input("Enter account number:")
	z=input("Enter expiry date:")
	#otp()
	print("\nOTP has been sent to your mail\n")
	a=int(input("Enter OTP:"))
	otpverificationforcard(a,y,w)
	print

Debitcard()
