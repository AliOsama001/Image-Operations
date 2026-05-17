# Image-Operations

A comprehensive Python application for performing various image processing operations with an interactive Streamlit-based user interface.

## Overview

Image-Operations is a feature-rich image processing tool that provides implementations of fundamental image processing algorithms. It offers both a command-line interface and a web-based UI powered by Streamlit, allowing users to perform advanced image manipulation and analysis tasks.

## Features

### Core Image Processing Modules

- **Point Operations** - Pixel-level transformations and adjustments
- **Color Operations** - Color space conversions and color-based manipulations
- **Histogram Processing** - Histogram analysis, equalization, and manipulation
- **Edge Detection** - Multiple edge detection algorithms
- **Segmentation** - Image segmentation techniques for region extraction
- **Mathematical Morphology** - Morphological operations (dilation, erosion, opening, closing)
- **Neighborhood Processing** - Convolution, filtering, and local operations
- **Image Restoration** - Noise reduction and image enhancement techniques

### User Interface

- Interactive Streamlit web application
- Real-time image preview
- User-friendly controls for all operations
- Multiple operation modes accessible from the main menu

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup Instructions

1. **Clone or download the repository**

   ```bash
   cd Image-Operations
   ```

2. **Create a virtual environment (recommended)**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Streamlit Application

```bash
streamlit run run.py
```

The application will open in your default web browser at `http://localhost:8501`

### Project Structure

```
Image-Operations/
├── run.py                          # Main entry point for Streamlit app
├── requirements.txt                # Python dependencies
├── README.md                       # This file
│
├── src/
│   ├── core/                       # Core image processing algorithms
│   │   ├── point_ops.py           # Point-wise operations
│   │   ├── color_ops.py           # Color space operations
│   │   ├── histogram.py           # Histogram operations
│   │   ├── segmentation.py        # Image segmentation
│   │   ├── edge_detection.py      # Edge detection algorithms
│   │   ├── mathematical_morphology.py  # Morphological operations
│   │   ├── neighborhood_processing.py  # Filtering and convolution
│   │   └── image_restoration.py   # Image enhancement and restoration
│   │
│   └── ui/                         # Streamlit UI components
│       ├── point_ops.py
│       ├── color_ops.py
│       ├── histogram.py
│       ├── segmentation.py
│       ├── edge_detection.py
│       ├── mathematical_morphology.py
│       ├── neighborhood_processing.py
│       └── restoration.py
```

## Dependencies

Key dependencies include:

- **opencv-python** - Computer vision library for image processing
- **numpy** - Numerical computing library
- **pillow** - Python Imaging Library
- **streamlit** - Web application framework
- **pandas** - Data manipulation library
- **scipy** - Scientific computing (via transitive dependencies)

For a complete list, see `requirements.txt`

## How to Run

### Direct Streamlit Run

```bash
streamlit run run.py
```

## Module Guide

### Core Operations (`src/core/`)

Each module in the core package implements image processing algorithms:

- **point_ops.py** - Brightness, contrast, and threshold adjustments
- **color_ops.py** - RGB, HSV, grayscale conversions
- **histogram.py** - Histogram equalization, analysis, and matching
- **edge_detection.py** - Sobel, Canny, Laplacian edge detection
- **segmentation.py** - Thresholding, watershed, k-means segmentation
- **mathematical_morphology.py** - Dilation, erosion, opening, closing
- **neighborhood_processing.py** - Blur, sharpen, custom kernels
- **image_restoration.py** - Denoising, inpainting, enhancement

### UI Components (`src/ui/`)

Streamlit-based user interface modules that wrap core operations with interactive controls and visualization.

## Getting Started

1. Run the application: `streamlit run run.py`
2. Upload an image using the file uploader
3. Select an operation from the sidebar menu
4. Adjust parameters using the interactive controls
5. View results in real-time and download the processed image

## Requirements

See `requirements.txt` for all Python package dependencies. The project primarily relies on:

- OpenCV (cv2)
- NumPy
- Streamlit

## Author

AbdElrahman Maher

## Support

For issues or questions, please 01013270651
