#un programme qui récupére les données utiles du parking de Comédie

import requests
from lxml import etree
response=requests.get("https://data.montpellier3m.fr/sites/default/files/ressources/FR_MTP_COME.xml")
print(response.text)
f1=open("FR_MTP_COME.txt","w", encoding='utf8')
f1.write(response.text)
f1.close()
tree = etree.parse("FR_MTP_COME.txt")
for user in tree.xpath("Name"):
    print('Nom du parking :',user.text)
for user in tree.xpath("Total"):
    print('Nombre total de places :',user.text)
for user in tree.xpath("Free"):
    print('Nombre de places libres :',user.text)