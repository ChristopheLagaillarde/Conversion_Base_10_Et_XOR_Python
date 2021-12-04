try:
    def conversion_base_10(valeur_binaire):
        valeur_base10 = int(0)

        for i in range(len(valeur_binaire) - 1):
            if valeur_binaire[i] == "1":
                valeur_base10 += (int(valeur_binaire[i]) * (2 ** ((len(valeur_binaire) - 1) - i)))

            elif valeur_binaire[i] == "0":
                continue

            else:
                raise ValueError

        return valeur_base10

    def xor_binaire(binaire_1, binaire_2):

        xor = str("")

        for i in range(len(binaire_1)):

            if binaire_1[i] == binaire_2[i]:
                xor += "0"

            else:
                xor += "1"

        return xor

    def egalise_taille_binaire():
        global valeur_binaire_1
        global valeur_binaire_2

        while len(valeur_binaire_1) != len(valeur_binaire_2):

            if len(valeur_binaire_1) < len(valeur_binaire_2):
                valeur_binaire_1 = "0" + valeur_binaire_1

            if len(valeur_binaire_2) < len(valeur_binaire_1):
                valeur_binaire_2 = "0" + valeur_binaire_2
        return


    valeur_binaire_1 = str(input("Saisir la première valeur binaire"))
    valeur_base10_1 = conversion_base_10(valeur_binaire_1)

    valeur_binaire_2 = str(input("Saisir la première valeur binaire"))
    valeur_base10_2 = conversion_base_10(valeur_binaire_2)

    egalise_taille_binaire()

    xor_obtenu = xor_binaire(valeur_binaire_1, valeur_binaire_2)

    print(valeur_base10_1)
    print(valeur_base10_2)
    print(xor_obtenu)

except ValueError:
    print("saisie non valide")