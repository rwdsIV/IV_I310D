def volume_of_sphere(radius):
	pi = 3.14
	area = 4/3 * pi * radius * radius * radius
	return area

radius1 = 30
area1 = volume_of_sphere(radius1)
print(f"The area of circle with radius {radius1} is: {area1}")

radius2 = 40
area2 = volume_of_sphere(radius2)
print(f"The area of circle with radius {radius2} is: {area2}")