def poes(area, h, poro, swi, boi):
    """

    Parameters
    ----------
    area
        area, acres
    h
        Thickness, ft
    poro
        Porosity, fraction
    swi
        Water saturation, fraction
    boi
        Bubble point factor, rb/stb

    Returns
        float number -> poes
    -------

    """
    return 7758 * area * poro * h(1 - swi) / boi