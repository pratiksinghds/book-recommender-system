from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

REPO_NAME = "Book-Recommender-System"
AUTHOR_USER_NAME = "PRATIKSINGH-DS"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = ['streamlit', 'numpy', 'scikit-learn']

setup(
    name=SRC_REPO,
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    description="A small package for Book Recommender System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    author_email="example@gmail.com",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS
)
