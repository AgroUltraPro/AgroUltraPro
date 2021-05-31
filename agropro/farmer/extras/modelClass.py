import numpy as np 
import cv2
import os
import pickle
import pandas as pd

import tflearn
from tflearn.layers.core import input_data,fully_connected,dropout
from tflearn.layers.conv import conv_2d,max_pool_2d,conv_3d,max_pool_3d
from tflearn.layers.estimator import regression

# class CNN:
#     def __init__(self):
        # self.IMG_SIZE = 300
        # self.LR = 1e-3
        # self.ModelName = 'farmer\extras\classifyModel2DSoil.tflearn'

        # network = input_data(shape = [None,self.IMG_SIZE,self.IMG_SIZE,1],name='input')

        # network = conv_2d(network,32, 5,activation = 'relu')
        # network = max_pool_2d(network,5)

        # network = conv_2d(network,64,5,activation = 'relu')
        # network = max_pool_2d(network,5)

        # network = conv_2d(network,128, 5,activation = 'relu')
        # network = max_pool_2d(network,5)  

        # network = conv_2d(network,64,5,activation = 'relu')
        # network = max_pool_2d(network,5)

        # network = conv_2d(network,32, 5,activation = 'relu')
        # network = max_pool_2d(network,5)    

        # network = fully_connected(network, 1024, activation = 'relu' )
        # network = dropout(network, 0.8)

        # network = fully_connected(network, 4, activation = 'softmax' )
        # network = regression(network, optimizer='adam',learning_rate=0.001,loss='categorical_crossentropy',name='targets')

        # self.model = tflearn.DNN(network)

        # self.model.load(self.ModelName)
        # # print('an error occured')
        

    
    # def prediction(self,image):
    #     image = np.fromstring(image.read(),np.uint8)
    #     print('The first image data is: ',image)
    #     imageDecode = cv2.imdecode(image,cv2.IMREAD_GRAYSCALE)
    #     image = cv2.resize(imageDecode,(300,300))
    #     image_stream = np.array(image)

    #     print('The image array is: ',image_stream)
    #     result = self.model.predict([image_stream.reshape(300,300,1)])[0]

    #     print('The results in class are: ',result)
    #     answer = {}
    #     index = np.argmax(result)
    #     answer['percent'] = result[index]*100
    #     if(index == 0):
    #         answer['output'] = 'Red'
    #         # answer['percent'] = result[0]*100
    #     elif(index == 1):
    #         answer['output'] = 'Clay'
    #     elif(index == 2):
    #         answer['output'] = 'Black'
    #     elif(index == 3):
    #         answer['output'] = 'Alluvial'
    #         # answer['percent'] = result[1]*100

    #     return answer




class CropPredict:
    def __init__(self):
        self.filename = 'farmer/extras/finalized_model2.sav'
        self.model = pickle.load(open(self.filename, 'rb'))
        # self.modelCrop = ['Crop_Apple', 'Crop_Arcanut (Processed)', 'Crop_Arecanut', 'Crop_Arhar/Tur', 'Crop_Ash Gourd', 'Crop_Atcanut (Raw)', 'Crop_Bajra', 'Crop_Banana', 'Crop_Barley', 'Crop_Bean', 'Crop_Beans & Mutter(Vegetable)', 'Crop_Beet Root', 'Crop_Ber', 'Crop_Bhindi', 'Crop_Bitter Gourd', 'Crop_Black pepper', 'Crop_Blackgram', 'Crop_Bottle Gourd', 'Crop_Brinjal', 'Crop_Cabbage', 'Crop_Cardamom', 'Crop_Carrot', 'Crop_Cashewnut', 'Crop_Cashewnut Processed', 'Crop_Cashewnut Raw', 'Crop_Castor seed', 'Crop_Cauliflower', 'Crop_Citrus Fruit', 'Crop_Coconut ', 'Crop_Coffee', 'Crop_Colocosia', 'Crop_Cond-spcs other', 'Crop_Coriander', 'Crop_Cotton(lint)', 'Crop_Cowpea(Lobia)', 'Crop_Cucumber', 'Crop_Drum Stick', 'Crop_Dry chillies', 'Crop_Dry ginger', 'Crop_Garlic', 'Crop_Ginger', 'Crop_Gram', 'Crop_Grapes', 'Crop_Groundnut', 'Crop_Guar seed', 'Crop_Horse-gram', 'Crop_Jack Fruit', 'Crop_Jobster', 'Crop_Jowar', 'Crop_Jute', 'Crop_Jute & mesta', 'Crop_Kapas', 'Crop_Khesari', 'Crop_Korra', 'Crop_Lab-Lab', 'Crop_Lemon', 'Crop_Lentil', 'Crop_Linseed', 'Crop_Litchi', 'Crop_Maize', 'Crop_Mango', 'Crop_Masoor', 'Crop_Mesta', 'Crop_Moong(Green Gram)', 'Crop_Moth', 'Crop_Niger seed', 'Crop_Oilseeds total', 'Crop_Onion', 'Crop_Orange', 'Crop_Other  Rabi pulses', 'Crop_Other Cereals & Millets', 'Crop_Other Citrus Fruit', 'Crop_Other Dry Fruit', 'Crop_Other Fresh Fruits', 'Crop_Other Kharif pulses', 'Crop_Other Vegetables', 'Crop_Paddy', 'Crop_Papaya', 'Crop_Peach', 'Crop_Pear', 'Crop_Peas  (vegetable)', 'Crop_Peas & beans (Pulses)', 'Crop_Perilla', 'Crop_Pineapple', 'Crop_Plums', 'Crop_Pome Fruit', 'Crop_Pome Granet', 'Crop_Potato', 'Crop_Pulses total', 'Crop_Pump Kin', 'Crop_Ragi', 'Crop_Rajmash Kholar', 'Crop_Rapeseed &Mustard', 'Crop_Redish', 'Crop_Ribed Guard', 'Crop_Rice', 'Crop_Ricebean (nagadal)', 'Crop_Rubber', 'Crop_Safflower', 'Crop_Samai', 'Crop_Sannhamp', 'Crop_Sapota', 'Crop_Sesamum', 'Crop_Small millets', 'Crop_Snak Guard', 'Crop_Soyabean', 'Crop_Sugarcane', 'Crop_Sunflower', 'Crop_Sweet potato', 'Crop_Tapioca', 'Crop_Tea', 'Crop_Tobacco', 'Crop_Tomato', 'Crop_Total foodgrain', 'Crop_Turmeric', 'Crop_Turnip', 'Crop_Urad', 'Crop_Varagu', 'Crop_Water Melon', 'Crop_Wheat', 'Crop_Yam', 'Crop_other fibres', 'Crop_other misc. pulses', 'Crop_other oilseeds']
        # self.modelSeason = ['Season_Autumn     ', 'Season_Kharif     ', 'Season_Rabi       ', 'Season_Summer     ', 'Season_Whole Year ', 'Season_Winter     ']
        # self.modelState_Name = ['State_Name_Andaman and Nicobar Islands', 'State_Name_Andhra Pradesh', 'State_Name_Arunachal Pradesh', 'State_Name_Assam', 'State_Name_Bihar', 'State_Name_Chandigarh', 'State_Name_Chhattisgarh', 'State_Name_Dadra and Nagar Haveli', 'State_Name_Goa', 'State_Name_Gujarat', 'State_Name_Haryana', 'State_Name_Himachal Pradesh', 'State_Name_Jammu and Kashmir ', 'State_Name_Jharkhand', 'State_Name_Karnataka', 'State_Name_Kerala', 'State_Name_Madhya Pradesh', 'State_Name_Maharashtra', 'State_Name_Manipur', 'State_Name_Meghalaya', 'State_Name_Mizoram', 'State_Name_Nagaland', 'State_Name_Odisha', 'State_Name_Puducherry', 'State_Name_Punjab', 'State_Name_Rajasthan', 'State_Name_Sikkim', 'State_Name_Tamil Nadu', 'State_Name_Telangana ', 'State_Name_Tripura', 'State_Name_Uttar Pradesh', 'State_Name_Uttarakhand', 'State_Name_West Bengal']
        self.modelCrop = ['Crop_Urad', 'Crop_Mesta', 'Crop_Arhar/Tur', 'Crop_Sugarcane', 'Crop_Cardamom', 'Crop_Soyabean', 'Crop_Coriander', 'Crop_Cashewnut', 'Crop_other oilseeds', 'Crop_Jack Fruit', 'Crop_Cowpea(Lobia)', 'Crop_Dry chillies', 'Crop_Gram', 'Crop_Tapioca', 'Crop_Moong(Green Gram)', 'Crop_Maize', 'Crop_Tobacco', 'Crop_Black pepper', 'Crop_Ragi', 'Crop_Wheat', 'Crop_Coconut ', 'Crop_Niger seed', 'Crop_Khesari', 'Crop_Masoor', 'Crop_Moth', 'Crop_Dry ginger', 'Crop_Castor seed', 'Crop_Sannhamp', 'Crop_Sunflower', 'Crop_Other Cereals & Millets', 'Crop_Rice', 'Crop_Other Kharif pulses', 'Crop_Banana', 'Crop_Groundnut', 'Crop_Horse-gram', 'Crop_Guar seed', 'Crop_Barley', 'Crop_Garlic', 'Crop_Cabbage', 'Crop_Rapeseed &Mustard', 'Crop_Cotton(lint)', 'Crop_Small millets', 'Crop_Sesamum', 'Crop_Linseed', 'Crop_Jute', 'Crop_Pump Kin', 'Crop_Turmeric', 'Crop_Blackgram', 'Crop_Safflower', 'Crop_Sweet potato', 'Crop_Bajra', 'Crop_Peas & beans (Pulses)', 'Crop_Jowar', 'Crop_Onion', 'Crop_Arecanut', 'Crop_Other  Rabi pulses', 'Crop_Potato']
        self.modelSeason = ['Season_Whole Year ', 'Season_Summer     ', 'Season_Winter     ', 'Season_Autumn     ', 'Season_Rabi       ', 'Season_Kharif     ']
        self.modelState_Name = ['State_Name_Uttar Pradesh', 'State_Name_Goa', 'State_Name_Assam', 'State_Name_Chandigarh', 'State_Name_Andaman and Nicobar Islands', 'State_Name_Rajasthan', 'State_Name_Uttarakhand', 'State_Name_Manipur', 'State_Name_Andhra Pradesh', 'State_Name_Chhattisgarh', 'State_Name_Telangana ', 'State_Name_Puducherry', 'State_Name_Tamil Nadu', 'State_Name_Arunachal Pradesh', 'State_Name_Himachal Pradesh', 'State_Name_Punjab', 'State_Name_Karnataka', 'State_Name_Nagaland', 'State_Name_Bihar', 'State_Name_Mizoram', 'State_Name_Gujarat', 'State_Name_Madhya Pradesh', 'State_Name_Jammu and Kashmir ', 'State_Name_Odisha', 'State_Name_West Bengal', 'State_Name_Kerala', 'State_Name_Maharashtra', 'State_Name_Haryana']

    def processData(self,data):
        inputArray = []

        for i in self.modelState_Name:
            if(data["state"] in i):
                inputArray.append(1)
            else:
                inputArray.append(0)
        
        for i in self.modelSeason:
            if(data["season"] in i):
                inputArray.append(1)
            else:
                inputArray.append(0)
        
        for i in self.modelCrop:
            if("Crop_"+data["crop"] == i):
                inputArray.append(1)
            else:
                inputArray.append(0)
        
        # inputArray.append(data["area"])
        inputArray.append(1)
        print("The given new inputArray is: ",inputArray)

        df = pd.DataFrame([inputArray],columns = self.modelState_Name + self.modelSeason + self.modelCrop + ["Area"])
        print("The input Dataframe is: ",df)

        return df

    
    def prediction(self,data):
        print("Enetered the class prediction function")
        newProcessedData = self.processData(data)
        return self.model.predict(newProcessedData)*data['area']
        # return self.model.predict(newProcessedData)

class CNN2:
    def __init__(self):
        self.IMG_SIZE = 300
        self.LR = 1e-3
        self.ModelName = 'farmer\extras\classifyModel3DSoil.tflearn'

        network = input_data(shape = [None,self.IMG_SIZE,self.IMG_SIZE,3,1],name='input')

        network = conv_3d(network,32,  filter_size=(3, 3, 3),activation = 'relu')
        network = max_pool_3d(network,kernel_size=(2, 2, 2), strides=(5, 5, 5))

        network = conv_3d(network,64, filter_size=(3, 3, 3),activation = 'relu')
        network = max_pool_3d(network,kernel_size=(2, 2, 2), strides=(5, 5, 5))

        # network = conv_2d(network,32, 5,activation = 'relu')
        # network = max_pool_2d(network,5) 

        network = conv_3d(network,128,  filter_size=(3, 3, 3),activation = 'relu')
        network = max_pool_3d(network,kernel_size=(2, 2, 2), strides=(5, 5, 5))  

        # network = conv_2d(network,32, 5,activation = 'relu')
        # network = max_pool_2d(network,5) 

        network = conv_3d(network,64, filter_size=(3, 3, 3),activation = 'relu')
        network = max_pool_3d(network,kernel_size=(2, 2, 2), strides=(5, 5, 5))

        network = conv_3d(network,32,  filter_size=(3, 3, 3),activation = 'relu')
        network = max_pool_3d(network,kernel_size=(2, 2, 2), strides=(5, 5, 5))    

        network = fully_connected(network, 1024, activation = 'relu' )
        network = dropout(network, 0.8)

        network = fully_connected(network, 4, activation = 'softmax' )
        network = regression(network, optimizer='adam',learning_rate=0.001,loss='categorical_crossentropy',name='targets')

        self.model = tflearn.DNN(network)
        self.model.load(self.ModelName)
        # print('an error occured')
        

    
    def prediction(self,image):
        image = np.fromstring(image.read(),np.uint8)
        print('The first image data is: ',image)
        imageDecode = cv2.imdecode(image,cv2.IMREAD_COLOR)
        image = cv2.resize(imageDecode,(300,300))
        image_stream = np.array(image)

        print('The image array is: ',image_stream)
        result = self.model.predict([image_stream.reshape(300,300,3,1)])[0]

        print('The results in class are: ',result)
        answer = {}
        index = np.argmax(result)
        answer['percent'] = result[index]*100
        if(index == 0):
            answer['output'] = 'Red'
            # answer['percent'] = result[0]*100
        elif(index == 1):
            answer['output'] = 'Clay'
        elif(index == 2):
            answer['output'] = 'Black'
        elif(index == 3):
            answer['output'] = 'Alluvial'
            # answer['percent'] = result[1]*100

        return answer