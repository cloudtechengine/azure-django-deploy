from setuptools import setup, find_packages

setup(
    name='Articlesapp',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
        asgiref==3.8.1
        cffi==1.16.0
        crispy-bootstrap5==2024.2
        cryptography==42.0.5
        Django==5.0.4
        django-crispy-forms==2.1
        pillow==10.3.0
        pycparser==2.22
        PyMySQL==1.1.0
        sqlparse==0.5.0
        tzdata==2024.1
    ],
)
