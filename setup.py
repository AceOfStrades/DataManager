from src.VERSION import VERSION as version
from setuptools  import setup, find_packages


# with open('VERSION.txt') as f:
#     version = f.read()

with open('requirements.txt') as f:
    requirements = f.read().split('\n')
    requirements = [i for i in requirements if i]



setup(
    name = 'Datamanager',
    version = version,
    description = 'Datamanager is a full interactive monitoring of overall financial informations from the gathering of data to tacking investment returns of strategies. For more information, please visit https://github.com/MaxWayne/Scrapper',
    author='Maximilien Pelletier',
    author_email='maximilienpelletier@gmail.com',   # py_modules=['mvp_msr8'],
    long_description=open('README.rst', encoding='utf-8').read(),
    long_description_content_type = 'text/markdown',
    platforms = ["Windows", "Linux", "Mac OS-X", "Unix"],
    install_requires = requirements,
    packages=find_packages(),
    include_package_data=True,
    package_dir = {'': 'src'},
    project_urls={
        'Bug Tracker': 'https://github.com/MaxWayne/Scrapper/issues',
        'Source Code': 'https://github.com/MaxWayne/Scrapper',
    },
    keywords='django assets staticfiles Node.js npm package.json',
    classifiers = [
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Framework :: Django',
        'Framework :: Django :: 4.0',
        'License :: OSI Approved :: Appache2.0',
        'Operating System :: OS Independent',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: MacOS'
    ]
)


'''
name:        what you will pip install, not import
py_modules:  what they will import
!! NAME OF THE MAIN FILE IN THE src DIR SHOULD BE SAME AS PACKAGE NAME
'''
