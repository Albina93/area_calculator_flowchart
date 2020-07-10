import math
user_dimens = []

shapes = {'Square': ['width'], 'Rectangle': ['width', 'length'],
          'Triangle': ['base', 'height'], 'Circle': ['radius']}
print(shapes.keys())
shape_choice = input("Choose shape from above: ").title()
print(shape_choice)

if shape_choice in shapes:
    # print("yes")
    required_dimen = shapes[shape_choice]
    # print(required_dimen)

    for dimen in required_dimen:
        user_dimen = int(input(f"Please enter your {dimen}: "))
        user_dimens.append(user_dimen)
    if shape_choice == 'Square':
        print(f'The result of Square is {user_dimens[0] ** 2}')
    elif shape_choice == 'Triangle':
        print(
            f'This result of Triangle is {user_dimens[0] * user_dimens[-1] // 2}')
    elif shape_choice == 'Rectangle':
        print(f'The result of Rectangle is {user_dimens[0] * user_dimens[-1]}')
    elif shape_choice == 'Circle':
        print(f'The result of Circle is {math.pi * user_dimens[0] ** 2:.3f}')
    # print(user_dimens)
