import unittest
from cStringIO import StringIO
from ff7viewer import Bone

from ff7viewer import HRCFile
from tests.fixtures import HRCFixtures

class Test_HRCFileTest(unittest.TestCase):
    def setUp(self):
        """Initialise a class with the name 'test.hrc'"""
        self.hrc = HRCFile.HRCFile("test.hrc")

    def test_HRCFile_create_with_name(self):
        """Test for successful creation of the class with the given name"""
        self.assertEquals(self.hrc.filename, "test.hrc")

    def test_HRCFile_parse_empty_header(self):
        """Test that an empty header raises an exception"""
        with self.assertRaises(IOError):
            self.hrc.parse_header(HRCFixtures.FIXTURE['empty'])

    def test_HRCFile_parse_malformed_header(self):
        """Test that a malformed header raises an exception"""
        with self.assertRaises(HRCFile.HeaderBlockError):
            self.hrc.parse_header(HRCFixtures.FIXTURE['malformed_header'])

    def test_HRCFile_parse_malformed_skeleton(self):
        """Test that a malformed skeleton raises an exception"""
        with self.assertRaises(HRCFile.MalformedSkeletonError):
            self.hrc.parse_header(HRCFixtures.FIXTURE['malformed_skeleton'])

    def test_HRCFile_parse_header(self):
        """Test that a parsed header returns the correct information"""
        (v, s, b, _) = self.hrc.parse_header(HRCFixtures.FIXTURE['well_formed'])
        self.assertEquals(v, 2)
        self.assertEquals(s, "test")
        self.assertEquals(b, 1)

    def test_HRCFile_parse_zero_bones(self):
        """Test to ensure that 0 bones raises an exception"""
        self.hrc.bones = 0
        with self.assertRaises(HRCFile.BoneNumberError):
            self.hrc.parse_bones(HRCFixtures.FIXTURE['empty'])

    def test_HRCFile_parse_empty_bones(self):
        """Test to ensure that empty bones raises an exception"""
        self.hrc.bones = 1
        with self.assertRaises(ValueError):
            self.hrc.parse_bones(HRCFixtures.FIXTURE['empty'])

    def test_HRCFile_parse_one_bone_used_name(self):
        """Test to ensure that no bone has the same name as another"""
        self.hrc.bones = 1
        with self.assertRaises(KeyError):
            self.hrc.parse_bones(HRCFixtures.FIXTURE['bad_bone_name'])

    def test_HRCFile_parse_one_bone_bad_parent(self):
        """Test to ensure the bone has a valid parent"""
        self.hrc.bones = 1
        with self.assertRaises(KeyError):
            self.hrc.parse_bones(HRCFixtures.FIXTURE['bad_parent_bone'])

if __name__ == '__main__':
    unittest.main()
