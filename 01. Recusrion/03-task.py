def draw_figure(num: int):

    if num == 0:
        return
    print('*' * num)
    draw_figure(num - 1)
    print('#' * num)


draw_figure(5)
