from utils import create_newfig, create_moving_polygon, create_still_polygon, run_or_export

func_code = 'an'
func_name = 'test_one_moving_one_stationary_distlimit_touching'

def setup_fig01():
    fig, ax, renderer = create_newfig('{}01'.format(func_code))

    create_moving_polygon(fig, ax, renderer, ((0, 2), (0, 3), (1, 3), (1, 2)), (5, -1.25), 'topright')
    create_still_polygon(fig, ax, renderer, ((3, 0), (3, 1), (4, 1), (4, 0)), 'botleft')
    return fig, ax, '{}01_{}'.format(func_code, func_name)

def setup_fig02():
    fig, ax, renderer = create_newfig('{}02'.format(func_code))
    
    create_moving_polygon(fig, ax, renderer, ((1, 2), (1, 3), (2, 3), (2, 2)), (4, 0), 'topright')
    create_still_polygon(fig, ax, renderer, ((2, 1), (4, 2), (5, 0), (1, 0)), 'botleft')
    return fig, ax, '{}02_{}'.format(func_code, func_name)

def setup_fig03():
    fig, ax, renderer = create_newfig('{}03'.format(func_code))
    
    create_moving_polygon(fig, ax, renderer, ((2, 4), (3, 4), (3, 2), (1, 3)), (3, -2), 'topright')
    create_still_polygon(fig, ax, renderer, ((0, 1), (2.5, 2), (3, 0), (2, 0)), 'botleft')
    return fig, ax, '{}03_{}'.format(func_code, func_name)
    
def setup_fig04():
    fig, ax, renderer = create_newfig('{}04'.format(func_code))
    
    create_moving_polygon(fig, ax, renderer, ((0, 0), (1, 2), (2, 1)), (3, 3), 'topright')
    create_still_polygon(fig, ax, renderer, ((3, 2), (5, 3), (5, 1)), 'botleft')
    return fig, ax, '{}04_{}'.format(func_code, func_name)

run_or_export(setup_fig01, setup_fig02, setup_fig03, setup_fig04)