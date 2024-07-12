test = 123
code = "test = 456"
exec(code, globals)
print(test)

code = """
def dynamic_function(x, y):
    return x + y
"""

globals_dict, locals_dict = safe_exec(code)
dynamic_function = locals_dict['dynamic_function']

result = dynamic_function(10, 20)
print(result)  # Output: 30