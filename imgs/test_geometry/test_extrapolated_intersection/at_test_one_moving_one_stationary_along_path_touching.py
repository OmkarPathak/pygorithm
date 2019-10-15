from utils import create_newfig, create_moving_polygon, create_still_polygon, run_or_export

func_code = 'at'
func_name = 'test_one_moving_one_stationary_along_path_touching'

def setup_fig01():
    fig, ax, renderer = create_newfig('{}01'.format(func_code), xlim=(-1, 16), ylim=(-1, 11))
    create_moving_polygon(fig, ax, renderer, ((3, 10), (2, 10), (1, 8), (2, 6), (5, 6), (7, 8)), (8, 0))
    create_still_polygon(fig, ax, renderer, ((10, 5), (8, 6), (6, 5), (6, 4), (7, 2), (10, 4)))

    return fig, ax, '{}01_{}'.format(func_code, func_name)

def setup_fig02():
    fig, ax, renderer = create_newfig('{}02'.format(func_code), xlim=(-8, 7), ylim=(-2, 12))
    create_moving_polygon(fig, ax, renderer, ((5, 5), (4, 5), (2, 0), (4, -1), (6, 0)), (-5, 0))
    create_still_polygon(fig, ax, renderer, ((2, 11), (-2, 8), (2, 5), (3, 6), (3, 11)))

    return fig, ax, '{}02_{}'.format(func_code, func_name)

def setup_fig03():
    fig, ax, renderer = create_newfig('{}03'.format(func_code), xlim=(-3, 12), ylim=(-5, 10))
    create_moving_polygon(fig, ax, renderer, ((9.5, 8.5), (8.5, 7.5), (9.5, 5), (10.5, 7)), (-9, -9))
    create_still_polygon(fig, ax, renderer, ((2, 5), (-1, 5), (-2, 3), (2, 1), (3, 2)))

    return fig, ax, '{}03_{}'.format(func_code, func_name)
    
def setup_fig04():
    fig, ax, renderer = create_newfig('{}04'.format(func_code), xlim=(-1, 14), ylim=(-3, 11))
    create_moving_polygon(fig, ax, renderer, ((4.5, 4), (0.5, 2), (0.5, 1), (0.5, 0), (2.5, -2), (3.5, -2), (5.5, -1)), (6.7492919018596025, 4.29500393754702))
    create_still_polygon(fig, ax, renderer, ((8, 8.5), (5, 9.5), (4, 8.5), (6, 5.5)))

    return fig, ax, '{}04_{}'.format(func_code, func_name)

run_or_export(setup_fig01, setup_fig02, setup_fig03, setup_fig04)