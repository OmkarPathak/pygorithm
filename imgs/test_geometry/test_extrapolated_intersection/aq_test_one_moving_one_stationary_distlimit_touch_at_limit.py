from utils import create_newfig, create_moving_polygon, create_still_polygon, run_or_export

func_code = 'aq'
func_name = 'test_one_moving_one_stationary_distlimit_touch_at_limit'

def setup_fig01():
    fig, ax, renderer = create_newfig('{}01'.format(func_code), ylim=(-1, 7))

    create_moving_polygon(fig, ax, renderer, ((0, 0), (0, 1), (1, 1), (1, 0)), (4, 3), 'none')
    create_still_polygon(fig, ax, renderer, ((3, 5, 'topleft'), (4, 5), (4, 4), (3, 4)), 'none')
    return fig, ax, '{}01_{}'.format(func_code, func_name)

def setup_fig02():
    fig, ax, renderer = create_newfig('{}02'.format(func_code), xlim=(-1, 8), ylim=(-1, 7))
    
    create_moving_polygon(fig, ax, renderer, ((4, 4), (5, 6), (4, 3)), (2, -1.5), 'topright')
    create_still_polygon(fig, ax, renderer, ((1, 3), (2, 3.5), (7, 1), (6, 0)), 'top')
    return fig, ax, '{}02_{}'.format(func_code, func_name)

def setup_fig03():
    fig, ax, renderer = create_newfig('{}03'.format(func_code))
    
    create_moving_polygon(fig, ax, renderer, ((6, 3), (6, 2), (5, 1), (4, 3)), (-3, 0), 'topright')
    create_still_polygon(fig, ax, renderer, ((0, 3, 'none'), (1, 3), (2, 1), (0, 1, 'none')))
    return fig, ax, '{}03_{}'.format(func_code, func_name)
    
def setup_fig04():
    fig, ax, renderer = create_newfig('{}04'.format(func_code))
    
    create_moving_polygon(fig, ax, renderer, ((5, 0, 'none'), (6, 1), (2, 1)), (0, 2), 'topright')
    create_still_polygon(fig, ax, renderer, ((3, 4, 'top'), (4, 4), (4, 3), (3, 3)), 'none')
    return fig, ax, '{}04_{}'.format(func_code, func_name)

run_or_export(setup_fig01, setup_fig02, setup_fig03, setup_fig04)