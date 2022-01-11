def guess():
	i=5
	while(True):
	
		if (i<1):
			print("Game over!!")
			break
		else:
			print("Guess left: ", i)
			n= int(input("Enter the number : "))
			if (n==18):
				print("Congrates!!")
				print("You have successfully guessed the number with:",6-i, "guess")
				break
			elif(n<18):
				print("Wrong choice!!")
				if(i>1):
					print("Enter greater than", n)
			elif(n>18):
				print("Wrong choice!!")
				if(i>1):
					print("Enter smaller than", n)
		i-=1
guess()
while(True):
	c= input("Do you want to play again? y/n ")
	if (c=='y'):
		guess()
	else:
		print("Thanks for playing!!")
		break
	
	