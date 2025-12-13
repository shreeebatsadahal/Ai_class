approved_ids = ["A101","B205","C303","D410"]
employee_id = input("Enter employee ID: ")
print(f"Is the employee ID approved? :{employee_id in approved_ids} ")
print(f"Is Z999 not in approved IDS?: {'Z999' not in approved_ids} ")

# 2. Question: Write two separate print statements:
# Use the in operator to check if employee_id is in approved_ids.
# Use the not in operator to check if "Z999" is not in approved_ids.
# approved_ids = ["A101"
# ,
# "B205"
# ,
# "C303"
# ,
# "D410"]
# employee_id = input("Enter employee ID: ")