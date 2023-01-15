# use "conda activate tf" to use this script
import tensorflow as tf

print("GPU memory: ", tf.test.gpu_device_name() )

gpus = tf.config.list_physical_devices('GPU')
