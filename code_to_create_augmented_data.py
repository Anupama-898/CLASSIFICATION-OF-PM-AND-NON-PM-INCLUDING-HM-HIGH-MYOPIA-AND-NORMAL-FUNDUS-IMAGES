from keras.preprocessing.image import ImageDataGenerator,img_to_array, load_img
datagen = ImageDataGenerator(

        rotation_range=40,

        width_shift_range=0.2,

        height_shift_range=0.2,

        shear_range=0.2,

        zoom_range=0.2,

        horizontal_flip=True,

        fill_mode='nearest')
j = 100
while(j<213):
	img = load_img(r'C:\Users\User\Desktop\augme. data\preset_myopia\P0'+str(j)+'.jpg')  
	j =j+1

	x = img_to_array(img)  # creating a Numpy array with shape (3, 150, 150)
	x = x.reshape((1,) + x.shape)  # converting to a Numpy array with shape (1, 3, 150, 150)

	i = 0

	for batch in datagen.flow(x,save_to_dir=r'C:\Users\User\Desktop\augme. data\preset_aug', save_prefix='eye', save_format='jpeg'):

		i += 1

		if i > 1:
	
			break

   
