def function(a, b):
    try:
        return int(a) + int(b)
    except ValueError:
        return "Error: Invalid input types"

result = function(5, '10')
print(result)
result = function(5, '10a')
print(result) 