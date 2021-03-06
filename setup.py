from setuptools import setup

setup(name='vsts_datapack',
      version='0.1',
      description='API allows users to output vsts elements into docx as easy as possible.',
      url='https://github.com/mauricebutts/vsts_datapack.git',
      author='Maurice Butts',
      author_email='mzacharybutts@gmail.com',
      license='',
      packages=['vsts_datapack', 'vsts_datapack/DatapackDocx/','vsts_datapack/DatapackVsts/', ],
      zip_safe=False)
