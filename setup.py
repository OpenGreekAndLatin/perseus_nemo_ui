from setuptools import setup, find_packages

setup(
    name='cts_leipzig_ui',
    version="0.0.1",
    packages=find_packages(exclude=["examples", "tests"]),
    url='https://github.com/OpenGreekAndLatin/cts_leipzig_ui',
    license='GNU GPL',
    author='Bridget Almas, Thibault Clérice',
    author_email='leponteineptique@gmail.com',
    description='Aperire UI for Nemo',
    test_suite="tests",
    install_requires=[
        "flask_nemo>=1.0.0b3"
    ],
    tests_require=[
        "capitains_nautilus>=0.0.5"
    ],
    include_package_data=True,
    zip_safe=False
)
