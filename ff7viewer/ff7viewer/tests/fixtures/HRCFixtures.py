FIXTURE = {}

# Empty file fixture
FIXTURE['empty'] = """


""".splitlines(True)

# Malformed Header
FIXTURE['malformed_header'] = """
x:HEADER_BLOCK 2
:SKELETON test
:BONES 0
""".splitlines(True)

# Malformed Skeleton
FIXTURE['malformed_skeleton'] = """
:HEADER_BLOCK 2
x:SKELETON test
:BONES 0
""".splitlines(True)

# Malformed Skeleton
FIXTURE['malformed_bones'] = """
:HEADER_BLOCK 2
:SKELETON test
x:BONES 0
""".splitlines(True)

# Well formed header
FIXTURE['zero_bones'] = """
:HEADER_BLOCK 2
:SKELETON test
:BONES 0
""".splitlines(True)

# Well formed header
FIXTURE['well_formed'] = """
:HEADER_BLOCK 2
:SKELETON test
:BONES 1
""".splitlines(True)

# Bad name - same as root
FIXTURE['bad_bone_name'] = """
root
bad_name
0.12345
0""".splitlines(True)

# Bad parent
FIXTURE['bad_parent_bone'] = """
name
bad_parent
0.12345
0""".splitlines(True)

# Bad float value
FIXTURE['bad_bone_length'] = """
name
parent
bad_number
0""".splitlines(True)

# Zero resources
FIXTURE['zero_resources'] = """
name
root
0.12345
0""".splitlines(True)

# One resource
FIXTURE['single_resource'] = """
name
root
0.12345
1 abcd""".splitlines(True)

# Multiple bones - root parent only
FIXTURE['multiple_bones_single_parent'] = """
child1
root
0.12345
1 abcd

child2
root
0.12345
1 abcd""".splitlines(True)