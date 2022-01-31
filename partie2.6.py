#un programme qui donne le pourcentage de places libres pour chaque parking ainsi que le
#pourcentage de places libres dans toute la ville.Enfin le jour et l'heure
import time
import requests
from lxml import etree
PAR=['FR_MTP_ANTI','FR_MTP_COME','FR_MTP_CORU','FR_MTP_EURO','FR_MTP_FOCH','FR_MTP_GAMB','FR_MTP_GARE','FR_MTP_TRIA','FR_MTP_ARCT',
'FR_MTP_PITO','FR_MTP_CIRC','FR_MTP_SABI','FR_MTP_GARC','FR_MTP_SABL','FR_MTP_MOSS','FR_STJ_SJLC','FR_MTP_MEDC','FR_MTP_OCCI','FR_CAS_VICA','FR_MTP_GA109','FR_MTP_GA250','FR_CAS_CDGA','FR_MTP_ARCE','FR_MTP_POLY']
y=0
w=0
for i in PAR:
    x=requests.get(f'https://data.montpellier3m.fr/sites/default/files/ressources/{i}.xml')
    f1=open(f'{i}.txt',"w", encoding='utf8')
    f1.write(x.text)
    f1.close()
    tree = etree.parse(f"{i}.txt")   #retirer les donnees
    for user in tree.xpath("Name"):    #extrait les données de name
        print('Nom du parking :',user.text)
    for user1 in tree.xpath("Total"):   
        print('Places totales :',user1.text)
    for user2 in tree.xpath("Free"):
        print('Nombre de places libres :',user2.text)
        #calcul du pourcentage, free*100/Total
        x=int((user2.text))*100/int(user1.text)
        print('Pourcentage:' ,round(x,2) ,'%')
    #le pourcentage de places libres dans toute la ville
    y=int((user1.text))+ y
    w=int((user2.text))+w
print('Places totales de toute la ville:' ,y)
print('Nombres de places libres de toute la ville:' ,w)
pour=int((w))*100/int(y)
print('Pourcentage de places libres dans toute la ville' ,round(pour,2) ,'%')
temps=int(time.time())
seconds = temps=int(time.time())
local_time = time.ctime(seconds)
print("Aujourd'hui à:", local_time)