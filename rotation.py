import math

def rotation_z(point_1, point_2):
    x1, y1 = point_1.x, point_1.y
    x2, y2 = point_2.x, point_2.y

    delta_x = x2 - x1
    delta_y = y2 - y1

    angle = math.atan2(delta_y, delta_x)
    return angle

def rotation_x(point_1, point_2):
    y1, z1 = point_1.y, point_1.z
    y2, z2 = point_2.y, point_2.z

    delta_y = y2 - y1
    delta_z = z2 - z1

    angle = math.atan2(delta_z, delta_y)
    return angle

def rotation_y(point_1, point_2):
    x1, z1 = point_1.x, point_1.z
    x2, z2 = point_2.x, point_2.z

    delta_x = x1 - x2
    delta_z = z2 - z1

    angle = math.atan2(delta_z, delta_x)
    return angle

def wrap_angle(angle):
    return (angle + math.pi) % (2 * math.pi) - math.pi
    
class SmoothRotation:
    def __init__(self, smoothness: float = 0.2):
        self.smoothness = smoothness
        self.old_angle = (0, 0, 0)
        self.history = [self.old_angle]
        self.angle = self.old_angle

    def angle_from_points(self, top, bottom, left, right):
        return (rotation_x(top, bottom), rotation_y(left, right), -rotation_z(left, right))

    def new_rotation(self, angle: tuple[float, float, float]):
        delta_angle = (angle[0] - self.old_angle[0], angle[1] - self.old_angle[1], angle[2] - self.old_angle[2])
        self.history.append(delta_angle)
        self.history = self.history[-5:]
        media_x = sum([rot[0] for rot in self.history]) / len(self.history) * self.smoothness
        media_z = sum([rot[2] for rot in self.history]) / len(self.history) * self.smoothness

        diff = wrap_angle(angle[1] - self.old_angle[1])
        interpolated_angle = self.old_angle[1] + diff * self.smoothness

        new_angle = (self.old_angle[0] + media_x, wrap_angle(interpolated_angle), self.old_angle[2] + media_z)
        self.old_angle = new_angle
        return new_angle
