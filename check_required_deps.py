def check_required_deps():
    """
    Verify necessary dependencies
    """
    try:
        import cv2
        if not hasattr(cv2, 'dnn_superres'):
            print("Module is not available in your OPENCV version.")
    except ImportError:
        print("OpenCV not installed. Run 'pip install opencv-python'")

    try:
        from PIL import Image
    except ImportError:
        print("Pillow not installed. Run 'pip install pillow'")
