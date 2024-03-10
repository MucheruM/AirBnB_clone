#!/usr/bin/python3

import json

from models.base_model import BaseModel


class FileStorage:
    """
    Manages the storage of objects in a dictionary and
    saving them to a JSON file.
    """

    __file_path = "file.json"
    __objects = {}

    """
    This code maps class names to their corresponding class obj
    Its a dictionary that holds mapping betwen class names and their associated
    class objects, facilitating dynamic instantiation based on class names.
    """
    __class_map = {
        'BaseModel': BaseModel,
        }

    def all(self):
        """
        Retrieve all objects stored in the dictionary.

        Return:
           dict: A dictionary containing all stored objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Adds a new object to the dictionary using a Key

        Args:
            obj: An object to be stored.
        """
        obj_class_name = obj.__class__.__name__
        obj_id = obj.id
        obj_key = f"{obj_class_name}.{obj_id}"

        self.__objects[obj_key] = obj

    def save(self):
        """
        Save the serialized objects dict (ser_obj_dict) to a JSON file.
        """
        ser_obj_dict = {}

        for key, obj_instance in self.__objects.items():
            ser_obj_dict[key] = obj_instance.to_dict()

        # Save the serialized objects dictionary to a JSON file
        with open(self.__file_path, "w", encoding="utf-8") as json_file:
            json_file.write(json.dumps(ser_obj_dict))

    def reload(self):
        """
        Reloads objects from a JSON file, updating the class state

        Attempts to read serialized objests from the specified JSON file.
        If successful, dynamically creates new instances based on stored data.

        If the file is not found, no action is taken.

        NB: Uses the '__class__' attribute for dynamic class instantiation.
        """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as json_file:
                diser_obj_dict = json.load(json_file)

            for key, obj_inst in diser_obj_dict.items():
                class_name = obj_inst['__class__']

                self.__objects[key] = self.__class_map[class_name](**obj_inst)
        except FileNotFoundError:
            pass
