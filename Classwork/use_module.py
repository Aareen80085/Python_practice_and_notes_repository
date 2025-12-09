# import custom_module
# import custom_module as nums 
# # from custom_module import y
# # print(custom_module.x)
# # print(y)
# print(nums.x)

# import custom_module as validate
# input_value = int(input("Enter a number: "))
# print(validate.validate(input_value))

try:
    print(x)
except Exception as e:
    print("default", e)
else:
    print("inside else")
finally:
    print("inside finally")
