from math import pi, sqrt


def area_cube(side_length: float) -> float:  # Kub
    if side_length < 0:
        raise ValueError("area_cube funksiyasi yalnis menfi olmayan deyerleri qebul edir")
    return 6 * side_length**2



def area_sphere(radius: float) -> float:  # Kure
    
    if radius < 0:
        raise ValueError("area_sphere() funksiyasi yalnis menfi olmayan deyerleri qebul edir")
    return 4 * pi * radius**2



def area_hemisphere(radius: float) -> float:  # Yarim kure
    
    if radius < 0:
        raise ValueError("area_hemisphere() funksiyasi yalnis menfi olmayan deyerleri qebul edir")
    return 3 * pi * radius**2




def area_cone(radius: float, height: float) -> float: # Konus
    
    if radius < 0 or height < 0:
        raise ValueError("area_cone() funksiyasi yalnis menfi olmayan deyerleri qebul edir")
    return pi * radius * (radius + (height**2 + radius**2) ** 0.5)


def area_cylinder(radius: float, height: float) -> float: # Silindir
    
    if radius < 0 or height < 0:
        raise ValueError("area_cylinder() funksiyasi yalnis menfi olmayan deyerleri qebul edir")
    return 2 * pi * radius * (height + radius)



def area_rectangle(length: float, width: float) -> float:  # Duzbucaqli
    
    if length < 0 or width < 0:
        raise ValueError("area_rectangle() funksiyasi yalnis menfi olmayan deyerleri qebul edir")
    return length * width



def area_square(side_length: float) -> float: # Kvadrat
    
    if side_length < 0:
        raise ValueError("area_square() funksiyasi yalnis menfi olmayan deyerleri qebul edir")
    return side_length**2



def area_triangle(base: float, height: float) -> float:  # Ucbucaq
    
    if base < 0 or height < 0:
        raise ValueError("area_triangle() funksiyasi yalnis menfi olmayan deyerleri qebul edir")
    return (base * height) / 2



def area_triangle_three_sides(side1: float, side2: float, side3: float) -> float: # Ucbucagin sahesi (beraber terefli)
    
    if side1 < 0 or side2 < 0 or side3 < 0:
        raise ValueError("area_triangle_three_sides() funksiyasi yalnis menfi olmayan deyerleri qebul edir")
    elif side1 + side2 < side3 or side1 + side3 < side2 or side2 + side3 < side1:
        raise ValueError("Girilen deyerler beraber terefli ucbucaq yaratmir")
    semi_perimeter = (side1 + side2 + side3) / 2
    area = sqrt(
        semi_perimeter
        * (semi_perimeter - side1)
        * (semi_perimeter - side2)
        * (semi_perimeter - side3)
    )
    return area




def area_parallelogram(base: float, height: float) -> float:  # Paraleloqram
    
    if base < 0 or height < 0:
        raise ValueError("area_parallelogram() funksiyasi yalnis menfi olmayan deyerleri qebul edir")
    return base * height



def area_trapezium(base1: float, base2: float, height: float) -> float:  # Trapesiya
    
    if base1 < 0 or base2 < 0 or height < 0:
        raise ValueError("area_trapezium() funksiyasi yalnis menfi olmayan deyerleri qebul edir")
    return 1 / 2 * (base1 + base2) * height



def area_circle(radius: float) -> float:   # Daire
     
    if radius < 0:
        raise ValueError("area_circle() funksiyasi yalnis menfi olmayan deyerleri qebul edir")
    return pi * radius**2



def area_ellipse(radius_x: float, radius_y: float) -> float:   # Ellips
    
    if radius_x < 0 or radius_y < 0:
        raise ValueError("area_ellipse() funksiyasi yalnis menfi olmayan deyerleri qebul edir")
    return pi * radius_x * radius_y




def area_rhombus(diagonal_1: float, diagonal_2: float) -> float:  # Romb
    
    if diagonal_1 < 0 or diagonal_2 < 0:
        raise ValueError("area_rhombus() funksiyasi yalnis menfi olmayan deyerleri qebul edir")
    return 1 / 2 * diagonal_1 * diagonal_2
































