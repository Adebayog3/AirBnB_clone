#!/usr/bin/python3
"""Defines the BaseModel class."""
from uuid import uuid4
from datetime import datetime
#import models
class BaseModel:
    """Represent the BaseModel of the HBnB project."""
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.
        
        Args:
            *args (any): Unused.
            **kwargs (dict): key/value pairs of attributes.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue

                
        elif key in ["created_at", "updated_at"]:
                    value = datetime.fromisoformat(value)
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self) # added

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Update time and save change into__object (in FileStorage)
        """
        self.updated_at = datetime.now()
        models.storage.save() # added

    def to_dict(self):
        """
         dictionary representation fo every intance
        time format: %Y-%m-%dT%H:%M:%S.%f
        key __class__ added to identify every intance
        Returns:
            dict: dictionary
        """
        return {
            "__class__": self.__class__.__name__,
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            **self.__dict__
        }
