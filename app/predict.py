# -*- coding: utf-8 -*-
import tensorflow as tf

def main(x):
    # 定义标签
    class_names = ['Iris setosa', 'Iris versicolor', 'Iris virginica']
    #模型路径并加载出来
    file_path = './model'
    model = tf.keras.models.load_model(file_path + "/iris-model")
    predict_dataset = tf.convert_to_tensor([
    x])
    predictions = model(predict_dataset)
    print(predictions)
    class_idx = tf.argmax(predictions,axis=1).numpy()[0]
    print(class_idx)
    result = class_names[class_idx]
    return result


if __name__ == '__main__':
    dataInput=[5.1,3.3,1.7,0.5]
    name = main(dataInput)
    print(name)
    
    