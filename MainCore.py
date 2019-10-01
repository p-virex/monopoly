import pygame
import sys
from pygame.color import THECOLORS
from random import choice, randint

from CellSize import CELL_SIZE
from pprint import pprint


class RenderCore(object):
    SIZE = (1200, 900)

    def __init__(self):
        pygame.init()
        self.session_cell_info = dict()
        self.screen = pygame.display.set_mode(self.SIZE)
        self.screen.fill(THECOLORS['white'])
        self.back_ground = pygame.image.load("empty_template.jpg")
        self.random_color = ['blue', 'red', 'orange', 'green', 'grey', 'green4']
        self.color_tag = False
        self.run_render()

    def run_render(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pos = pygame.mouse.get_pos()
                        self.check_mouse_position(pos)
                        print(pos)
            self.screen.blit(self.back_ground, (0, 0))
            if not self.color_tag:
                self.generate_game_field()
                # self.debug_fill_color_cell()

    def debug_fill_color_cell(self):
        name_cell = 'cell_'
        for i in range(1, 37):  # start position 1, total 36 cell (37 - 1) + 4 corner
            temp_name_cell = name_cell + str(i)
            a_random_color = choice(self.random_color)
            self.session_cell_info[temp_name_cell] = {'size': CELL_SIZE[temp_name_cell][0], 'color': a_random_color}
            pygame.draw.rect(self.screen, (THECOLORS[a_random_color]), CELL_SIZE[temp_name_cell][0])
        self.color_tag = True
        pygame.display.flip()

    def generate_game_field(self):
        random_color = ['blue', 'red', 'orange', 'green', 'grey', 'green4', 'black', 'pink', 'brown', 'cyan', 'yellow']
        start_cell = 1
        name_cell = 'cell_'
        color_template = self.generate_template()
        self.session_cell_info['color_template'] = color_template
        end_cycle = False
        pprint(self.session_cell_info)

        for color_dig in color_template:
            color = choice(random_color)
            for i in range(color_dig):
                cell = name_cell + str(start_cell)
                self.session_cell_info[cell] = {'color': color}
                pygame.draw.rect(self.screen, (THECOLORS[color]), CELL_SIZE[cell][0])
                start_cell += 1
                if start_cell > 36:
                    end_cycle = True
                    break
            if end_cycle:
                break
            cell = name_cell + str(start_cell)
            self.session_cell_info[cell] = {'color': 'white'}
            pygame.draw.rect(self.screen, (THECOLORS['white']), CELL_SIZE[cell][-1])
            start_cell += 1
            random_color.remove(color)
        self.color_tag = True
        pygame.display.flip()

    @staticmethod
    def check_mouse_position(pos):
        if all([pos[0] > 160, pos[0] < 740, pos[-1] > 155, pos[-1] < 730]):
            print('Mouse out field')
            return
        if any([pos[0] < 24, pos[0] > 880, pos[-1] < 16, pos[-1] > 880]):
            print('Mouse out field')
            return
        print('Mouse in game field')
        if pos[0] < 156:
            for name_cell in CELL_SIZE.keys():
                next_name_cell = name_cell.split('_')[0] + '_'
                next_index = int(name_cell.split('_')[-1]) + 1
                next_cell = next_name_cell + str(next_index)
                msg = 'Cell: {}, position: {}, cell pos: {}, next cell pos: {}'
                print(msg.format(name_cell, pos[-1], CELL_SIZE[name_cell][0][1], CELL_SIZE[next_cell][0][1]))
                if all([CELL_SIZE[name_cell][0][1] < pos[-1], CELL_SIZE[next_cell][0][1] > pos[-1]]):
                    print(name_cell, '!!!')
                    break
                if next_index == 10:
                    print('Cell not found: next > %s, prev > %s' % (next_cell, name_cell))
                    break
        if pos[0] > 744:
            cell_index = [19, 20, 21, 22, 23, 24, 25, 26, 27]
            for name_cell in CELL_SIZE.keys()[::-1]:
                ind_cell = int(name_cell.split('_')[-1])
                if ind_cell not in cell_index:
                    continue
                next_cell = 'cell_{}'.format(ind_cell + 1)
                msg = 'Cell: {}, position: {}, cell pos: {}, next cell pos: {}'
                print(msg.format(name_cell, pos[-1], CELL_SIZE[name_cell][0][1], CELL_SIZE[next_cell][0][1]))
                if all([pos[-1] < CELL_SIZE[name_cell][0][1], CELL_SIZE[next_cell][0][1] > pos[-1]]):
                    print(name_cell)
                    break

    @staticmethod
    def generate_template():
        min_entity, max_entity = 2, 4
        template_point = 0
        color_template = []
        while template_point < 28:
            random_dig = randint(min_entity, max_entity)
            color_template.append(random_dig)
            template_point += random_dig
            if template_point > 28:
                template_point = 0
                color_template.clear()
        print(len(color_template), '!!!!')
        return color_template


if __name__ == '__main__':
    RenderCore()
