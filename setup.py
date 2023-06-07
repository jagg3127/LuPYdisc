import setuptools

setuptools.setup(
    # Here is the module name.
    name="LuPYdisc",
    version="0.1.0",
    author="Luna",
    description="def go check out AioPY",
    packages=setuptools.find_packages(),

    # if module has dependencies i.e. if your package rely on other package at pypi.org
    # then you must add there, in order to download every requirement of package
    install_requires=["Py-cord", "Discord", "sly"],
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)