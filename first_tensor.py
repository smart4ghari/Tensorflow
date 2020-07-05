import tensorflow as tf
print(tf.version)  #To print the version of the tensorflow
string = tf.Variable("This is a string",tf.string)
#Here to check the rank of the given variable
print(tf.rank(string)) #The output will be tf.Tensor(0, shape=(), dtype=int32) Here '0' represents the rank
list1 = tf.Variable(["hello"],tf.string)
print(tf.rank(list1)) #The output will be tf.Tensor(0, shape=(), dtype=int32) Here '1' represents the rank
#Since list is one dimensional