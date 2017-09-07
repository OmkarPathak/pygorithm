from utils import create_newfig, create_moving_line, create_still_segment, run_or_export

func_code = 'ag'
func_name = 'test_line_line_touching_at_start'

def setup_fig01():
    fig, ax, renderer = create_newfig('{}01'.format(func_code))

    create_moving_line(fig, ax, renderer, (1, 1), (2, 1), (0, 2), 'botleft')
    create_still_segment(fig, ax, renderer, (2, 1), (3, 0), 'topright')
    return fig, ax, '{}01_{}'.format(func_code, func_name)

def setup_fig02():
    fig, ax, renderer = create_newfig('{}02'.format(func_code))
    
    create_moving_line(fig, ax, renderer, (1, 1), (1, 3), (2, 0), 'left')
    create_still_segment(fig, ax, renderer, (1, 2), (2, 2), 'topright')
    return fig, ax, '{}02_{}'.format(func_code, func_name)

def setup_fig03():
    fig, ax, renderer = create_newfig('{}03'.format(func_code))
    
    create_moving_line(fig, ax, renderer, (1, 1), (2, 0), (2, 0), 'topright')
    create_still_segment(fig, ax, renderer, (0, 1), (1.5, 0.5), 'botleft')
    return fig, ax, '{}03_{}'.format(func_code, func_name)
    
def setup_fig04():
    fig, ax, renderer = create_newfig('{}04'.format(func_code))
    
    create_moving_line(fig, ax, renderer, (5, 4), (6, 3), (-2, -2), 'topright')
    create_still_segment(fig, ax, renderer, (5.5, 3.5), (6, 4), 'botleft', 'botright')
    return fig, ax, '{}04_{}'.format(func_code, func_name)

run_or_export(setup_fig01, setup_fig02, setup_fig03, setup_fig04)