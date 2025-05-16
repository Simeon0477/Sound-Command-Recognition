import sounddevice as sd
import numpy as np
import whisper
import time

# Chargement du modèle Whisper local (plus petit et plus rapide)
# Options disponibles: "tiny", "base", "small", "medium", "large"
# Choisissez selon votre puissance de calcul
model_size = "base"
print(f"Chargement du modèle Whisper {model_size}...")
model = whisper.load_model(model_size)
print("Modèle chargé!")

def listen_for_command():
    """Écoute et transcrit une commande vocale en utilisant Whisper localement"""
    # Paramètres d'enregistrement
    sample_rate = 16000  # Hz
    duration = 3  # secondes
    
    print("Prêt à écouter votre commande...")
    print("Parlez maintenant...")
    
    try:
        # Enregistrer l'audio
        recording = sd.rec(int(duration * sample_rate), 
                          samplerate=sample_rate, 
                          channels=1,
                          dtype='float32')
        sd.wait()  # Attendre la fin de l'enregistrement
        print("Enregistrement terminé!")
        
        # Normaliser l'audio
        audio_data = recording.flatten()
        
        # Transcrire avec Whisper local
        print("Transcription en cours...")
        result = model.transcribe(audio_data, language="fr")
        transcription = result["text"].lower().strip()
        
        return transcription
        
    except Exception as e:
        print(f"Erreur: {e}")
        return ""

def parse_direction(text):
    """Analyse le texte pour en extraire la direction"""
    directions = {
        "gauche": ["gauche", "à gauche", "vers la gauche"],
        "droite": ["droite", "à droite", "vers la droite"],
        "avant": ["avant", "en avant", "devant", "tout droit"],
        "arrière": ["arrière", "en arrière", "recule", "reculer"]
    }
    
    # Cherche une correspondance entre le texte et les directions connues
    for direction, keywords in directions.items():
        if any(keyword in text for keyword in keywords):
            return direction
    
    return "direction non reconnue"

def main():
    while True:
        try:
            # Écoute la commande vocale
            transcription = listen_for_command()
            
            if transcription:
                print(f"Texte reconnu: '{transcription}'")
                
                # Analyse la direction
                direction = parse_direction(transcription)
                print(f"Direction reconnue: {direction}")
                
                # Si l'utilisateur dit "stop" ou "arrêt", quitte la boucle
                if "stop" in transcription or "arrêt" in transcription:
                    print("Arrêt du programme.")
                    break
            
            time.sleep(1)  # Petite pause avant d'écouter à nouveau
            
        except KeyboardInterrupt:
            print("Programme interrompu par l'utilisateur")
            break
        except Exception as e:
            print(f"Erreur: {e}")

if __name__ == "__main__":
    main()
