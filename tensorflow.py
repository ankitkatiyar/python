# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 15:20:19 2018

@author: katiyar.a
"""

import tensorflow as tf

# Create two constants
x1 = tf.constant([1,2,3,4])
x2 = tf.constant([4,3,2,1])

# multiply 
result = tf.multiply(x1,x2);

# print
print(result);

# results are not calculated  until you run them inside a session so create a session and run this session

# notice the Capiltal S in Session
sess= tf.Session();

print(sess.run(result))

# clsoe the session
sess.close();


# using autocloase manner of the session
# Initialize Session and run `result`
with tf.Session() as sess:
  output = sess.run(result)
  print(output)
  
  
# sessions can also be configurable
sess= tf.Session(config=tf.ConfigProto(allow_soft_placement=True,
                                        log_device_placement=True));
print(sess.run(result))
sess.close()
  
  
  
  
  
  
  
  
  
  
  
  
  