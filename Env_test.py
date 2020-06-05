import tensorflow as tf

tf.compat.v1.disable_eager_execution()  # 保证sess.run()能够运行
matrix1 = tf.constant([[3,3]])
matrix2 = tf.constant([[2], [2]])
product = tf.matmul(matrix1, matrix2)

with tf.compat.v1.Session() as sess:  # 在tensorflow2.0中，Session()改成了compat.v1.Session()
    result2 = sess.run(product)
    print(result2)
