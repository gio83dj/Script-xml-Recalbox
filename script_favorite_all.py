import xml.etree.ElementTree as ET
import xml.etree.ElementTree as OT

# Crea file txt
file_out = open('out.txt','w')
file_out.writelines("------TERMINALE------" + "\n")
file_out.close()

file_out = open('differences.txt','w')
file_out.close()

# Dichiarazione Variabili
numero_gioco_new = 0
numero_gioco_bkp = 0
numero_preferiti_new = 0
numero_preferiti_bkp = 0

# --- Caricare  gli xml ---
tree_bkp = ET.parse('gamelist.backup.xml')
root_bkp = tree_bkp.getroot()
tree_new = OT.parse('gamelist.xml')
root_new = tree_new.getroot()

# --- Conta tag favourite true---
for gioco in root_new.findall('game'):
    nome = gioco.find('name').text
    f = open('nomi.txt','a')                        
    f.write('    --------------------------------   ' + "\n")
    f.write(nome + "\n")
    preferito = gioco.find('favorite')
    if preferito != None:                                   #Quando un tag non esiste alla variabile viene assegnata None che è uno statement diverso da True o 0 che si chiama None
        if preferito.text == "true":
            print ("Lista NEW: ", "PREFERITO: SI", nome)
            numero_preferiti_new += 1
        else:
            print ("Lista NEW: ", "PREFERITO: NO", nome)
    else:
        print ("Lista NEW: ", "PREFERITO: NO", nome)

for gioco in root_bkp.findall('game'):
    nome = gioco.find('name').text
    preferito = gioco.find('favorite')
    if preferito != None:                                   #Quando un tag non esiste alla variabile viene assegnata None che è uno statement diverso da True o 0 che si chiama None
        if preferito.text == "true":
            print ("Lista BKP: ", "PREFERITO: SI", nome)
            numero_preferiti_bkp += 1
        else:
            print ("Lista BKP: ", "PREFERITO: NO", nome)
    else:
        print ("Lista BKP: ", "PREFERITO: NO", nome)

# Ricerca variabile Favorite BKP
for gioco in root_bkp.findall('game'):
    nome = gioco.find('name').text
    path_bkp = gioco.find('path').text                      # Controlla il nome del gioco dal tag path
    nome_path_bkp = path_bkp[2:-4]                          # Toglie i due caratteri iniziali (./) e i quattro finali (.zip)
    preferito_bkp = gioco.find('favorite')
    if preferito_bkp != None:
        preferito_bkp = gioco.find('favorite').text
    else:
        preferito_bkp = "false"
    file_out = open('out.txt','a')                          # Scrive su file il valore del preferito bkp
    file_out.write('    --------------------------------   ' + "\n")
    file_out.write('Gioco: ' + nome + "\n")
    file_out.write('Preferito BKP: ' + preferito_bkp + "\n")
    file_out.write('path_bkp: ' + path_bkp + "\n")
    file_out.close()
 
# Ricerca variabile Favorite NEW nello stesso gioco BKP
    for gioco_new in root_new.iter('game'):
        path_new = gioco_new.find('path').text              # Controlla il nome del gioco dal tag path
        if path_new == path_bkp:                            # Confronta i nomi se sono uguali con quello BKP
            preferito_new = gioco_new.find('favorite')
            if preferito_new != None:                       # Controlla se esiste tag favorite
                preferito_new = gioco_new.find('favorite').text
            else:                                           # Se non esiste tag favorite lo crea impostandolo false
                gioco_new.append(OT.Element('favorite'))
                gioco_new.find('favorite').text = "false"
                preferito_new = "false"
                
            file_out = open('out.txt','a')                  # Scrive su file il valore del preferito new
            file_out.write("Preferito NEW: " + preferito_new + "\n")
            file_out.close()

# Confronta il preferito bkp con quello new e le differenze le scrive sul file differences.txt come lista nomi giochi     
            if preferito_bkp != preferito_new:
                file_out = open('differences.txt','a')
                file_out.write(path_new + "\n") 
                file_out.close()
                if preferito_bkp == "true":                # Controlla se il valore BKP era true lo cambia in true anche sul NEW
                    gioco_new.find('favorite').text = "true"
                    file_out = open('differences.txt','a')
                    file_out.write(nome + "CAMBIATO IN PREFERITO" + "\n" + "\n") 
                    file_out.close()


#   Salvare file xml di output
tree_new.write('output.xml')

#   Stampa a Terminale varie informazioni
for gioco in root_new.findall('game'):
    numero_gioco_new = numero_gioco_new + 1
print ("Numero di gioco NEW Totali: ", numero_gioco_new)
for gioco in root_bkp.findall('game'):
    numero_gioco_bkp = numero_gioco_bkp + 1
print ("Numero di gioco BKP Totali: ", numero_gioco_bkp)
print ("Numero Preferiti NEW: ", numero_preferiti_new)
print ("Numero Preferiti BKP: ", numero_preferiti_bkp)


"""
#   Rimuovere un gioco
    if gioco.find('name').text == "Fantasia":
        root_bkp.remove(gioco)
#   Settare attributo tag
    gioco.set('desc', preferito_new)
"""
    #print (gioco_new.find('image').text)
#   Cambiare contenuto di un Tag
    #if gioco.find('desc') != None:
    #    gioco.find('desc').text = preferito_new