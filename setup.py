import setuptools

# read the contents of your README file
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'space_time_a_star',         # How you named your package folder (MyLib)
    version = '1.0',      # Start with a small number and increase it with every change you make
    author = 'Haoran Peng',
    author_email = 'gavinsweden@gmail.com',
    maintainer = "Pengyuan Wei",
    maintainer_email = "ucabpw3@ucl.ac.uk",
    url = 'https://github.com/pengyuanwei/space_time_a_star',   # Provide either the link to your github or to your website
    description = 'A* search algorithm with an added time dimension to deal with dynamic obstacles.',   # Give a short description about your library
    long_description = long_description,
    long_description_content_type = 'text/markdown',   

    license = 'MIT',    # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    keywords = ['multi-agent-path-finding', 'anonymous-agent', 'conflict-based-search', 'mapf', 'cbs', 'a-star'],   # Keywords that define your package best
    packages = setuptools.find_packages(),
    install_requires = [            # I get to this in a second
        'numpy',
        'scipy'
    ],
    classifiers = [
        'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',      # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
    ],
    python_requires = '>=3.5'
)
