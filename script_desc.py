import xml.etree.ElementTree as ET
import xml.etree.ElementTree as OT
#f = open('out.txt','w')
#print >>f,'------TERMINALE------'
#f = open('found.txt','w')
#print >>f,'------TROVATI------'
numero_gioco_ita = 0
numero_gioco = 0
numero_preferiti = 0
numero_preferiti_ing = 0

# --- caricati  gli xml ---
listanuova_tree = ET.parse('gamelist.xml')
root_ing = listanuova_tree.getroot()
listaita_tree = OT.parse('gamelist_ita.xml')
root_ita = listaita_tree.getroot()


# --- conta tag favourite ---

for gioco in root_ita.findall('game'):
    nome = gioco.find('name').text
    preferito = gioco.find('favorite')
    if preferito != None:  #Quando un tag non esiste alla variabile viene assegnata None che è uno statement diverso da True o 0 che si chiama None
        print ("Lista ITA: ", preferito.text, nome)
        numero_preferiti += 1


for gioco in root_ing.findall('game'):
    nome = gioco.find('name').text
    preferito = gioco.find('favorite')
    if preferito != None:  #Quando un tag non esiste alla variabile viene assegnata None che è uno statement diverso da True o 0 che si chiama None
        print ("Lista NUOVA: ", preferito.text, nome)
        numero_preferiti_ing += 1

# --- trova tag descrizione
"""
for gioco in root_ita.findall('game'):
    nome = gioco.find('name').text
    path_ita = gioco.find('path').text
    nome_path_ita = path_ita[2:-4]  # Toglie i due caratteri iniziali (./) e i quattro finali (.zip)
    descrizione_ita = gioco.find('desc')
    if descrizione_ita != None:
        descrizione_ita = gioco.find('desc').text
        descrizione_ita = descrizione_ita[:999]  ##  TRONCA LA LUNGHEZZA DELLA DESCRIZIONE A UN TOT DI CARATTERI
    else:
        descrizione_ita = ""
    print("Gioco: ", nome)
    print("Descrizione Italiana: ", descrizione_ita)
    print("    --------------------------------   ")
    for gioco_nuovi in root_ing.iter('game'):
        path_ing = gioco_nuovi.find('path').text
        #print (path_ing)
        if path_ing == path_ita:
            #print(gioco_nuovi.find('desc').text)
            descrizione_ing = gioco_nuovi.find('desc')
            if descrizione_ing != None:
                descrizione_ing = gioco_nuovi.find('desc').text
            else:
                descrizione_ing = ""
            print("Descrizione Inglese: ", descrizione_ing)
    print("path_ita: ", path_ita)
    print("    --------------------------------   ")
    print("    --------------------------------   ")
    print("    --------------------------------   ")
"""
# Ricerca variabile Descrizione Inglese

for gioco in root_ing.findall('game'):
    nome = gioco.find('name').text
    path_ing = gioco.find('path').text
    nome_path_ing = path_ing[2:-4]  # Toglie i due caratteri iniziali (./) e i quattro finali (.zip)
    descrizione_ing = gioco.find('desc')
    if descrizione_ing != None:
        descrizione_ing = gioco.find('desc').text
    else:
        descrizione_ing = ""
    print("Gioco: ", nome)
    print("Descrizione Inglese: ", descrizione_ing)
    print("path_ing: ", path_ing)
    print("    --------------------------------   ")
    
# Ricerca variabile Descrizione Italiana

    for gioco_nuovi in root_ita.iter('game'):
        path_ita = gioco_nuovi.find('path').text
        #print (path_ing)
        if path_ita == path_ing:
            #print(gioco_nuovi.find('desc').text)
            descrizione_ita = gioco_nuovi.find('desc')
            if descrizione_ita != None:
                descrizione_ita = gioco_nuovi.find('desc').text
                descrizione_ita = descrizione_ita[:999]  ##  TRONCA LA LUNGHEZZA DELLA DESCRIZIONE A UN TOT DI CARATTERI
            else:
                descrizione_ita = ""
            print("Descrizione Italiana: ", descrizione_ita)
            print (gioco_nuovi.find('image').text)
#   Cambiare contenuto di un Tag
    if gioco.find('desc') != None:
        gioco.find('desc').text = descrizione_ita
"""
#   Rimuovere un gioco
    if gioco.find('name').text == "Fantasia":
        root_ing.remove(gioco)
#   Settare attributo tag
    gioco.set('desc', descrizione_ita)
    print("    --------------------------------   ")
    print("    --------------------------------   ")
"""
#   Salvare file xml di output
listanuova_tree.write('output.xml')
    
# --- conta titoli ---

for gioco in root_ita.findall('game'):
    numero_gioco_ita = numero_gioco_ita + 1
print ("Numero di gioco Italiano Totali: ", numero_gioco_ita)
for gioco in root_ing.findall('game'):
    numero_gioco = numero_gioco + 1
print ("Numero di gioco Nuovi Totali: ", numero_gioco)
print ("Numero Preferiti Italiano: ", numero_preferiti)
print ("Numero Preferiti Inglese: ", numero_preferiti_ing)