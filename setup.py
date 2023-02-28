from setuptools import setup
setup(
    name = 'imgstg',
    packages = ['imgstg'],
    version = '1.0.0',
    license = 'MTL',
    description = 'python library for image steganography. used to encrypt and decrypt text message inside an image',
    authon = 'Mohammed Sujaid',
    author_email = 'sujaidsujaid1162@gmail.com',
    url = 'https://sujaid.pythonanywhere.com',
    keywords = ['image steganography', 'steganography', 'image', 'sujaid'],
    install_requires = [
        'numpy',
        'Pillow'
    ],
    requires_python = ">=3.8",
    classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    ]
)