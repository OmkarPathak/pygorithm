from utils import create_newfig, create_moving_line, create_still_segment, run_or_export

func_code = 'af'
func_name = 'test_line_line_touching'

def setup_fig01():
    fig, ax, renderer = create_newfig('{}01'.format(func_code))

    create_moving_line(fig, ax, renderer, (1, 3), (2, 3), (3, -3), 'top')
    create_still_segment(fig, ax, renderer, (3, 3), (5, 0), 'topright')
    return fig, ax, '{}01_{}'.format(func_code, func_name)

def setup_fig02():
    fig, ax, renderer = create_newfig('{}02'.format(func_code))
    
    create_moving_line(fig, ax, renderer, (1, 1), (2, 1), (1, 1), 'bot')
    create_still_segment(fig, ax, renderer, (3, 2), (3, 3), 'right')
    return fig, ax, '{}02_{}'.format(func_code, func_name)

def setup_fig03():
    fig, ax, renderer = create_newfig('{}03'.format(func_code))
    
    create_moving_line(fig, ax, renderer, (1, 1), (2, 1), (2, 2), 'bot')
    create_still_segment(fig, ax, renderer, (2, 3), (3, 3), 'top')
    return fig, ax, '{}03_{}'.format(func_code, func_name)
    
def setup_fig04():
    fig, ax, renderer = create_newfig('{}04'.format(func_code))
    
    create_moving_line(fig, ax, renderer, (1, 1), (2, 1), (0, 2), 'bot')
    create_still_segment(fig, ax, renderer, (2, 3), (3, 3), 'top')
    return fig, ax, '{}04_{}'.format(func_code, func_name)

run_or_export(setup_fig01, setup_fig02, setup_fig03, setup_fig04)