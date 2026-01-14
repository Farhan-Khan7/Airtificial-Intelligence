info = {
    'author': 'Airtificial Intelligence',
    'version': '1.0.0',
    'description': 'A collection of dictionaries for various applications.',
    'license': 'MIT',
}

# print(info['author'])  # Output: Airtificial Intelligence
# print(info.get('version'))  # Output: 1.0.0

dict_keys = info.keys()
dict_values = info.values()

print(dict_keys)    # Output: ['author', 'version', 'description', 'license']
print(dict_values)  # Output: ['Airtificial Intelligence', '1.0.0', 'A collection of dictionaries for various applications.', 'MIT']

