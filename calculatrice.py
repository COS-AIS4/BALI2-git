def calculatrice():
    print("Bienvenue dans la calculatrice Python !")
    
    try:
        a = float(input("Entrez le premier nombre : "))
        op = input("Entrez l'opérateur (+, -, *, /) : ")
        b = float(input("Entrez le deuxième nombre : "))

        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        elif op == '*':
            result = a * b
        elif op == '/':
            if b == 0:
                print("Erreur : Division par zéro !")
                return
            result = a / b
        else:
            print("Opérateur invalide.")
            return

        print(f"Résultat : {result}")

    except ValueError:
        print("Erreur : Veuillez entrer des nombres valides.")

if __name__ == "__main__":
    calculatrice()
