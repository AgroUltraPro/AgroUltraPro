import cv2
import os
import numpy as np 
from random import shuffle 
import tflearn
from tflearn.layers.core import input_data,fully_connected,dropout
from tflearn.layers.conv import conv_2d,max_pool_2d,conv_3d,max_pool_3d
from tflearn.layers.estimator import regression




training_data =[]
def generate_training_data():
    for item in os.listdir('Soil_Dataset/train'):
        # print(item)
        if(item == 'Alluvial_Soil'):
            answer = [0,0,0,1]
            # print("yes entered in Alluvial dir")
        elif(item == 'Black_Soil'):
            answer = [0,0,1,0]
        elif(item == 'Clay_Soil'):
            answer = [0,1,0,0]
        elif(item == 'Red_Soil'):
            answer = [1,0,0,0]
        
        for imageName in os.listdir('Soil_Dataset/Train/'+item):
            # print(imageName,"hello came inside here")
            # print(base_dir,"base")
            imagePath = os.path.join(base_dir + '/Soil_Dataset/Train/'+item+'/'+imageName)
            # print("checking for imagePath:",imagePath)
            image = cv2.imread(imagePath)
            # print("Checking for image: ",image)
            image = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
            image = cv2.resize(image,(300,300),interpolation=cv2.INTER_AREA)
            # print(image.shape)
            # cv2.imshow('Test Image',image)
            # cv2.waitKey(0)
           
            # break
            if len(image):
                training_data.append([np.array(image),np.array(answer)])
            
        
    # cv2.destroyAllWindows()
    shuffle(training_data)
    return training_data


def neural_network_model(input_size):
    network = input_data(shape = [None,input_size,input_size,1],name='input')

    network = conv_2d(network,32, 5,activation = 'relu')
    network = max_pool_2d(network,5)

    network = conv_2d(network,64,5,activation = 'relu')
    network = max_pool_2d(network,5)

    network = conv_2d(network,32, 5,activation = 'relu')
    network = max_pool_2d(network,5) 

    network = conv_2d(network,128, 5,activation = 'relu')
    network = max_pool_2d(network,5)  

    network = conv_2d(network,32, 5,activation = 'relu')
    network = max_pool_2d(network,5) 

    network = conv_2d(network,64,5,activation = 'relu')
    network = max_pool_2d(network,5)

    network = conv_2d(network,32, 5,activation = 'relu')
    network = max_pool_2d(network,5)    

    network = fully_connected(network, 1024, activation = 'relu' )
    network = dropout(network, 0.8)

    network = fully_connected(network, 4, activation = 'softmax' )
    network = regression(network, optimizer='adam',learning_rate=0.001,batch_size=32,loss='categorical_crossentropy',name='targets')

    model = tflearn.DNN(network)
    return model


def train_model(train_data, model = False):
    X=np.array([i[0] for i in train_data]).reshape([-1,300,300,1])
    Y=[i[1] for i in train_data]

    if not model:
        model = neural_network_model(input_size=len(X[0][0]))
    
    model.fit({'input':X},{'targets':Y},n_epoch=25,show_metric=True,run_id='classify_Model_Soil')
    return model



# train_data = generate_training_data()
# np.save('train_data_2D_Soil.npy',train_data)
train_data = np.load('train_data_2D_Soil.npy',allow_pickle=True)
print("Process Ended length: ",len(train_data[0][0][0]))

# np.save('train_data_2D.npy',train_data)
# train_data = np.load('train_data_2D.npy',allow_pickle=True)
# print("yess came here")

model = train_model(train_data)
model.save('classifyModel2DSoil2.tflearn')
# model = neural_network_model(input_size=300)
# model.load('classifyModel2D.tflearn')

# testImagePath = os.path.join(base_dir + '/data' + '/' + dirArray[0] + '/predator/' + '173.jpg')
# image = cv2.imread(testImagePath)
# image = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
# image = cv2.resize(image,(300,300),interpolation=cv2.INTER_AREA)

# print("The testing image predicted  is: ",model.predict([image.reshape(300,300,1)]))
# print("Percentage predicted:")
# print(":",model.predict([image.reshape(300,300,1)])[0][0]*100)
# print(",model.predict([image.reshape(300,300,1)])[0][1]*100)


# # print("The argmax is: ",np.argmax(model.predict([image.reshape(300,300,1)])[0]))
# # print(":",dirAnimal[np.argmax(model.predict([image.reshape(300,300,1)])[0])])
# cv2.imshow('Test Image',image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# print(len(train_data[0][0]))