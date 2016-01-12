from distutils.core import setup

setup(
    name='cookie-cutter',
    version='0.2.0',
    packages=['cookie_cutter'],
    package_dir={'cookie_cutter' : '.'}, # look for package contents in current directory
    author='Tyler Krupicka and Jimmy Ly',
    author_email='site@tylerkrupicka.com',
    description='Loads cookies from your browser into a cookiejar object so can download with urllib and other libraries the same content you see in the web browser.',
    url='https://github.com/tylerkrupicka/cookie-cutter',
    install_requires=['pyaes','pbkdf2','keyring'],
    license='lgpl'
)
