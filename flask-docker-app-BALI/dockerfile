# Utiliser l'image officielle de Python
FROM python:3.9

# Définir le répertoire de travail à /app
WORKDIR /app

# Copier les fichiers de requirements.txt et app.py dans le conteneur
COPY requirements.txt requirements.txt
COPY app.py app.py

# Installer les dépendances
RUN pip install --upgrade pip

RUN pip install -r requirements.txt

# Exposer le port 5000 pour l'application Flask
EXPOSE 5000

# Exécuter l'application Flask
CMD ["python", "app.py"]

