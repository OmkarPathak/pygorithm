from utils import create_newfig, create_moving_polygon, create_still_polygon, run_or_export

func_code = 'as'
func_name = 'test_one_moving_one_stationary_along_path_no_intr'

def setup_fig01():
    fig, ax, renderer = create_newfig('{}01'.format(func_code), ylim=(-1, 7))

    create_moving_polygon(fig, ax, renderer, ((0, 0), (0, 1), (1, 1), (1, 0)), (4, 3), 'none')
    create_still_polygon(fig, ax, renderer, ((3, 1, 'botright'), (4, 1), (4, 0), (3, 0)), 'none')
    return fig, ax, '{}01_{}'.format(func_code, func_name)

def setup_fig02():
    fig, ax, renderer = create_newfig('{}02'.format(func_code), xlim=(-2, 12), ylim=(-1, 10))
    
    create_moving_polygon(fig, ax, renderer, ((11, 5), (8, 8), (7, 7), (6, 3), (9, 3)), (-1, -3))
    create_still_polygon(fig, ax, renderer,  ((3.5, 8.5), (1.5, 8.5), (-0.5, 7.5), (0.5, 3.5), (1.5, 2.5), (4.5, 2.5), (5.5, 6.5)))
    return fig, ax, '{}02_{}'.format(func_code, func_name)

def setup_fig03():
    fig, ax, renderer = create_newfig('{}03'.format(func_code), xlim=(-3, 9), ylim=(-1, 15))
    
    create_moving_polygon(fig, ax, renderer, ((0.5, 9.0), (-1.5, 8.0), (-1.5, 6.0), (1.5, 5.0), (2.5, 5.0), (2.5, 9.0)), (0, 5))
    create_still_polygon(fig, ax, renderer, ((7.0, 6.0), (4.0, 5.0), (4.0, 3.0), (6.0, 2.0), (8.0, 3.0)))
    return fig, ax, '{}03_{}'.format(func_code, func_name)
    
def setup_fig04():
    fig, ax, renderer = create_newfig('{}04'.format(func_code), xlim=(-2, 12), ylim=(-3, 10))
    
    create_moving_polygon(fig, ax, renderer, ((5.5, 4.5), (3.5, -1.5), (9.5, -1.5), (10.5, 0.5)), (-4, 0))
    create_still_polygon(fig, ax, renderer, ((7.5, 8.5), (6.5, 5.5), (7.5, 4.5), (9.5, 4.5), (10.5, 7.5)))
    return fig, ax, '{}04_{}'.format(func_code, func_name)

run_or_export(setup_fig01, setup_fig02, setup_fig03, setup_fig04)