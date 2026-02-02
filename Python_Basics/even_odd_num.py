def even_odd_num(num):
    if num%2 == 0:
        return 'Even'
    else:
        return 'Odd'

try:
    user_input = int(input("Enter the number here - "))
    print("Given number is ",even_odd_num(user_input))
except ValueError:
    print("❌ Please enter a valid number! Only Integers are allowed.")
except Exception as e:
    print(f"Unexpected error occured : {e}")