# un programme qui permet de récupérer l’occupation du parking « FR_MTP_GARE » toutes
#les 10 secondes pendant 5 minutes et qui sauvegarde ces données dans un fichier.
import time
import requests
from lxml import etree

periode=int(input("Période:"))
minute=int(periode)*60
duration=int(input("Seconde:"))
p=int(minute/duration)
for i in range (p):
    response=requests.get("https://data.montpellier3m.fr/sites/default/files/ressources/FR_MTP_COME.xml")
    print(response.text)
    f1=open("FR_MTP_COME.txt","w", encoding='utf8')
    f1.write(response.text)
    f1.close()
    tree = etree.parse("FR_MTP_COME.txt")
    for user in tree.xpath("Name"):
        print('Nom du parking :',user.text)
    for user1 in tree.xpath("Total"):
        print('Nombre total de places :',user1.text)
    for user2 in tree.xpath("Free"):
        print('Nombre de places libres :',user2.text)
    x=int((user1.text))-int((user2.text))
    print('Nombres de places occupées:' ,x)
    temps=int(time.time())
    seconds = temps=int(time.time())
    local_time = time.ctime(seconds)
    print("Local time:", local_time)
    time.sleep(duration)
