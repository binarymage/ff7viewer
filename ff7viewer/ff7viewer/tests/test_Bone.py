import unittest
import random

from ff7viewer import Bone

class Test_Bone(unittest.TestCase):
    def setUp(self):
        self.bone = Bone.Bone("root")

    def test_Bone_create_root(self):
        """Make sure the root bone has a name"""
        self.assertEquals(self.bone.name, "root")

    def test_Bone_set_random_length(self):
        """Make a random length and assign to the child bone"""
        num = random.random()
        self.bone.set_length(num)

        # Check to see if it was stored correctly
        self.assertEquals(self.bone.length, num)

    def test_Bone_set_non_numerical_length(self):
        """Check for non-numerical length"""
        with self.assertRaises(Bone.BoneLengthError):
            self.bone.set_length("Non numerical value!")

    def test_Bone_set_empty_resource_name(self):
        """Ensure an empty resource name raises an exception"""
        with self.assertRaises(Bone.EmptyResourceError):
            self.bone.add_resource("")

    def test_Bone_set_one_resource_name(self):
        # Ensure that the resource name is stored correctly
        self.bone.add_resource("aaab")
        self.assertIn("aaab", self.bone.resources)

    def test_Bone_set_duplicate_resource_name(self):
        """Ensure that duplicate resources raise an exception"""
        self.bone.add_resource("aaab")
        with self.assertRaises(Bone.DuplicateResourceError):
            self.bone.add_resource("aaab")

if __name__ == '__main__':
    unittest.main()
