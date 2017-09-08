from utils import create_newfig, create_moving_point, create_still_segment, run_or_export
    
def setup_fig01():
    fig, ax, renderer = create_newfig('aa01')

    create_moving_point(fig, ax, renderer, 1, 1, 6, 1)
    create_still_segment(fig, ax, renderer, (2, 4), (6, 2))
    return fig, ax, 'aa01_test_point_line_no_intr'

def setup_fig02():
    fig, ax, renderer = create_newfig('aa02')
    
    create_moving_point(fig, ax, renderer, 1, 1, 1, 4)
    create_still_segment(fig, ax, renderer, (2, 4), (6, 2), 'topright')
    return fig, ax, 'aa02_test_point_line_no_intr'

def setup_fig03():
    fig, ax, renderer = create_newfig('aa03')
    
    create_moving_point(fig, ax, renderer, 4, 1, 1, 4)
    create_still_segment(fig, ax, renderer, (2, 4), (6, 4), 'topright')
    return fig, ax, 'aa03_test_point_line_no_intr'
    
def setup_fig04():
    fig, ax, renderer = create_newfig('aa04')
    
    create_moving_point(fig, ax, renderer, 2, 1, 6, 4)
    create_still_segment(fig, ax, renderer, (1, 2), (5, 4), 'topleft')
    return fig, ax, 'aa04_test_point_line_no_intr'

run_or_export(setup_fig01, setup_fig02, setup_fig03, setup_fig04)