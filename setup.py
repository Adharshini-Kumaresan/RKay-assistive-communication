from setuptools import setup, find_packages

setup(
    name="rkay_assistive_communication",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "opencv-python",
        "numpy",
        "pyaudio",
        "flask",
    ],
)
