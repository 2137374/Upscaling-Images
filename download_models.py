def download_models():
    """
    Download pre-trained super-resolution models
    """
    import os
    import urllib.request

    models = {
        "ESPCN_x2.pb": "https://github.com/fannymonori/TF-DNN-SuperResolution/raw/master/ESPCN/ESPCN_x2.pb",
        "ESPCN_x3.pb": "https://github.com/fannymonori/TF-DNN-SuperResolution/raw/master/ESPCN/ESPCN_x3.pb",
        "ESPCN_x4.pb": "https://github.com/fannymonori/TF-DNN-SuperResolution/raw/master/ESPCN/ESPCN_x4.pb"
    }

    for model_name, url in models.items():
        if not os.path.exists(model_name):
            print(f"Downloading model {model_name}...")
            try:
                urllib.request.urlretrieve(url, model_name)
                print(f"Model {model_name} downloaded successfully!")
            except Exception as e:
                print(f"Error downloading model {model_name}: {e}")