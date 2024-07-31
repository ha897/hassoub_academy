from setuptools import setup
setup(
    name='taskaty',
    version='0.1.0',
    description='A simple command-Line Task-app written in Python',
    author='Mohammed Taher',
    #الحزم المحتاجة 
    install_requires=['tabulate'],
    #تنفيز داله مين بتاسكاتي
    entry_points={
        'console_scripts': [
        'taskaty=taskaty:main',
        ],
    },
  )