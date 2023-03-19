def make_car(manufacturer, model_name, **features):
    features['manufacturer'] = manufacturer
    features['model_name'] = model_name

    return features

