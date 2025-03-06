# Utiliser une image Python légère
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier de l'application
COPY app.py /app

# Installer Flask
RUN pip install flask

# Exposer le port de l'application
EXPOSE 5000

# Lancer l'application
CMD ["python", "app.py"]

