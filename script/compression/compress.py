import tinify as tf


def compress(file):
    '''Jofer's Tinify API Key'''
    tf.key = "v6xM0hKM0pN2p8XCRQ0KGbpSQMHfLwXr"

    result_data = tf.from_buffer(file).to_buffer()
    return result_data
