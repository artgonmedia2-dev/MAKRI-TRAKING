# Utiliser une image Python officielle très légère
FROM python:3.11-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de dépendances et installer
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste de l'application
COPY . .

# Exposer le port que Cloud Run utilise par défaut
EXPOSE 8080

# Démarrer le serveur Gunicorn au lieu du serveur de dev Flask
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]
