import cv2
import numpy as np
from PIL import Image
from check_required_deps import check_required_deps
from download_models import download_models


def upscale_image(input_path, output_path, scale_factor=2, method="sr"):
    """
    Upscale an image keeping high quality.

    Args:
        input_path: original image path
        output_path: saving path for the upscaled image
        scale_factor: upscaling factor (default: 2)
        method: upscaling method ("sr", "bicubic", "lanczos")
    """
    # Read image
    if method == "sr":
        # Super Resolution method
        img = cv2.imread(input_path)
        if img is None:
            print(f"Error: impossible to read image {input_path}")
            return

        # RGB conversion
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Create super resolution object
        sr = cv2.dnn_superres.DnnSuperResImpl_create()

        # Choose model in function of scale factor
        model_path = None
        if scale_factor == 2:
            model_path = "ESPCN_x2.pb"
            model_name = "espcn"
        elif scale_factor == 3:
            model_path = "ESPCN_x3.pb"
            model_name = "espcn"
        elif scale_factor == 4:
            model_path = "ESPCN_x4.pb"
            model_name = "espcn"
        else:
            print(f"Scale factor {scale_factor} not supported for super resolution")
            print("using laczos as fallback")
            method = "lanczos"

        if model_path:
            try:
                sr.readModel(model_path)
                sr.setModel(model_name, scale_factor)
                result = sr.upsample(img)
                result_rgb = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)

                # Convert to PIL for saving with DPI
                pil_img = Image.fromarray(result_rgb)

                # Get original DPI or use default
                original_img = Image.open(input_path)
                original_dpi = original_img.info.get('dpi', (96, 96))

                # Scale DPI according to scale factor
                new_dpi = (int(original_dpi[0] * scale_factor), int(original_dpi[1] * scale_factor))

                # Save with new DPI
                pil_img.save(output_path, dpi=new_dpi)
                print(f"Successfully upscaled image using super resolution (factor {scale_factor})")
                print(f"New DPI: {new_dpi}")
                return
            except Exception as e:
                print(f"Error in uploading super resolution model: {e}")
                print("using laczos as fallback")
                method = "lanczos"

    # Alternative methods
    img = Image.open(input_path)

    # Get original DPI or use default
    original_dpi = img.info.get('dpi', (96, 96))

    # Scale DPI according to scale factor
    new_dpi = (int(original_dpi[0] * scale_factor), int(original_dpi[1] * scale_factor))

    if method == "bicubic":
        # upscaling with bicubic interpolation (good for drawings)
        new_size = (int(img.width * scale_factor), int(img.height * scale_factor))
        upscaled_img = img.resize(new_size, Image.BICUBIC)
        upscaled_img.save(output_path, dpi=new_dpi)
        print(f"Image upscaled successfully using bicubic interpolation (factor {scale_factor})")
        print(f"New DPI: {new_dpi}")

    elif method == "lanczos":
        # Upscaling using Lanczos algorithm (good for photos)
        new_size = (int(img.width * scale_factor), int(img.height * scale_factor))
        upscaled_img = img.resize(new_size, Image.LANCZOS)
        upscaled_img.save(output_path, dpi=new_dpi)
        print(f"Image upscaled successfully using lanczos (factor {scale_factor})")
        print(f"New DPI: {new_dpi}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Upscale images keeping high quality')
    parser.add_argument('input', help='Image path to be upscaled \'Image')
    parser.add_argument('output', help='Target path where to save \'image')
    parser.add_argument('--scale', type=float, default=2.0, help='Scale factor (default: 2.0)')
    parser.add_argument('--method', type=str, default='sr',
                        choices=['sr', 'bicubic', 'lanczos'],
                        help='Upscaling method (default: sr)')
    parser.add_argument('--download-models', action='store_true',
                        help='Download models per super-resolution')

    args = parser.parse_args()
    check_required_deps()
    if args.download_models:
        download_models()

    upscale_image(args.input, args.output, args.scale, args.method)