#!/usr/bin/python3

import uuid
from datetime import datetime


class BaseModel:
    """A class that defines all common attributes for methods"""

    def __init__(self, *args, **kwargs):
        """The initial set of instruction

        This means that all instances created from this class,
        will have all the attributes and values describes here
        """

        if kwargs:
            # Iterate through key-value pairs in kwargs
            for key, value in kwargs.items():
                # Convert 'created_at' and 'updated_at' values to datetime objs
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")

                """Set instance attr with the given key to the new value

                checks if key is != to "__class__" string

                setattr:
                    Uses setattr to set attribute on the self object,
                    with the appropriate key and value
                """
                if key != "__class__":
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

    def __str__(self):
        """
        Returns a human-readable/informal, str repr of an obj
        Returns:
            dict: The object attributes such as id and time of
                  BaseModel and their values
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the update at time attribute with the current tumestamp"""
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """Create a copy of the object dictionary protecting original values"""
        my_dict = self.__dict__.copy()

        """Modifying the time to print in isoformat"""
        my_dict["__class__"] = self.__class__.__name__
        my_dict["updated_at"] = self.updated_at.isoformat()
        my_dict["created_at"] = self.created_at.isoformat()

        return my_dict
