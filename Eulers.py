
import pygame
import pygame.locals as l
from math import sqrt, cos, sin, radians, acos, pi
import numpy as np
import math

def draw_3d_lines(screen, color, points_list, distance=0.01):
    for i in range(len(points_list) - 1):
        x1 = points_list[i][0]
        y1 = points_list[i][1]
        z1 = points_list[i][2]

        x2 = points_list[i + 1][0]
        y2 = points_list[i + 1][1]
        z2 = points_list[i + 1][2]

        # Apply translation and scaling
        x1t = int(x1 / distance + screen.get_width() / 2)
        y1t = int(y1 / distance + screen.get_height() / 2)
        x2t = int(x2 / distance + screen.get_width() / 2)
        y2t = int(y2 / distance + screen.get_height() / 2)

        pygame.draw.line(screen, color, (x1t, y1t), (x2t, y2t), 1)

def rotate_3d_points(points_list, angle_x, angle_y, angle_z):
    angle_x = radians(angle_x)
    angle_y = radians(angle_y)
    angle_z = radians(angle_z)

    cos_angle_x = cos(angle_x)
    sin_angle_x = sin(angle_x)
    cos_angle_y = cos(angle_y)
    sin_angle_y = sin(angle_y)
    cos_angle_z = cos(angle_z)
    sin_angle_z = sin(angle_z)

    rotated_points = []
    for point in points_list:
        x = point[0]
        y = point[1]
        z = point[2]

        # Apply rotation on x-axis
        x_rotated = x
        y_rotated = y * cos_angle_x - z * sin_angle_x
        z_rotated = y * sin_angle_x + z * cos_angle_x

        # Apply rotation on y-axis
        x_final = x_rotated * cos_angle_y + z_rotated * sin_angle_y
        y_final = y_rotated
        z_final = -x_rotated * sin_angle_y + z_rotated * cos_angle_y

        # Apply rotation on z-axis
        x_rotated = x_final * cos_angle_z - y_final * sin_angle_z
        y_rotated = x_final * sin_angle_z + y_final * cos_angle_z
        z_rotated = z_final

        rotated_points.append((x_rotated, y_rotated, z_rotated))

    return np.array(rotated_points)
def rotate_around_point(points_list, point, angle_x,angle_y,angle_z):
    angle_x = radians(angle_x)
    angle_y = radians(angle_y)
    angle_z = radians(angle_z)

    cos_angle_x = cos(angle_x)
    sin_angle_x = sin(angle_x)
    cos_angle_y = cos(angle_y)
    sin_angle_y = sin(angle_y)
    cos_angle_z = cos(angle_z)
    sin_angle_z = sin(angle_z)

    x = point[0]
    y = point[1]
    z = point[2]

    # Apply rotation on x-axis
    x_rotated = x
    y_rotated = y * cos_angle_x - z * sin_angle_x
    z_rotated = y * sin_angle_x + z * cos_angle_x

    # Apply rotation on y-axis
    x_final = x_rotated * cos_angle_y + z_rotated * sin_angle_y
    y_final = y_rotated
    z_final = -x_rotated * sin_angle_y + z_rotated * cos_angle_y

    # Apply rotation on z-axis
    x_rotated = x_final * cos_angle_z - y_final * sin_angle_z
    y_rotated = x_final * sin_angle_z + y_final * cos_angle_z
    z_rotated = z_final
    vx=point[0]-x_rotated
    vy=point[1]-y_rotated
    vz=point[2]-z_rotated

    rotated_points = []
    for point in points_list:
        x = point[0]
        y = point[1]
        z = point[2]

        # Apply rotation on x-axis
        x_rotated = x
        y_rotated = y * cos_angle_x - z * sin_angle_x
        z_rotated = y * sin_angle_x + z * cos_angle_x

        # Apply rotation on y-axis
        x_final = x_rotated * cos_angle_y + z_rotated * sin_angle_y
        y_final = y_rotated
        z_final = -x_rotated * sin_angle_y + z_rotated * cos_angle_y

        # Apply rotation on z-axis
        x_rotated = x_final * cos_angle_z - y_final * sin_angle_z +vx
        y_rotated = x_final * sin_angle_z + y_final * cos_angle_z +vy
        z_rotated = z_final+vz

        rotated_points.append((x_rotated, y_rotated, z_rotated))
    rotated_points = np.array(rotated_points)
    return rotated_points
def make_3d_circle_part(first_point, last_point, center, num_points, dir):
    angle0 = math.atan2(last_point[2] - first_point[2], last_point[0] - first_point[0])
    angle1 = math.atan2(last_point[2] - first_point[2], last_point[1] - first_point[1])
    point_list = [first_point, center, last_point]
    point_list = rotate_around_point(point_list,center,0,angle0,angle1)
    # Calculate the angle between the first and last points.
    first_point=point_list[0]
    last_point=point_list[1]
    center=point_list[2]
    
    cosTh = np.dot([last_point[1] - center[1], last_point[0] - center[0]],[first_point[1] - center[1], first_point[0] - center[0]])
    sinTh = np.cross([last_point[1] - center[1], last_point[0] - center[0]],[first_point[1] - center[1], first_point[0] - center[0]])
    angle = np.rad2deg(np.arctan2(sinTh,cosTh))
    angle3 = 0
    if dir == "down":
        if angle > 0:
            pass
        elif angle<0:
            angle = 360-angle
            
    elif dir == "up":
        if angle < 0:
            pass
        elif angle>0:
            angle = -360+angle
    elif angle == 0:
        if type(dir) == int:
            angle3 = dir
            angle = -180
        else:
            print("wrong input")
    else:
        print("error")
    # Calculate the radius of the circle.
    radius = math.sqrt((last_point[0] - first_point[0])**2 + (last_point[1] - first_point[1])**2)
    # Generate the points on the circle.
    points = []
    anglex = angle
    for i in range(num_points):
        # Calculate the angle of the current point.

        # Calculate the x, y, and z coordinates of the current point.
        x = center[0] + radius * math.cos(math.radians(angle)) +1
        y = center[1] + radius * math.sin(math.radians(angle))
        z = center[2]

        # Add the current point to the list of points.
        points.append((x, y, z))
        angle = angle - anglex / num_points
    points = rotate_around_point(points,center,-angle3,-angle0,-angle1)
    points = np.array(points)
    return points
def find_circle_center(point_a,point_b,point_c):
    a = plane_of_equ
    find_crossing()
def make_plane(curve1, curve2):
    if len(curve1) == len(curve2):
        precision = len(curve1)
        xlist = list()
        for p in range(precision):
            point1 = curve1[p]
            point2 = curve2[p]
            xd = (point1[0] - point2[0]) / precision
            yd = (point1[1] - point2[1]) / precision
            zd = (point1[2] - point2[2]) / precision
            line = list()
            for i in range(precision):
                xpoint = point1[0] - xd * i
                ypoint = point1[1] - yd * i
                zpoint = point1[2] - zd * i
                line.append([xpoint, ypoint, zpoint])
            xlist.append(line)
        ylist = list()
        for p in range(precision):
            nline = list()
            for i in range(precision):
                line = xlist[i]
                point = line[p]
                nline.append(point)
            ylist.append(nline)
        xarray = np.array(xlist)
        yarray = np.array(ylist)
        return np.array([xarray, yarray])
    else:
        print("need the same length curves (use the step variable in the creation of the curves)")

def draw_3d_grid(screen, color, grid):
    for i in grid:
        for j in i:
            draw_3d_lines(screen, color, j)

def rotate_3d_grid(grid, angle_x, angle_y, angle_z):
    rotated_grid = []
    for i in grid:
        rotated_lines = []
        for j in i:
            rotated_line = rotate_3d_points(j, angle_x, angle_y, angle_z)
            rotated_lines.append(rotated_line)
        rotated_grid.append(rotated_lines)
    return rotated_grid

# Example usage
pygame.init()

# Set up the screen
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("3D Curve")

# Starting point
start1 = [1,0, 1]

# Ending point
end1 = [-1, 0, -1]

# Curve control point
curve1 = [0, 0, 0]
curve1 = make_3d_circle_part(start1, end1, curve1, 30,0)
start2 = [1, 0, 1]
# Ending point
end2 = [-1, 0, -1]

# Curve control point
curve2 = [0, 0, 0]
curve2 = make_3d_circle_part(start2, end2, curve2, 30,180)
grid = make_plane(curve1, curve2)

# Main game loop
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == l.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                grid = rotate_3d_grid(grid, 0, 10, 0)
            if event.key == pygame.K_d:
                grid = rotate_3d_grid(grid, 0, -10, 0)
            if event.key == pygame.K_w:
                grid = rotate_3d_grid(grid, 10, 0, 0)
            if event.key == pygame.K_s:
                grid = rotate_3d_grid(grid, -10, 0, 0)
            if event.key == pygame.K_q:
                grid = rotate_3d_grid(grid, 0, 0, 10)
            if event.key == pygame.K_e:
                grid = rotate_3d_grid(grid, 0, 0, -10)
    screen.fill((0, 0, 0)) # Clear the screen
    draw_3d_grid(screen, (255, 0, 0), grid)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()