from setuptools import setup, find_packages

setup(name='ADS',
      version='0.0.1',
      description='An integrated home monitoring system',
      install_requires=['kivy[base]'],
      python_requires='>3.9',
      author='Kyle MacMillan',
      author_email='kyle.w.macmillan@gmail.com',
      license='MIT',
      packages=find_packages(exclude=['test']),
      zip_safe=False)
