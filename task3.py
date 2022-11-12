print ('welcome to ITI grocary shop!')
x = input ('please select a mode; for customer mode press 1, for owner mode press 2, to exsit press 0')
x = int (x)

mylist= ['apple', 'banana', 'cherry']
cost= {'apple' : 40,'banana' : 30,'cherry' : 70}
while True:
	if x==1:
		print('welcome our customer! you have four options now')
		print ('1- to show our products, please press 1')
		print ('2- to buy from our products please press 2')
		print ('3- to print the bill please prss 3')
		print ('4- to exist please press 0')
		
		y = input ('input your option')
		y = int (y)
		'''z = input ('choose your option now')
		z = int (y)
		a = input ('choose your option now')
		a = int (y)
		b = input ('choose your option now')
		b = int (y)'''
		
		
		
		
		if y == 1:
			print ('our prducts are')
			print (mylist)
				
				
				
		elif y == 2:
		
			z= input('please enter the product name you want to buy')
			
		
		
		elif y == 3:
			
			'''print (cost)'''
			if z== 'apple':                            #غالبا سينتاكس البرينت دا مش صح عشان مش مطلعلي سعر ال ابل بس 
				print(cost,':','apple')
			elif z== 'banana':
				print(cost, ':','banana')
			elif z == 'cherry':
				print (cost,':','cherry')
			
		
		elif y == 4:
			exit ()
				
				
		
	elif x==2:
			print ("Hello our owner! you have five options")
			print ("1- to add new products please press 1")
			print ("2- to show the products please prss 2")
			print ("3- to add cost please press 3")
			print ("4- to change cost please prss 4")
			print ("5- to exsit please prss 5")
				
			a = input ("input your option")
			a = int (a)
				
			'''d = input ("the products are")
			d = int (d)
			e =input ("add cost")
			e = int (e)
			f = input ("change cost")
			f = int (f)
			g = input ("exsit option")
			g = int (g)'''
				
			
			if a == 1:
			
				h = input ('enter the product you want to add')
				mylist.append (h)
				print (mylist)   #ودا سطر ليا انا انما مش المفروض يتحط
						
			
			elif a== 2:
				print (mylist)
						
			
			elif a== 3:
				cost["orange"] = 90
				print (cost)
						
			
			elif a== 4:
				cost ["apple"] = 45
				print (cost)
						
			
			elif a== 5:
				exit()
				
	
	else:
		exit()