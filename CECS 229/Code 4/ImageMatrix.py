import image
from Matrix import Matrix
def png2graymatrix(filename):

    #FIXME: a single line of code should go here
    image_data = image.file2image(filename)
    
    if not image.isgray(image_data):
        image_data = image.color2gray(image_data)#FIXME: make the image grayscale
        
    return Matrix(image_data) #FIXME


def graymatrix2png(img_matrix, path):
    return image.image2file(img_matrix.rowx,path)
    pass