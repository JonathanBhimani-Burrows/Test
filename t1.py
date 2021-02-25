import tensorflow as tf



print("Hello world")
print(tf.test.is_gpu_available())
print("TensorFlow version: {}".format(tf.__version__))
Q = tf.Variable([0.3, dtype=tf.float32)]
print(Q)