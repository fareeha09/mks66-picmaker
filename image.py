import math

width = 500
height = 500

#list that will hold the pixel data for image
colors=[]

def produce_image():
	
	file = open('image.ppm','w')
	file.write('P3\n'+ str(width) + '\n' + str(height) + '\n' + '225\n')
	
	r = 255
	g = 0
	b = 0
	
	for i in range(width):
		for k in range(height):
			r = r-1
			g = g+1 
			b = b+1
			file.write("{} {} {}".format(r, g, b))
			#colors.append("{} {} {}".format(r, g, b))
		
	file.close

if __name__  == "__main__":
	produce_image()
			
	

