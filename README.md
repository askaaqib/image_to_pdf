# Image to PDF Converter

Convert image files to PDF format with this Django-based web application.

## Description

The **Image to PDF Converter** is a web application built with Django that allows users to upload image files, which are then converted into PDF documents. The application provides a simple and user-friendly interface for performing this task.

**Features:**

- Upload images in common formats (e.g., JPG, PNG, GIF).
- Convert uploaded images into a single PDF document.
- Easily download the resulting PDF file.

## Table of Contents

- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

Make sure you have the following software and tools installed on your system:

- Python 3.7+
- `virtualenv` (for creating a virtual environment)
- Django 3.2+

### Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/askaaqib/image_to_pdf.git
   cd image_to_pdf

2. Create a virtual environment and activate it:

   ```shell
   virtualenv venv
   source venv/bin/activate
 
3. Install project dependencies:

   ```shell
   pip install -r requirements.txt

4. Run database migrations:

   ```shell
   python manage.py makemigrations
   python manage.py migrate
 
1. Clone the repository:

   ```shell
   git clone https://github.com/askaaqib/image_to_pdf.git
   cd image_to_pdf

### Usage

1. Start the Django development server:

   ```shell
   python manage.py runserver
2. Open a web browser and navigate to http://127.0.0.1:8000/pdf_converter/upload/.
3. Upload an image file by clicking the "Choose File" button and then the "Convert" button. The image will be converted to a PDF file, which you can download.

## Contributing

We welcome contributions from the open-source community. To contribute to this project, please follow these guidelines:

1. Fork the repository and create a new branch for your feature or bug fix.
2. Make your changes and ensure that they work as expected.
3. Write clear, concise, and meaningful commit messages.
4. Push your changes to your branch on your fork.
5. Create a pull request to the `main` branch of the original repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Styling

We follow the PEP 8 style guide for Python code. Please adhere to these guidelines when contributing to this project.

 
