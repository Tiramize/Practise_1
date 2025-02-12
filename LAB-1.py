def get_numbers_from_user():
    user_input = input("Введите три целых числа, разделенных пробелами: ")
    numbers = user_input.split()  
   
    return [int(num) for num in numbers]

def reverse_list(input_list):
    if len(input_list) != 3:
        raise ValueError("Список должен содержать ровно три числа разделенные пробелом.")
    
    reversed_list = [input_list[2], input_list[1], input_list[0]]
    
    return reversed_list

try:
    original_list = get_numbers_from_user()
    new_list = reverse_list(original_list)
    print("Перевернутый список:", new_list) 
except ValueError:
    print("Ошибка:", ValueError)