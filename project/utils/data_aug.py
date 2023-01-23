
from keras import layers, Sequential

def create_data_aug_layer(data_aug_layer: dict):
    """
    Use this function to parse the data augmentation methods for the
    experiment and create the corresponding layers.

    It will be mandatory to support at least the following three data
    augmentation methods (you can add more if you want):
        - `random_flip`: keras.layers.RandomFlip()
        - `random_rotation`: keras.layers.RandomRotation()
        - `random_zoom`: keras.layers.RandomZoom()

    See https://tensorflow.org/tutorials/images/data_augmentation.

    Parameters
    ----------
    data_aug_layer : dict
        Data augmentation settings coming from the experiment YAML config
        file.

    Returns
    -------
    data_augmentation : keras.Sequential
        Sequential model having the data augmentation layers inside.
    """
    # Parse config and create layers
    # Append the data augmentation layers on this list
    data_aug_layers = []
    for key, data_aug_parameters in data_aug_layer.items():
        if key == "random_flip":
            data_aug_layers.append(
                layers.RandomFlip(**data_aug_parameters)
            )
        if key == "random_rotation":
            data_aug_layers.append(
                layers.RandomRotation(**data_aug_parameters)
            )
        if key == "random_zoom":
            data_aug_layers.append(
                layers.RandomZoom(**data_aug_parameters)
            )

    # Return a keras.Sequential model having the the new layers created
    # Assign to `data_augmentation` variable
    data_augmentation = Sequential(data_aug_layers) if len(data_aug_layers) else None

    return data_augmentation
