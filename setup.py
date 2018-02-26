from distutils.core import setup

setup(
    name='pyautomonkey',
    version='0.1dev',
    packages=['pyautomonkey'],
    license='apache',
    long_description=open('README.md').read(),
    install_requires=[
        "Desktopmagic >= 14.3.11",
        "numpy >= 1.13.0",
        "Pillow >= 4.0.0",
        "pywin32 >= 220",
        "opencv-python >= 3.4.0.12"
    ],
)
