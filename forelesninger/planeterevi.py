planeter = ["Merkur", "Venus", "Jorden", "Mars", "jupiter", "Saturn", "Uranus", "Neptun"]
tyngdekraft = [3.7, 8.87, 9.807, 3.721, 24.79, 10.44, 8.87, 11.15]

kjør = True
while kjør:
    print("/n ======================================")
    print("== Hva er din vekt på en annen planet? ==")
    print(" ========================================")

    for planetnummer in range (len(planeter)):
        print(f"{planetnummer + 1} - {planeter[planetnummer]}")

    valgt_planetnummer = input("/n Velg en planet ved å skrive inn et tall: ")
    valgt_planetnummer = int(valgt_planetnummer)

    valgt_planet = planeter[valgt_planetnummer]
    print(f"Du har valgt {valgt_planet}.")

    din_vekt = float(input("Hva er din vekt på jorden?"))

    #utregninger 
    jordens_tyngdekraft = tyngdekraft[2]
    din_masse = din_vekt / jordens_tyngdekraft
    din_vekt_pa_planet = round(din_masse * tyngdekraft[valgt_planetnummer], 2)

    print(f"Din vekt på planeten {valgt_planet} er {din_vekt_pa_planet} kg, som har tyngdekraft {tyngdekraft[valgt_planet]}")

    en_gang_til = input("Vil du prøve igjen? Y/N")

    kjør = (en_gang_til.upper() == "Y")

print("Takk fro at du spilte!")
