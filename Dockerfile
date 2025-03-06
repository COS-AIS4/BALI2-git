# Utiliser une image de base Python
FROM python:3.9-slim

# Copier les fichiers de l'application dans le conteneur
WORKDIR /app
COPY app.py /app

# Installer les dépendances
RUN pip install flask

# Exposer le port de l'application
EXPOSE 5000

# Définir la commande pour exécuter l'application
CMD ["python", "app.py"]

