from utils import create_newfig, create_moving_polygon, create_still_polygon, run_or_export

func_code = 'ai'
func_name = 'test_one_moving_one_stationary_no_intr'

def setup_fig01():
    fig, ax, renderer = create_newfig('{}01'.format(func_code))

    create_moving_polygon(fig, ax, renderer, ((0, 1, 'right'), (1, 2, 'bot'), (2, 1, 'left'), (1, 0, 'top')), (0, 2))
    create_still_polygon(fig, ax, renderer, ((3, 1), (3, 2), (4, 1)), 'botleft')
    return fig, ax, '{}01_{}'.format(func_code, func_name)

def setup_fig02():
    fig, ax, renderer = create_newfig('{}02'.format(func_code))
    
    create_moving_polygon(fig, ax, renderer, ((0, 1, 'right'), (1, 2, 'bot'), (2, 1, 'left'), (1, 0, 'top')), (1, 2))
    create_still_polygon(fig, ax, renderer, ((3, 1), (3, 2), (4, 1)), 'botleft')
    return fig, ax, '{}02_{}'.format(func_code, func_name)

def setup_fig03():
    fig, ax, renderer = create_newfig('{}03'.format(func_code))
    
    create_moving_polygon(fig, ax, renderer, ((4, 4), (5, 3.5), (5.5, 2.5), (4, 3)), (-2, 0), 'topright')
    create_still_polygon(fig, ax, renderer, ((3, 1), (3, 2), (4, 1)), 'botleft')
    return fig, ax, '{}03_{}'.format(func_code, func_name)
    
def setup_fig04():
    fig, ax, renderer = create_newfig('{}04'.format(func_code))
    
    create_moving_polygon(fig, ax, renderer, ((3, 1), (3, 2), (4, 1)), (2, 0), 'botleft')
    create_still_polygon(fig, ax, renderer, ((4, 4), (5, 3.5), (5.5, 2.5), (4, 3)), 'topright')
    return fig, ax, '{}04_{}'.format(func_code, func_name)

run_or_export(setup_fig01, setup_fig02, setup_fig03, setup_fig04)