import photoslideshow.common.photo as p


def test_calc_resize_smaller_height_new_width():
    width = 800
    height = 600
    new_width = 700
    new_height = 300
    calc_width, calc_height = p.calc_resize(width, height, new_width, new_height)
    assert calc_width == 400
    assert calc_height == 300


def test_calc_resize_smaller_height_new_height():
    width = 800
    height = 600
    new_width = 300
    new_height = 700
    calc_width, calc_height = p.calc_resize(width, height, new_width, new_height)
    assert calc_width == 300
    assert calc_height == 225


def test_calc_resize_smaller_width_new_width():
    width = 500
    height = 600
    new_width = 700
    new_height = 300
    calc_width, calc_height = p.calc_resize(width, height, new_width, new_height)
    assert calc_width == 250
    assert calc_height == 300


def test_calc_resize_smaller_width_new_height():
    width = 500
    height = 600
    new_width = 300
    new_height = 700
    calc_width, calc_height = p.calc_resize(width, height, new_width, new_height)
    assert calc_width == 300
    assert calc_height == 360


def test_calc_resize_square():
    width = 500
    height = 500
    new_width = 300
    new_height = 700
    calc_width, calc_height = p.calc_resize(width, height, new_width, new_height)
    assert calc_width == 300
    assert calc_height == 300


def test_calc_resize_smaller():
    width = 500
    height = 800
    new_width = 600
    new_height = 1700
    calc_width, calc_height = p.calc_resize(width, height, new_width, new_height)
    assert calc_width == width
    assert calc_height == height

