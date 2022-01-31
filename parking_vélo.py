import requests
from lxml import etree
import time
parkings=['FR_MTP_ANTI','FR_MTP_COME','FR_MTP_CORU','FR_MTP_EURO','FR_MTP_FOCH','FR_MTP_GAMB','FR_MTP_GARE','FR_MTP_TRIA','FR_MTP_ARCT','FR_MTP_PITO','FR_MTP_CIRC','FR_MTP_SABI','FR_MTP_GARC','FR_MTP_SABL','FR_MTP_MOSS','FR_STJ_SJLC','FR_MTP_MEDC','FR_MTP_OCCI','FR_CAS_VICA','FR_MTP_GA109','FR_MTP_GA250','FR_CAS_CDGA','FR_MTP_ARCE','FR_MTP_POLY']
Toville=0 #Le nombre total des parkings de toute la ville
FrVille=0 #Le nombre total des parkings libre de toute la ville
ToVelo=0 #Le nombre total des places du velo de toute la ville
AvVelo=0 #le nombre total des places occupées du vélo de toute la ville
# Pour saisir la période et la durée
period=int(input("Période(min):"))
period=period*60
duration=int(input("duration(sec):"))
t=int(period/duration)
# t est le nombre de fois que ce programme doit être exécuté.
for p in range(t):
    for x in parkings: #la liste "parkings" contient les noms des fichiers de chaque zone. On fait un boucle pour récupérer des données de chaque zone.
        #Récupérer les données et les mettre dans un nouveau fichier
        data=requests.get(f"https://data.montpellier3m.fr/sites/default/files/ressources/{x}.xml")
        f1=open(f"{x}.txt","w",encoding='utf8')
        f1.write(data.text)
        f1.close()
        #trier des données et choisir le nombre des places libre et des places total.
        tree=etree.parse(f"{x}.txt")
        a=0
        b=0
        for user in tree.xpath("Total"):
            total=int(user.text)
            a=a+total
        for user in tree.xpath("Free"):
            libre=int(user.text)
            b=b+libre
        # ajouter des nombre dans le valeur du "nombre total". C'est pour obtenir la somme de tous les parkings et tous les parkings libres
        Toville=Toville+a
        FrVille=FrVille+b
    # Récupérer des données de places du vélo
    data2=requests.get("https://data.montpellier3m.fr/sites/default/files/ressources/TAM_MMM_VELOMAG.xml")
    f3=open("VELO.txt","w",encoding='utf8')
    f3.write(data2.text)
    f3.close()
    # Trier
    tree2=etree.parse("VELO.txt")
    for user in tree2.xpath('//si/@av'):
        av=int(user)
        AvVelo=AvVelo+av
    for user in tree2.xpath('//si/@to'):
        to=int(user)
        ToVelo=ToVelo+to
    PourcentVelo=AvVelo/ToVelo # le valeur : Places occupées du vélo / Places total du vélo
    PercentVoiture=FrVille/Toville # le valeur : Parkings libres/ Parkings total
    PercentVoiture=1-PercentVoiture # pour obtenir le taux d'occupation de voiture
    temps=time.time()
    temps=time.ctime(temps)
    t=temps.split(' ')
    f2=open("Data.txt","a",encoding='utf8')
    f2.write(f"{t[3]}    {round(PercentVoiture*100, 2)}%    {round(PourcentVelo*100, 2)}%")
    f2.write('\n')
    f2.close()
    time.sleep(duration)