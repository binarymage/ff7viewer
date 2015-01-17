# Excetions
class BoneLengthError(Exception):
    """Inappropriate floating point length"""
    pass

class EmptyResourceError(Exception):
    """Empty resource given"""
    pass

class DuplicateResourceError(Exception):
    """Duplicate resource given"""
    pass

# The Bone class
class Bone(object):
    """A Bone"""

    def __init__(self, name):
        """Initialise the class with the given name"""
        self.name = name
        self.resources = []

    def set_length(self, l):
        """Set the length of this bone"""
        try:
            self.length = float(l)
        except ValueError:
            raise BoneLengthError
        except:
            raise

    def add_resource(self, r):
        """Add the name of a resource attached to this bone"""
        if not r:
            raise EmptyResourceError
        if r in self.resources:
            raise DuplicateResourceError
        self.resources.append(r)
