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
