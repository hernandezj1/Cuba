from pdf2image import convert_from_path
 
 
# Store Pdf with convert_from_path function
images = convert_from_path('C:/Users/joseh/Cuba/sitios_de_las_cordilleras_servicio.pdf', poppler_path=r'C:\Users\joseh\Cuba\poppler-23.08.0\Library\bin')
 
for i in range(len(images)):
   
      # Save pages as images in the pdf
    images[i].save('page'+ str(i) +'.jpg', 'JPEG')