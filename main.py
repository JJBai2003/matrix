from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()

#Test print_matrix
print("test print_matrix [1,2,3,1], [2,3,4,1], [3,4,5,1], [4,5,6,1]")
matrix1 = [[1,2,3,1], [2,3,4,1], [3,4,5,1], [4,5,6,1]]
print_matrix(matrix1)
print()

#Testing add_edge 
m1 = new_matrix()
m2 = new_matrix(rows = 0)
add_edge(m2,1,2,3,4,5,6)
print("Testing add_edge. Adding (1, 2, 3), (4, 5, 6) m2 =")
print_matrix(m2)

#Testing ident.
print("Testing ident. m1 =")
ident(m1)
print_matrix(m1)

#Testing Matrix mult. 
print("Testing Matrix mult. m1 * m2 =")
matrix_mult(m1, m2)
print_matrix(m2)

#Testing Matrix multi.  (pt2)
m1 = new_matrix(rows=0)
add_edge(m1, 1, 2, 3, 4, 5, 6)
add_edge(m1, 7, 8, 9, 10, 11, 12)
print("Testing Matrix mult. m1 =")
print_matrix(m1)

#Testing Matrix multi. (pt2 contin.)
matrix_mult(m1, m2)
print("Testing Matrix mult. m1 * m2 =")
print_matrix(m2)




#For the image
drawing = new_matrix(rows = 0)
color = [175,255,156]

#outline
add_edge(drawing, 100,400,0,100,150,0)
add_edge(drawing, 400,400,0,400,150,0)
add_edge(drawing, 100,150,0,175,100,0)
add_edge(drawing, 400,150,0,325,100,0)
add_edge(drawing, 175,100,0,325,100,0)
add_edge(drawing, 100,400,0,200,300,0)
add_edge(drawing, 400,400,0,300,300,0)
add_edge(drawing, 200,300,0,300,300,0)

#ears
#left
add_edge(drawing, 110,375,0,110,300,0)
add_edge(drawing, 110,300,0,175,300,0)
add_edge(drawing, 110,375,0,175,300,0)

#right
add_edge(drawing, 390,375,0,390,300,0)
add_edge(drawing, 390,300,0,315,300,0)
add_edge(drawing, 390,375,0,315,300,0)



#eyes
#right
add_edge(drawing, 165,250,0,165,200,0)
add_edge(drawing, 165,200,0,215,200,0)
add_edge(drawing, 215,200,0,215,250,0)
add_edge(drawing, 215,250,0,165,250,0)
#inside
add_edge(drawing, 180,250,0,180,200,0)
add_edge(drawing, 200,250,0,200,200,0)
#left
add_edge(drawing, 325,250,0,325,200,0)
add_edge(drawing, 325,200,0,275,200,0)
add_edge(drawing, 275,200,0,275,250,0)
add_edge(drawing, 275,250,0,325,250,0)
#inside
add_edge(drawing, 290,250,0,290,200,0)
add_edge(drawing, 310,250,0,310,200,0)

#nose
add_edge(drawing, 225,190,0,245,175,0)
add_edge(drawing, 245,175,0,265,190,0)
add_edge(drawing, 265,190,0,225,190,0)
add_edge(drawing, 245,175,0,245,150,0)

#mouth
add_edge(drawing, 245,150,0,225,125,0)
add_edge(drawing, 225,125,0,205,150,0)
add_edge(drawing, 245,150,0,265,125,0)
add_edge(drawing, 265,125,0,285,150,0)




draw_lines(drawing, screen, color )

save_ppm_ascii(screen, 'pic2.ppm')
save_extension(screen, 'cat.png')
display(screen)
