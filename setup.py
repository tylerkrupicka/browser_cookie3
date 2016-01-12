from distutils.core import setup

setup(
    name='cookie-cutter',
    version='0.2.0',
    packages=['cookie-cutter'],
    package_dir={'cookie-cutter' : '.'}, # look for package contents in current directory
    author='Tyler Krupicka and Jimmy Ly',
    author_email='site@tylerkrupicka.com',
    description='Retrieves cookies from Chrome and Firefox and returns them as a cookie jar.',
    url='https://github.com/tylerkrupicka/cookie-cutter',
    install_requires=['pyaes','pbkdf2','keyring'],
    license='lgpl'
)
