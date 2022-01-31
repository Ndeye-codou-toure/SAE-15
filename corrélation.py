from math import sqrt

def moyenne1(L1):
	somme = 0
	for i in L1:
		somme+=i
		moy1=sum(L1)/len(L1)
	return moy1

def moyenne2(L2):
	somme = 0
	for i in L2:
		somme+=i
		moy2=sum(L2)/len(L2)
	return moy2


def sigma(L1):
	mean = sum(L1)/len(L1)
	var = sum((l-mean)**2 for l in L1) / len(L1)
	ecart = sqrt(var)
	return ecart

	
def sigma(L2):
	mean2 = sum(L2)/len(L2)
	var2 = sum((i-mean2)**2 for i in L2) / len(L2)
	ecart2 = sqrt(var2)
	return ecart2



f4=open('Data.txt','r', encoding="utf8")
lines=f4.readlines()
f4.close()
Lvoiture=[]
Lvelo=[]

for do in lines:
    L=do.split('   ')
    x=float(L[1].strip('%'))
    y=float(L[2].strip('%\n'))
    Lvoiture.append(x)
    Lvelo.append(y)
print(Lvoiture,Lvelo)
# Lvoiture est la liste des pourcentages de voiture et Lvelo est celle de velo
    
# Covariance
somme=0
for x in range(len(Lvoiture)):
    a=Lvoiture[x]-moyenne1(Lvoiture)
    b=Lvelo[x]-moyenne2(Lvelo)
    c=a*b
    somme=somme+c
cov=somme/len(Lvoiture)


# Corrélation
Cor=cov/sqrt(sigma(Lvoiture)*sigma(Lvelo))
print("Covariance:",cov,"corrélation:",Cor)
