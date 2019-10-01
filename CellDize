from random import randint, choice

CELL_SIZE = {
    'cell_1': [(131, 154, 26, 61), (24, 154, 133, 61)],
    'cell_2': [(131, 219, 26, 61), (24, 219, 133, 61)],
    'cell_3': [(131, 283, 26, 61), (24, 283, 133, 61)],
    'cell_4': [(131, 348, 26, 61), (24, 348, 133, 61)],
    'cell_5': [(131, 412, 26, 61), (24, 412, 133, 61)],
    'cell_6': [(131, 477, 26, 61), (24, 477, 133, 61)],
    'cell_7': [(131, 541, 26, 62), (24, 541, 133, 62)],
    'cell_8': [(131, 606, 26, 61), (24, 606, 133, 61)],
    'cell_9': [(131, 671, 26, 61), (24, 671, 133, 61)],

    'cell_10': [(161, 735, 61, 26), (161, 735, 61, 141)],
    'cell_11': [(226, 735, 61, 26), (226, 735, 61, 141)],
    'cell_12': [(291, 735, 60, 26), (291, 735, 60, 141)],
    'cell_13': [(355, 735, 60, 26), (355, 735, 60, 141)],
    'cell_14': [(418, 735, 61, 26), (418, 735, 61, 141)],
    'cell_15': [(483, 735, 62, 26), (483, 735, 62, 141)],
    'cell_16': [(548, 735, 62, 26), (548, 735, 62, 141)],
    'cell_17': [(613, 735, 61, 26), (613, 735, 61, 141)],
    'cell_18': [(677, 735, 62, 26), (677, 735, 62, 141)],

    'cell_19': [(743, 671, 26, 60), (743, 671, 136, 60)],
    'cell_20': [(743, 607, 26, 61), (743, 607, 136, 61)],
    'cell_21': [(743, 542, 26, 61), (743, 542, 136, 61)],
    'cell_22': [(743, 477, 26, 61), (743, 477, 136, 61)],
    'cell_23': [(743, 413, 26, 61), (743, 413, 136, 61)],
    'cell_24': [(743, 348, 26, 61), (743, 348, 136, 61)],
    'cell_25': [(743, 284, 26, 61), (743, 284, 136, 61)],
    'cell_26': [(743, 219, 26, 61), (743, 219, 136, 61)],
    'cell_27': [(743, 154, 26, 61), (743, 154, 136, 61)],

    'cell_28': [(677, 124, 62, 26), (677, 21, 62, 130)],
    'cell_29': [(613, 124, 61, 26), (613, 21, 61, 130)],
    'cell_30': [(548, 124, 61, 26), (548, 21, 61, 130)],
    'cell_31': [(483, 124, 61, 26), (483, 21, 61, 130)],
    'cell_32': [(419, 124, 61, 26), (419, 21, 61, 130)],
    'cell_33': [(354, 124, 61, 26), (354, 21, 61, 130)],
    'cell_34': [(290, 124, 61, 26), (290, 21, 61, 130)],
    'cell_35': [(226, 124, 60, 26), (226, 21, 60, 130)],
    'cell_36': [(161, 124, 62, 26), (161, 21, 62, 130)],
    'corner_1': [(24, 21, 133, 129)],
    'corner_2': [(24, 735, 133, 142)],
    'corner_3': [(743, 735, 136, 141)],
    'corner_4': [(743, 22, 136, 128)],

}


def generate_game_field():
    random_color = ['blue', 'red', 'orange', 'green', 'grey', 'green4', 'black', 'pink', 'brown', 'cyan', 'yellow']

    start_cell = 1
    name_cell = 'cell_'
    color_template = generate_template()
    print(color_template)
    for color_dig in color_template:
        color = choice(random_color)
        for i in range(color_dig):
            cell = name_cell + str(start_cell)
            print(cell, color)
            start_cell += 1
        cell = name_cell + str(start_cell)
        print(cell, 'white')
        start_cell += 1
        random_color.remove(color)
            # pygame.draw.rect(self.screen, (THECOLORS[random_color]), CELL_SIZE[temp_name_cell][0])


def generate_template():
    min_entity, max_entity = 2, 4
    template_point = 0
    color_template = []
    while template_point < 27:
        random_dig = randint(min_entity, max_entity)
        color_template.append(random_dig)
        template_point += random_dig
        if template_point > 27:
            template_point = 0
            color_template.clear()
    return color_template


if __name__ == '__main__':
    generate_game_field()
