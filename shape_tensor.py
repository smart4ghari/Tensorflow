import tensorflow as tf
#Shape of Tensors
rank1_tensor = tf.Variable([["Number","Name","Time"],["1","2","3"]],tf.string)
print(rank1_tensor.shape)   #This will print the shape of the rank1_tensor
#The output will be in this format (2, 3) contains 2 lists and 3 elements
'''>>>>>>>>>>>Changing Shapes<<<<<<<<<<<'''
ones_tensor = tf.ones([1,2,3])
reshaped = tf.reshape(ones_tensor,[2,3,1])
print(reshaped)

zeros_tensor = tf.zeros([5,5,5])    #This should return 125 elements with 5 shapes, 5 lists, 5 elements
print(zeros_tensor)
