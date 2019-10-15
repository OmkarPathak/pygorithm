from utils import create_newfig, create_moving_polygon, create_still_polygon, run_or_export

func_code = 'ax'
func_name = 'test_one_moving_one_stationary_along_path_intr_after_end'

def setup_fig01():
    fig, ax, renderer = create_newfig('{}01'.format(func_code), xlim=(-12, 7), ylim=(-1, 6))
    create_moving_polygon(fig, ax, renderer, ((-6.5, 3.5), (-7.5, 0.5), (-10.5, 1.5), (-8.5, 4.5)), (5, 0))
    create_still_polygon(fig, ax, renderer, ((1, 2.5), (1, 0.5), (-1, 0.5), (-1, 1.5), (0, 2.5)))

    return fig, ax, '{}01_{}'.format(func_code, func_name)

def setup_fig02():
    fig, ax, renderer = create_newfig('{}02'.format(func_code), xlim=(-2, 19), ylim=(-1, 11))
    create_moving_polygon(fig, ax, renderer, ((1.5, 3.5), (0.5, 2.5), (-0.5, 2.5), (-0.5, 3.5), (0.5, 4.5)), (10, 4))
    create_still_polygon(fig, ax, renderer, ((17.5, 6), (14.5, 6), (12.5, 8), (14.5, 10), (17.5, 9)))

    return fig, ax, '{}02_{}'.format(func_code, func_name)

def setup_fig03():
    fig, ax, renderer = create_newfig('{}03'.format(func_code), xlim=(-1, 16), ylim=(-1, 12))
    create_moving_polygon(fig, ax, renderer, ((1, 2), (0, 3), (0, 5), (1, 6), (4, 4)), (7, 3))
    create_still_polygon(fig, ax, renderer, ((14, 7.5), (13, 8.5), (15, 9.5), (15, 8.5)))

    return fig, ax, '{}03_{}'.format(func_code, func_name)
    
def setup_fig04():
    fig, ax, renderer = create_newfig('{}04'.format(func_code), xlim=(-3, 15), ylim=(-8, 5))
    create_moving_polygon(fig, ax, renderer, ((2.5, -4), (1.5, -6), (0.5, -6), (-1.5, -4), (-0.5, -2), (2.5, -3)), (6, -1))
    create_still_polygon(fig, ax, renderer, ((12, -7), (10, -5), (10, -4), (14, -4)))

    return fig, ax, '{}04_{}'.format(func_code, func_name)

run_or_export(setup_fig01, setup_fig02, setup_fig03, setup_fig04)