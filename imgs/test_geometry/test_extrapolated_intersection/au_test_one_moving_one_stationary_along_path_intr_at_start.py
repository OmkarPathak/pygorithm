from utils import create_newfig, create_moving_polygon, create_still_polygon, run_or_export

func_code = 'au'
func_name = 'test_one_moving_one_stationary_along_path_intr_at_start'

def setup_fig01():
    fig, ax, renderer = create_newfig('{}01'.format(func_code), xlim=(-4, 15), ylim=(-2, 10))
    create_moving_polygon(fig, ax, renderer, ((5, 3.5), (5, 2.5), (3, -0.5), (-2, 0.5), (-3, 2.5), (-2, 4.5), (0, 6.5)), (9, 2))
    create_still_polygon(fig, ax, renderer, ((6.5, 6.5), (9.5, 0.5), (3.5, -0.5), (1.5, 2.5), (3.5, 6.5)))

    return fig, ax, '{}01_{}'.format(func_code, func_name)

def setup_fig02():
    fig, ax, renderer = create_newfig('{}02'.format(func_code), xlim=(-3, 18), ylim=(-3, 9))
    create_moving_polygon(fig, ax, renderer, ((6.5, 5.5), (4.5, 3.5), (2.5, 6.5), (2.5, 7.5), (6.5, 6.5)), (10, -5))
    create_still_polygon(fig, ax, renderer, ((6, 2.5), (1, -1.5), (-2, 2.5), (-2, 2.5), (3, 6.5)))

    return fig, ax, '{}02_{}'.format(func_code, func_name)

def setup_fig03():
    fig, ax, renderer = create_newfig('{}03'.format(func_code), xlim=(-1, 16), ylim=(-6, 10))
    create_moving_polygon(fig, ax, renderer, ((10.5, 3.5), (8.5, 2.5), (5.5, 6.5), (9.5, 8.5), (11.5, 6.5), (11.5, 5.5)), (3, -7))
    create_still_polygon(fig, ax, renderer, ((12, 1), (11, 0), (9, -3), (8, -3), (5, -1), (5, 4), (9, 5)))

    return fig, ax, '{}03_{}'.format(func_code, func_name)
    
def setup_fig04():
    fig, ax, renderer = create_newfig('{}04'.format(func_code), xlim=(-8, 8), ylim=(-1, 19))
    create_moving_polygon(fig, ax, renderer, ((3.5, 6), (-0.5, 5), (-0.5, 7), (-0.5, 8), (1.5, 9), (1.5, 9), (3.5, 7)), (-6, 9))
    create_still_polygon(fig, ax, renderer, ((7, 6), (5, 6), (4, 6), (3, 7), (5, 10), (7, 9)))

    return fig, ax, '{}04_{}'.format(func_code, func_name)

run_or_export(setup_fig01, setup_fig02, setup_fig03, setup_fig04)