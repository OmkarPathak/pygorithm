from utils import create_newfig, create_moving_line, create_still_segment, run_or_export

func_code = 'ae'
func_name = 'test_line_line_no_intr'

def setup_fig01():
    fig, ax, renderer = create_newfig('{}01'.format(func_code))

    create_moving_line(fig, ax, renderer, (1, 4), (1, 3), (2, 0), 'botright')
    create_still_segment(fig, ax, renderer, (1, 1), (3, 2), 'bot')
    return fig, ax, '{}01_{}'.format(func_code, func_name)

def setup_fig02():
    fig, ax, renderer = create_newfig('{}02'.format(func_code))
    
    create_moving_line(fig, ax, renderer, (1, 3), (2, 4), (3, -3), 'topleft')
    create_still_segment(fig, ax, renderer, (1, 0.5), (3, 0.5), 'bot')
    return fig, ax, '{}02_{}'.format(func_code, func_name)

def setup_fig03():
    fig, ax, renderer = create_newfig('{}03'.format(func_code))
    
    create_moving_line(fig, ax, renderer, (1, 3), (2, 4), (3, -3), 'topleft')
    create_still_segment(fig, ax, renderer, (4, 3), (6, 4), 'botright')
    return fig, ax, '{}03_{}'.format(func_code, func_name)
    
def setup_fig04():
    fig, ax, renderer = create_newfig('{}04'.format(func_code))
    
    create_moving_line(fig, ax, renderer, (1, 3), (2, 3), (3, -3), 'bot')
    create_still_segment(fig, ax, renderer, (0, 4), (3, 3), 'topright')
    return fig, ax, '{}04_{}'.format(func_code, func_name)

run_or_export(setup_fig01, setup_fig02, setup_fig03, setup_fig04)