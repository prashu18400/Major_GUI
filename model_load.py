from keras.models import load_model


def model_load():
    model = load_model('Age_detection_20.h5')
    return model


