import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
f = open("requirements.txt","w")
f.write('requests\nuser_agent\njson\nsecrets\nnames\nhashlib\nurllib\nuuid\nre\nmechanize\ninstaloader ')

fr = open("requirements.txt",'r')
requires = fr.read().split('\n')
    
setuptools.setup(
    name="SalamHunter",
    version="1.0.1",
    author="salammzere3",
    author_email="salamhunter@gmail.com",
    description="• Script Very Nice To Helping Programmer .",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/salammzere3/SalamHunterr",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9",
    install_requires=requires,
)
