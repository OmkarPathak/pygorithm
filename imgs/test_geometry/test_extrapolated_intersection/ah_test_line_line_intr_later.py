from utils import create_newfig, create_moving_line, create_still_segment, run_or_export

func_code = 'ah'
func_name = 'test_line_line_intr_later'

def setup_fig01():
    fig, ax, renderer = create_newfig('{}01'.format(func_code))

    create_moving_line(fig, ax, renderer, (5, 4), (6, 3), (-2, -2), 'topright')
    create_still_segment(fig, ax, renderer, (3.5, 1.5), (3.5, 0), 'botleft', 'bot')
    return fig, ax, '{}01_{}'.format(func_code, func_name)

def setup_fig02():
    fig, ax, renderer = create_newfig('{}02'.format(func_code))
    
    create_moving_line(fig, ax, renderer, (5, 4), (5, 3), (-2, -2), 'topright')
    create_still_segment(fig, ax, renderer, (3, 3), (3, 0), 'left')
    return fig, ax, '{}02_{}'.format(func_code, func_name)

def setup_fig03():
    fig, ax, renderer = create_newfig('{}03'.format(func_code))
    
    create_moving_line(fig, ax, renderer, (5, 4), (5, 3), (-2, 0), 'right')
    create_still_segment(fig, ax, renderer, (1, 1), (3, 3.5), 'left')
    return fig, ax, '{}03_{}'.format(func_code, func_name)
    
def setup_fig04():
    fig, ax, renderer = create_newfig('{}04'.format(func_code))
    
    create_moving_line(fig, ax, renderer, (0, 1), (1, 0), (1, 2), 'topright')
    create_still_segment(fig, ax, renderer, (2, 1), (2, 4), 'right')
    return fig, ax, '{}04_{}'.format(func_code, func_name)

run_or_export(setup_fig01, setup_fig02, setup_fig03, setup_fig04)