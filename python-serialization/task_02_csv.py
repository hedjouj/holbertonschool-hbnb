#!/usr/bin/env python3
"""
Module de conversion CSV vers JSON
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convertit un fichier CSV en format JSON
    
    Args:
        csv_filename (str): Nom du fichier CSV à convertir
        
    Returns:
        bool: True si la conversion réussit, False sinon
    """
    try:
        # Liste pour stocker les dictionnaires de chaque ligne
        data_list = []
        
        # Ouvrir et lire le fichier CSV
        with open(csv_filename, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            
            # Convertir chaque ligne en dictionnaire
            for row in csv_reader:
                data_list.append(row)
        
        # Sérialiser vers JSON et sauvegarder
        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data_list, json_file, indent=4)
        
        return True
        
    except FileNotFoundError:
        print(f"Erreur: Le fichier {csv_filename} n'a pas été trouvé.")
        return False
    except Exception as e:
        print(f"Erreur lors de la conversion: {e}")
        return False