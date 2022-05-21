from setuptools import setup, find_packages


setup(
    name="LearnTdd",
    version="0.0.1",
    packages=find_packages("src", include=["LearnTdd"]),
    package_dir={"":"src"}
)

print("finished setup for LearnTdd")