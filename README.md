# Upscaling-Images
Upscaling Images using openCV dependencies.
Techniques used are:
- SR
- Bicubic
- Lanczos

To use SR technique only [2, 3, 4] upscaling factors are allowed. For Bicubic and Lanczos, any upscaling factor can be used.

To run: 
"python main.py input.jpg output.jpg --scale 2 --method bicubic --download-models"
Another script "DPIHandling.py" is present if changing DPI is needed in order to print images.

License
This project is licensed under the MIT License. See the LICENSE file for full details.
Copyright (c) [Year] [Your Name]
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED.
