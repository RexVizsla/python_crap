# !!!MONITOR RAM USAGE WHEN USING THE SCRIPT TO AVOID CRASHES!!!

primzahlen = []
keine_primzahlen = []
startwert = 2
reichweite = 1000000

for testzahl in range(startwert, reichweite-1 + startwert):
    if testzahl in keine_primzahlen:
        pass
    else:
        print(testzahl)
        for vielfaches in range(reichweite-1):
            keine_primzahlen.append(testzahl*vielfaches)
            vielfaches = vielfaches + 1
        primzahlen.append(testzahl)
print("Die ermittelten Primzahlen lauten: " + str(primzahlen))