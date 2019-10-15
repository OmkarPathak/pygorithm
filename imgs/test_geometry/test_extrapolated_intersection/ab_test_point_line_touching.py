from utils import create_newfig, create_moving_point, create_still_segment, run_or_export

func_code = 'ab'
func_name = 'test_point_line_touching'

def setup_fig01():
    fig, ax, renderer = create_newfig('{}01'.format(func_code))

    create_moving_point(fig, ax, renderer, 1, 1, 2, 4)
    create_still_segment(fig, ax, renderer, (2, 4), (6, 2), 'topright')
    return fig, ax, '{}01_{}'.format(func_code, func_name)

def setup_fig02():
    fig, ax, renderer = create_newfig('{}02'.format(func_code))
    
    create_moving_point(fig, ax, renderer, 2, 1, 6, 2)
    create_still_segment(fig, ax, renderer, (2, 0), (6, 2), 'botright')
    return fig, ax, '{}02_{}'.format(func_code, func_name)

def setup_fig03():
    fig, ax, renderer = create_newfig('{}03'.format(func_code))
    
    create_moving_point(fig, ax, renderer, 2, 1, 2, 0)
    create_still_segment(fig, ax, renderer, (2, 0), (6, 2), 'botright')
    return fig, ax, '{}03_{}'.format(func_code, func_name)
    
def setup_fig04():
    fig, ax, renderer = create_newfig('{}04'.format(func_code))
    
    create_moving_point(fig, ax, renderer, 6.25, 3, 2, 0, 'topright')
    create_still_segment(fig, ax, renderer, (2, 0), (6, 2), 'botright')
    return fig, ax, '{}04_{}'.format(func_code, func_name)

run_or_export(setup_fig01, setup_fig02, setup_fig03, setup_fig04)