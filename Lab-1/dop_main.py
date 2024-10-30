import sys, time

def make_image(mat: list[list[int]]) -> str:
    return '\n'.join([''.join(map(str, row)) for row in mat])

RED = '\u001b[41m'
WHITE = '\u001b[47m'
BLACK = '\033[40m'
END = '\u001b[0m'
SEP = '\n' + '─' + '\n'

plot_list = [[0 for _ in range(10)] for _ in range(10)]
exist = f'{BLACK}  {END}'
not_exist = f'{WHITE}  {END}'

for i in range(10):
    if i in (0, 1, 4, 5, 8, 9):
        plot_list[i] = [exist for _ in range(10)]
    elif i in (2, 3):
        plot_list[i] = [not_exist for _ in range(4)] + [exist]
        plot_list[i] = plot_list[i] + plot_list[i][::-1]
    else:
        plot_list[i] = [not_exist, exist, exist, not_exist, not_exist]
        plot_list[i] = plot_list[i] + plot_list[i][::-1]

mirror_plot = plot_list[5:-1]
plot_list = plot_list[1:5]

f = True
while True:
    actual = plot_list + mirror_plot if f else mirror_plot + plot_list
    f = not f
    print(make_image(actual))
    time.sleep(.5)
    for i in range(8):
        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')
