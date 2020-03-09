import sys


def  add (a, b):
	return a+b
if __name__=="__main__":

	if len(sys.argv) > 3:
		print ("falt")
	elif len(sys.argv)==3:
		a = sys.argv[1]
		b = sys.argv[2]
		print(sys.argv)
		print(add(a,b))
	else :
		print("insere le que deux nombre")



#	try :
#		x=int(x)
#	except:
#		 print("Impossible d'insere plus de deux valeur")

		#print("le contenue ne doit pas depasse plus de 3")

#	except Exception as e:
#		print(e)

