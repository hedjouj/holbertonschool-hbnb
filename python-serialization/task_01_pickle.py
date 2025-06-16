#!/usr/bin/env python3
"""
Module de sérialisation d'objets personnalisés avec pickle
"""
import pickle


class CustomObject:
    """
    Classe personnalisée pour démontrer la sérialisation avec pickle
    """
    
    def __init__(self, name, age, is_student):
        """
        Initialise l'objet CustomObject
        
        Args:
            name (str): Nom de la personne
            age (int): Âge de la personne
            is_student (bool): Statut étudiant
        """
        self.name = name
        self.age = age
        self.is_student = is_student
    
    def display(self):
        """
        Affiche les attributs de l'objet
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")
    
    def serialize(self, filename):
        """
        Sérialise l'objet actuel vers un fichier
        
        Args:
            filename (str): Nom du fichier de sortie
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Erreur lors de la sérialisation: {e}")
    
    @classmethod
    def deserialize(cls, filename):
        """
        Désérialise un objet depuis un fichier
        
        Args:
            filename (str): Nom du fichier d'entrée
            
        Returns:
            CustomObject: Instance désérialisée ou None si erreur
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.UnpicklingError, EOFError) as e:
            print(f"Erreur lors de la désérialisation: {e}")
            return None
        except Exception as e:
            print(f"Erreur inattendue: {e}")
            return None
