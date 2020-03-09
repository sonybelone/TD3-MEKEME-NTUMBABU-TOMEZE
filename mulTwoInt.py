import sys

def mul(a,b):
	return a*b
if __name__=="__main__":
	if len(sys.argv)>3:
		print( "veuillez entrez uniquement deux nombres s'il vous plait")
	elif len(sys.argv)==3:
		a= int(sys.argv[1])
		b= int(sys.argv[2])
		print(mul(a,b))
	elif len(sys.argv)==2:
		a= int(sys.argv[1])
		b= int(input("inserer deuxieme valeur s'il vous plait: "))
		print (mul(a,b))
	else:
		a= int (input("inserer premiere valeur s'il vous plait: "))
		b= int(input("inserer deuxieme valeur s'il vous plait: "))
		print (mul(a,b))

