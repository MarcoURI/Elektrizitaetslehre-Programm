# file_loader

from PIL import Image
import os

def load_image(file_path):
    """
    Lädt ein Bild von einem lokalen Pfad
    
    Args:
        file_path: Pfad zur Bilddatei
    
    Returns:
        PIL.Image: Das geladene Bild oder None bei Fehler
    """
    try:
        if os.path.exists(file_path):
            return Image.open(file_path)
        else:
            print(f"Fehler: Datei nicht gefunden: {file_path}")
            return None
    except Exception as e:
        print(f"Fehler beim Laden des Bildes: {e}")
        return None

def load_images_from_directory(directory_path, extensions=('.jpg', '.jpeg', '.png')):
    """
    Lädt alle Bilder aus einem Verzeichnis
    
    Args:
        directory_path: Pfad zum Verzeichnis mit den Bildern
        extensions: Tuple mit erlaubten Dateierweiterungen
    
    Returns:
        dict: Dictionary mit Dateinamen als Schlüssel und PIL.Image als Werte
    """
    images = {}
    
    if not os.path.isdir(directory_path):
        print(f"Fehler: Verzeichnis nicht gefunden: {directory_path}")
        return images
    
    for filename in os.listdir(directory_path):
        if filename.lower().endswith(extensions):
            file_path = os.path.join(directory_path, filename)
            img = load_image(file_path)
            if img:
                images[filename] = img
    
    return images