import tensorflow as tf

def devide(a, b):
  res = ( a / b )
  print_ab = tf.Print(res, [a, b])
  s = tf.where(tf.is_nan(res), print_ab, res)
  return s

with tf.Session() as sess:
  print(sess.run(devide( tf.constant(5), tf.constant(0) )) )
