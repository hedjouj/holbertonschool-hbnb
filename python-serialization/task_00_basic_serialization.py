#!/usr/bin/env python3
"""
Module de sérialisation de base utilisant JSON
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Sérialise un dictionnaire Python vers un fichier JSON
    
    Args:
        data: Dictionnaire Python à sérialiser
        filename: Nom du fichier JSON de sortie
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Erreur lors de la sérialisation: {e}")


def load_and_deserialize(filename):
    """
    Charge et désérialise des données depuis un fichier JSON
    
    Args:
        filename: Nom du fichier JSON d'entrée
        
    Returns:
        dict: Dictionnaire Python désérialisé
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except Exception as e:
        print(f"Erreur lors de la désérialisation: {e}")
        return None
