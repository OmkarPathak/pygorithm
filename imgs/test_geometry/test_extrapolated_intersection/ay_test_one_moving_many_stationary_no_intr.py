from utils import create_newfig, create_moving_polygon, create_still_polygon, run_or_export

func_code = 'ay'
func_name = 'test_one_moving_many_stationary_no_intr'

def setup_fig01():
    fig, ax, renderer = create_newfig('{}01'.format(func_code), xlim=(-1, 12), ylim=(-1, 12))
    create_moving_polygon(fig, ax, renderer, ((3, 3, 'botleft'), (4, 3), (4, 4), (3, 4)), (4, 4), 'none')
    create_still_polygon(fig, ax, renderer, ((6, 3, 'botleft'), (7, 3), (7, 4), (6, 4)), 'none')
    create_still_polygon(fig, ax, renderer, ((3, 6, 'botleft'), (3, 7), (4, 7), (4, 6)), 'none')
    create_still_polygon(fig, ax, renderer, ((4, 10), (6, 11), (6, 8), (2, 7)))

    return fig, ax, '{}01_{}'.format(func_code, func_name)

def setup_fig02():
    fig, ax, renderer = create_newfig('{}02'.format(func_code), xlim=(-3, 9), ylim=(-10, 5))
    create_moving_polygon(fig, ax, renderer, ((-1, -9.5), (-1, -5.5), (3, -5.5), (4, -7.5)), (3, 6))
    create_still_polygon(fig, ax, renderer, ((6, -6), (8, -7), (7, -9)))
    create_still_polygon(fig, ax, renderer, ((0, 2), (2, 3), (1, 1)))
    create_still_polygon(fig, ax, renderer, ((-2, -2, 'botleft'), (-2, -1), (-1, -1), (-1, -2)), 'none')
    create_still_polygon(fig, ax, renderer, ((8, -4, 'botleft'), (8, -3), (7, -3), (7, -4)), 'none')

    return fig, ax, '{}02_{}'.format(func_code, func_name)

def setup_fig03():
    fig, ax, renderer = create_newfig('{}03'.format(func_code), xlim=(-1, 21), ylim=(-1, 15))
    create_moving_polygon(fig, ax, renderer, ((18.5, 3), (17.5, 3), (17.5, 5), (19.5, 5)), (-3, 9))
    create_still_polygon(fig, ax, renderer, ((18, 13), (20, 14), (18.5, 11)))
    create_still_polygon(fig, ax, renderer, ((5, 5), (6, 2), (3, 3), (2, 4)))

    return fig, ax, '{}03_{}'.format(func_code, func_name)
    
def setup_fig04():
    fig, ax, renderer = create_newfig('{}04'.format(func_code), xlim=(-9, 7), ylim=(-4, 6))
    create_moving_polygon(fig, ax, renderer, ((-6, 2), (-6, 1), (-8, 0), (-8, 2)), (5, 0))
    create_still_polygon(fig, ax, renderer, ((-7, 3, 'botleft'), (-7, 4), (-6, 4), (-6, 3)), 'none')
    create_still_polygon(fig, ax, renderer, ((-6, 3, 'botleft'), (-6, 4), (-5, 4), (-5, 3)), 'none')
    create_still_polygon(fig, ax, renderer, ((-5, 3, 'botleft'), (-5, 4), (-4, 4), (-4, 3)), 'none')
    create_still_polygon(fig, ax, renderer, ((-4, 3, 'botleft'), (-4, 4), (-3, 4), (-3, 3)), 'none')


    return fig, ax, '{}04_{}'.format(func_code, func_name)

run_or_export(setup_fig01, setup_fig02, setup_fig03, setup_fig04)