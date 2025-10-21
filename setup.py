from setuptools import setup, find_packages

setup(
    name="Blowing_Smoke",
    version="0.1.1",
    packages=find_packages(),
    install_requires=[
        "Faker>=23.0.0"
    ],
    entry_points={
        "console_scripts": [
            "fake_data=Blowing_Smoke_pkg.generate_fake_data:main"
        ]
    },
    python_requires='>=3.8',
    description="Fake employee, performance, and character data generator",
    author="Jesse Vargas",
    url="https://github.com/jessejamesva/Blowing_Smoke",
)
