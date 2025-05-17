# Sound-Command and FaceID Recognition - GPU 
Test du model Whisper de Open AI pour la reconnaissance directionnelle dans le but du projet robotique de l'ETAN
### ESP32CAM
### Arduino Mega
### Deploiement et traitement Local (GPU)

# Projet de Reconnaissance de Commandes Sonores

Ce projet utilise le modèle Whisper de OpenAI pour la reconnaissance vocale.

## Prérequis

- **Python 3.7 ou supérieur**
- **Pip** (inclus avec Python)
- **Anaconda**

## Installation

1. **Installez Whisper avec Git  et de sounddevice:**  
   ```bash
   - conda create -n **nom_env** python=3.9 (ideal)
   - conda activate **nom_env**
   - pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118 (Verifiez la version CUDA compatible avec votre materielle)
   - conda install -c conda-forge ffmpeg (Pour lire l'audio[Whisper])

   pip install git+https://github.com/openai/whisper.git
   pip install sounddevice

### Résumé

Cette version inclut l'installation de Whisper directement via Git avec `pip`.

# Face-Recognition - GPU (InsightFace + ONNXRuntimes)
## Prérequis
   - torch GPU
   - C++ Build Tools (visual studio)
   - onnxruntimes-gpu

# installation
   pip install insightface[all]
## Reconnaissance faciale en locale GPU avec ESP32 via WIFI
### Architecture 
   1. ESP32CAM
      - Capture une image (format JPEG).
      - Envoie l’image via une requête HTTP POST à une API Flask.
      - Reçoit une réponse JSON.
      - Affiche le flux vidéo, et superpose un carré + "TRUE" si reconnu.
   2. API Flask
      - Reçoit l’image.
      - Utilise InsightFace pour comparer le visage avec une base de visages connus.
      - Renvoie true si le visage est reconnu avec une bonne similarité.
