num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def format_numbers(numbers : list[list[int]]):
    """
    利用列表推導式將每項整數轉換為字串，

    並用格式化的方式將字串填充為置右的8個字元，

    呈現的將會是包含3個子列表的二維列表
    """
    return [ # 二維列表
        ['{:>8}'.format(str(x)) for x in get_even_squares(numbers)], # 一維列表
        ['{:>8}'.format(str(y)) for y in get_odd_cubes(numbers)], # 一維列表
        ['{:>8}'.format(str(z)) for z in get_sliced_list(numbers)] # 一維列表
    ]

def get_even_squares(num_list : list[int]):
    """ 利用列表推導式回傳 num_list 所有偶數平方之列表 """
    return [x * x for x in num_list if x % 2 == 0]

def get_odd_cubes(num_list : list[int]):
    """ 利用迴圈回傳 num_list 裡所有奇數三次方之列表 """
    odd_cubes_list = []
    for x in num_list:
        if(x % 2 != 0):
            odd_cubes_list.append(x * x * x)
    return odd_cubes_list

def get_sliced_list(num_list : list[int]):
    """ 利用切片回傳 num_list 裡第5個元素到最後1個元素之列表 """
    return num_list[4:]

result_list = format_numbers(num_list)

# ','.join([item for item in row]) // 在每一項字串物件後加上','
# '\n'.join([###### for row in result_list]) // 在每一列後加上換行符號
print('\n'.join([','.join([item for item in row]) for row in result_list]))
