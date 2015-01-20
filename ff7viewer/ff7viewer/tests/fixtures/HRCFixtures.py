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
x:BONES 0.12345
""".splitlines(True)

# Zero bones
FIXTURE['zero_bones'] = """
:HEADER_BLOCK 2
:SKELETON test
:BONES 0
""".splitlines(True)

# Non-integer bones
FIXTURE['non_int_bones'] = """
:HEADER_BLOCK 2
:SKELETON test
:BONES 1.0
""".splitlines(True)

# Nnegative bones
FIXTURE['negative_bones'] = """
:HEADER_BLOCK 2
:SKELETON test
:BONES -3
""".splitlines(True)

# Well formed header
FIXTURE['well_formed'] = """
:HEADER_BLOCK 2
:SKELETON test
:BONES 1
""".splitlines(True)

# Duplicate bone name
FIXTURE['bad_parent_bone'] = """
root
root
0.12345
0""".splitlines(True)

# Bad parent
FIXTURE['bad_parent_bone'] = """
name
bad_parent
0.12345
0""".splitlines(True)

# Zero resources - okay
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

# Multiple bones
FIXTURE['multiple_bones'] = """
child1
root
0.12345
1 abcd

child2
root
0.12345
1 abcd""".splitlines(True)