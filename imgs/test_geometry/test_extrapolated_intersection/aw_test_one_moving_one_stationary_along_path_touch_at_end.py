from utils import create_newfig, create_moving_polygon, create_still_polygon, run_or_export

func_code = 'aw'
func_name = 'test_one_moving_one_stationary_along_path_touch_at_end'

def setup_fig01():
    fig, ax, renderer = create_newfig('{}01'.format(func_code), xlim=(-5, 10), ylim=(-2, 5))
    create_moving_polygon(fig, ax, renderer, ((-2, 0.5), (-3, -0.5), (-4, 0.5), (-3, 1.5)), (7, 1))
    create_still_polygon(fig, ax, renderer, ((9, 0), (8, 0), (5, 1), (5, 3), (7, 4), (9, 4)))

    return fig, ax, '{}01_{}'.format(func_code, func_name)

def setup_fig02():
    fig, ax, renderer = create_newfig('{}02'.format(func_code), xlim=(-1, 20), ylim=(-7, 10))
    create_moving_polygon(fig, ax, renderer, ((11, -3.5), (9, -5.5), (6, -4.5), (6, -1.5), (9, -1.5)), (7, 8.5))
    create_still_polygon(fig, ax, renderer, ((14, 8), (14, 7), (12, 7), (13, 9)))

    return fig, ax, '{}02_{}'.format(func_code, func_name)

def setup_fig03():
    fig, ax, renderer = create_newfig('{}03'.format(func_code), xlim=(-4, 7), ylim=(-1, 10))
    create_moving_polygon(fig, ax, renderer, ((3, 0.5), (2, 1.5), (2, 2.5), (4, 2.5)), (-0.5, 5))
    create_still_polygon(fig, ax, renderer, ((-0.5, 5), (-1.5, 5), (-2.5, 7), (-0.5, 9), (1.5, 8), (1.5, 7)))

    return fig, ax, '{}03_{}'.format(func_code, func_name)
    
def setup_fig04():
    fig, ax, renderer = create_newfig('{}04'.format(func_code), xlim=(-1, 19), ylim=(-10, 6))
    create_moving_polygon(fig, ax, renderer, ((15, 4.5), (15, 2.5), (13, 3.5), (13, 4.5), (14, 4.5)), (-1, -9))
    create_still_polygon(fig, ax, renderer, ((12, -5), (11, -9), (8, -9), (10, -4)))

    return fig, ax, '{}04_{}'.format(func_code, func_name)

run_or_export(setup_fig01, setup_fig02, setup_fig03, setup_fig04)