from setuptools import setup

setup(name="trajectory-extractor",
      version='1.0b',
      description='Python implementation of a trajectory extractor from traffic camera',
      install_requires=['numpy',
                        'PyYAML',
                        'matplotlib',
                        'pandas',
                        'pytest',
                        'scikit-image',
                        'Cython',
                        'tensorflow==1.15.2',
                        'Keras',
                        'IPython',
                        'imgaug',
                        'scipy',
                        'pandas',
                        'pycocotools',
                        'opencv-python',
                        'opencv-contrib-python'])
