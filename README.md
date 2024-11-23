# Face Detection with OpenCV

Welcome to the Face Detection with OpenCV project! This repository demonstrates how to implement facial recognition and tracking using OpenCV, a powerful library for computer vision tasks. The project is designed to showcase real-time face detection in images and video.

## Features

- Real-time face detection in webcam video.
- Supports multiple face detection models using OpenCV.
- Easy-to-understand code to help you understand the implementation of face detection.
- Detects and marks faces in images and video feeds.

## Installation

To get started with the project, follow these steps:

1. **Clone the Repository:**

    Clone this repository to your local machine:

    ```bash
    git clone https://github.com/Nehorai444/computer-vision.git
    ```

2. **Install Dependencies:**

    Navigate to the project directory and install the necessary dependencies:

    ```bash
    cd computer-vision
    pip install -r requirements.txt
    ```

    If `requirements.txt` doesn't exist, you can install OpenCV manually with:

    ```bash
    pip install opencv-python
    ```

3. **Run the Project:**

    To run the face detection script on your webcam, use the following command:

    ```bash
    python face_detection.py
    ```

    Alternatively, you can process a static image with:

    ```bash
    python face_detection.py --image path_to_your_image.jpg
    ```

## Usage

- The project allows for both real-time webcam detection and detection from images.
- Once you run the script, a window will pop up showing the detected faces, with bounding boxes around them.
- Press `q` to exit the video feed.

## Technologies Used

- **OpenCV**: Library used for computer vision tasks.
- **Python**: The programming language used for the project.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- OpenCV: [https://opencv.org/](https://opencv.org/)
- The face detection model used in OpenCV: [Haar Cascades](https://github.com/opencv/opencv/tree/master/data/haarcascades)

Happy coding!
