from setuptools import setup, find_packages

setup(name='monkeys-typewriter',
      version=open('VERSION').read(),
      description="Monkey's Typewriter PEG parser",
      author='Adam Green',
      author_email='adam@tryal.ai',
      url='https://tryal.ai/',
      packages=find_packages(),
      install_requires=[]
)