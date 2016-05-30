#normalize_angle_f.m

def normalize_angle_f(r, low):
    angle = r - 2*pi*floor((r-low)/(2*pi))
    return angle
