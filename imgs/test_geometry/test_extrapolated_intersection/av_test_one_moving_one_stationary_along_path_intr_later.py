from utils import create_newfig, create_moving_polygon, create_still_polygon, run_or_export

func_code = 'av'
func_name = 'test_one_moving_one_stationary_along_path_intr_later'

def setup_fig01():
    fig, ax, renderer = create_newfig('{}01'.format(func_code), xlim=(-10, 15), ylim=(-1, 18))
    create_moving_polygon(fig, ax, renderer, ((-5, 9), (-8, 7), (-9, 7), (-8, 11), (-8, 11), (-5, 10)), (15, 2))
    create_still_polygon(fig, ax, renderer, ((4, 15.5, 'right'), (5, 12.5, 'botleft'), (0, 11.5), (1, 16.5, 'top')), 'left')

    return fig, ax, '{}01_{}'.format(func_code, func_name)

def setup_fig02():
    fig, ax, renderer = create_newfig('{}02'.format(func_code), xlim=(-2, 21), ylim=(-7, 11))
    create_moving_polygon(fig, ax, renderer, ((4.5, -0.5), (3.5, -2.5), (1.5, -3.5), (-0.5, 0.5), (-0.5, 1.5), (1.5, 2.5)), (13, 3))
    create_still_polygon(fig, ax, renderer, ((8, 6), (10, 6), (10, 4), (8, 4)))

    return fig, ax, '{}02_{}'.format(func_code, func_name)

def setup_fig03():
    fig, ax, renderer = create_newfig('{}03'.format(func_code), xlim=(-3, 25), ylim=(-1, 21))
    create_moving_polygon(fig, ax, renderer, ((3, 17.5), (3, 16.5), (1, 15.5), (-1, 15.5), (-1, 18.5), (0, 19.5)), (18, -7))
    create_still_polygon(fig, ax, renderer, ((14.5, 13), (14.5, 9), (12.5, 9), (11.5, 12), (12.5, 13)))

    return fig, ax, '{}03_{}'.format(func_code, func_name)
    
def setup_fig04():
    fig, ax, renderer = create_newfig('{}04'.format(func_code), xlim=(-10, 8), ylim=(-12, 6))
    create_moving_polygon(fig, ax, renderer, ((-5, 2.5), (-8, 0.5), (-9, 1.5), (-8, 4.5), (-6, 4.5)), (12, -10))
    create_still_polygon(fig, ax, renderer, ((6, -1.5), (5, -3.5), (2, -2.5), (3, 0.5)))

    return fig, ax, '{}04_{}'.format(func_code, func_name)

run_or_export(setup_fig01, setup_fig02, setup_fig03, setup_fig04)