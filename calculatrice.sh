#!/bin/bash

echo "Bienvenue dans la calculatrice Bash !"
echo "Entrez le premier nombre :"
read a
echo "Entrez l'opérateur (+, -, *, /) :"
read op
echo "Entrez le deuxième nombre :"
read b

case $op in
    +) result=$((a + b)) ;;
    -) result=$((a - b)) ;;
    \*) result=$((a * b)) ;;
    /) result=$((a / b)) ;;
    *) echo "Opérateur invalide" && exit 1 ;;
esac

echo "Résultat : $result"
