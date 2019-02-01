all:
	python image.py
	display image.ppm
	
clean:
	rm image.ppm