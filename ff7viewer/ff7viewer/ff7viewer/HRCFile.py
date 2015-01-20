import Bone
import Node

class HeaderBlockError(Exception):
    """Invalid or malformed :HEADER_BLOCK line"""
    pass

class MalformedSkeletonError(Exception):
    """Malformed :SKELETON line"""
    pass

class MalformedBoneError(Exception):
    """Malformed :BONES line"""
    pass

class BoneNumberError(Exception):
    """Invalid number of bones"""
    pass

class DuplicateBoneError(Exception):
    """Duplicated bone name"""
    pass

class InvalidParentBoneError(Exception):
    """Invalid parent bone"""
    pass

class HRCFile(object):
    """An HRC file"""

    def __init__(self, filename):
        """Initialise the class with the given filename"""
        self.filename = filename
        self.bones = 0
        self.bone_list = []
        root = Bone.Bone("root")
        self.bone_tree = Node.Node(root)

    def readfile(self):
        """Read the HRC file"""
        with open(self.filename, "r") as f:
            self._read(f)
            close(f)

    def _strip_blank_lines(self, lines):
        """Remove leading blank lines"""
        for l in lines:
            if l == "\n":
                lines = lines[1:]
            else:
                break
        return lines

    def parse_header(self, lines):
        """Parse the HRC header for information"""
        # Remove any leading empty lines
        lines = self._strip_blank_lines(lines)

        # Empty file
        if not lines:
            raise IOError
        
        # Get the header
        (type, version) = lines[0].split(" ")
        if type != ":HEADER_BLOCK":
            raise HeaderBlockError

        # Get the name
        (type, skeleton) = lines[1].split(" ")
        if type != ":SKELETON":
            raise MalformedSkeletonError

        # Get the number of bones
        (type, bones) = lines[2].split(" ")
        if type != ":BONES":
            raise MalformedBoneError

        # Make sure the number is a positive integer greater than 0
        if bones.find(".") != -1:
            raise BoneNumberError
        try:
            bones = int(bones)
        except ValueError:
            raise BoneNumberError
        if bones <= 0:
            raise BoneNumberError

        return (int(version), skeleton.strip(), int(bones), lines[3:])

    def _make_bone(self, body):
        """Create a bone from the given text"""
        body = self._strip_blank_lines(body)
        if not body:
            raise ValueError
        name = body[0].strip()
        parent = body[1].strip()
        length = float(body[2].strip())
        resources = body[3].strip().split(" ")
        
        if name in self.bone_list:
            raise DuplicateBoneError

        if parent not in self.bone_list:
            raise InvalidParentBoneError

        bone = Bone.Bone(name)
        bone.set_length(length)
        for i in range(int(resources[0])):
            bone.add_resource(resources[i + 1])

        return (bone, parent, body[4:])

    def _find_node(self, node):
        """Find the bone in the tree"""
        for i in iter(self.bone_tree):
            if i.data.name == node:
                return i

        return None

    def parse_bones(self, body):
        """Parse bones into the bone tree"""
        for i in range(self.bones):
            try:
                (bone, parent, body) = self._make_bone(body)
                Node.Node(bone, self._find_node(parent))
            except:
                raise

    def _read(self, f):
        """Read the given file stream and parse it"""
        # Read the lines into memory
        lines = f.readlines();
        try:
            (self.version, self.skeleton_name, self.bones, body) = self.parse(lines)
            # self.parse_bones(body)
        except:
            raise

