from setuptools import find_packages, setup


version = "9.0.0"


extras_require = {
    "images": ["Pillow"],
}


setup(
    name="incuna-test-utils",
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    version=version,
    description="Custom TestCases and other test helpers for Django apps",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Incuna",
    author_email="admin@incuna.com",
    url="https://github.com/incuna/incuna-test-utils/",
    install_requires=[],
    extras_require=extras_require,
    zip_safe=False,
    license="BSD",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Testing",
    ],
)
