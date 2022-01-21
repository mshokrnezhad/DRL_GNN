import tensorflow as tf

c = tf.constant([[1,2,3,4], [5,6,7,8], [4,3,2,1]])

print(tf.math.unsorted_segment_sum(data=c, segment_ids=tf.constant([0, 1, 2]), num_segments=3))