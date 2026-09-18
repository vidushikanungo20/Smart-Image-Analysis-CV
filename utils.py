import os

def ensure_directories():

    folders = [
        "results",
        "data/sample_images"
    ]

    for folder in folders:

        os.makedirs(
            folder,
            exist_ok=True
        )
