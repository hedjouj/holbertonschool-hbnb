#!/usr/bin/env python3
"""
Module de sérialisation et désérialisation XML
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Sérialise un dictionnaire Python vers un fichier XML
    
    Args:
        dictionary (dict): Dictionnaire à sérialiser
        filename (str): Nom du fichier XML de sortie
    """
    try:
        # Créer l'élément racine
        root = ET.Element("data")
        
        # Itérer à travers les éléments du dictionnaire
        for key, value in dictionary.items():
            # Créer un élément enfant pour chaque clé-valeur
            child = ET.SubElement(root, key)
            child.text = str(value)  # Convertir en string pour XML
        
        # Créer l'arbre XML et l'écrire dans le fichier
        tree = ET.ElementTree(root)
        tree.write(filename, encoding='utf-8', xml_declaration=True)
        
    except Exception as e:
        print(f"Erreur lors de la sérialisation XML: {e}")


def deserialize_from_xml(filename):
    """
    Désérialise un fichier XML vers un dictionnaire Python
    
    Args:
        filename (str): Nom du fichier XML d'entrée
        
    Returns:
        dict: Dictionnaire désérialisé ou None si erreur
    """
    try:
        # Parser le fichier XML
        tree = ET.parse(filename)
        root = tree.getroot()
        
        # Reconstruire le dictionnaire
        dictionary = {}
        for child in root:
            dictionary[child.tag] = child.text
        
        return dictionary
        
    except FileNotFoundError:
        print(f"Erreur: Le fichier {filename} n'a pas été trouvé.")
        return None
    except ET.ParseError as e:
        print(f"Erreur de parsing XML: {e}")
        return None
    except Exception as e:
        print(f"Erreur lors de la désérialisation XML: {e}")
        return None