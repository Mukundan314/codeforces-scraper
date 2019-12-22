from setuptools import setup

setup(
    name="codeforces-scraper",
    version="0.1.0",
    author="mukundan314",
    author_email="mukundan314@gmail.com",
    url="https://github.com/mukundan314/codeforces-scraper",
    py_modules=["codeforces_scraper"],
    entry_points={
        'console_scripts': ['codeforces-scraper=codeforces_scraper:main']
    }
)
