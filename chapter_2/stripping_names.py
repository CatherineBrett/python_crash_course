# Whitespace characters (tabs and newlines)
persons_name = "\n\tjulian barnes\t"
print(persons_name)

# Strip the whitespace on the left:
print(persons_name.lstrip())

# On the right:
print(persons_name.rstrip())

# Left and right at the same time:
print(persons_name.strip())
