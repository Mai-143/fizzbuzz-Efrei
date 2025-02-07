# Utilisation de l'image Python légère
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers du projet dans le conteneur
COPY . .

# Définir PYTHONPATH pour inclure le dossier de l'application
ENV PYTHONPATH=/app

# Installer pytest et pytest-cov
RUN pip install pytest pytest-cov

# Exécuter les tests avec pytest et générer un rapport de couverture
CMD ["pytest", "--cov=.", "--cov-report=term-missing"]
