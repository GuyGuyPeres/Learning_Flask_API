def divide (dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor can not be ZERO --> 0")
    
    
    return dividend/divisor




students = [
    {"name": "Bob", "grades": [80, 85]},
    {"name": "Rolf", "grades": []},
    {"name": "Jen", "grades": [90, 95]}
]

for student in students:
    try:
        average = divide(sum(student["grades"]), len(student["grades"]))
        print(student["name"], "average:", average)
    except ZeroDivisionError as e:
        print("Error:", student["name"], "has no grades.")
    else:
        print("Processed successfully.")
    finally:
        print("Finished processing", student["name"])
        print("\n")