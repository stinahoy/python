pakke_liste = []
while True:
    command = input("Skriv 'l' for å legge til, 'd' for å slette, 'p' for print, 'q' for quit: ")
    if command == 'l':
        ting = input("Legg til: ")
        pakke_liste.append(ting)
    elif command == 'd':
        ting = input("Slett: ")
        pakke_liste.remove(ting) if ting in pakke_liste else print("Ting ikke funnet.")
    elif command == 'p':
        print("Pakke liste:", pakke_liste)
    elif command == 'q':
        break
    else:
        print("Kommando ikke funnet.")