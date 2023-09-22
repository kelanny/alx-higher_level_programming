#!/usr/bin/python3
"""
The module contain a Base class.
"""
import json
import csv

class Base:
    """This is a Base class representation.
    The class is the base of all other classes.
    It manages the id attribute in all future classes.

    Attributes:
        __nb_objects (int): Private class attribute.
        id (int): The unique id of each object related to the Base class.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ This initializes an instance of the Base class.

        Args:
            id (int): A unique integer assigned to a  base class instance.
    """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON serialization of a list of dicts.

        Args:
            list_dictionaries (list): A list of dictionaries.
        """

        if list_dictionaries is None or list_dictionaries == []:
            return ("[]")
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a json string representation of list with Base class instanses

        Args:
            list_objs (list): A list of inherited class instances.
        """

        filename = f"{cls.__name__}.json"
        with open(filename, 'w') as jfile:
            if list_objs is None:
                jfile.write("[]")
            else:
                list_dicts = [item.to_dictionary() for item in list_objs]
                jfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Deserialize a JSON string representation to a python object.
        """

        if json_string is None or json_string == "[]":
            return ([])
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """Create and return an instance with all attributes already set.
        Args:
            None.
        """

        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new_class = cls(1, 1)
            else:
                new_class = cls(1)
            new_class.update(**dictionary)
            return (new_class)

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a file.
        """

        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, 'r') as jfile:
                list_dicts = Base.from_json_string(jfile.read())
                return ([cls.create(**dic) for dic in list_dicts])
        except IOError:
            return([])

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves serialized objects to a csv file.

        Args:
            list_objs (list): List of serialized objects.

        """

        filename = str(cls.__name__) + ".csv"

        with open(filename, 'w') as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.
         Reads from `<cls.__name__>.csv`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([key, int(value)] for key, value in obj.items())
                                   for obj in list_dicts]
                return ([cls.create(**d) for d in list_dicts])
        except IOError:
            return ([])
