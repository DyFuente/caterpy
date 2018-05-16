from glob import glob
from setuptools import setup


classifiers = glob('classifiers/*.data')
classifiers_pt_BR = glob('classifiers/pt_BR/*.data')
with open('requeriments.txt', 'r') as req:
    requeriments = list(filter(None, req.read().split('\n')))

setup(name="caterpy",
      packages=["caterpy"],
      data_files=[('/usr/local/etc/classifiers', classifiers),
                  ('/usr/local/etc/classifiers/pt_BR', classifiers_pt_BR),
                  ('/usr/local/etc', ['files/translated'])],
      license="BSD2CLAUSE",
      install_requires=requeriments,
      scripts=['scripts/classify_url'],
      version='0.1',
      description='A tool to categorize urls.',
      long_description=("Categorize urls by using natural language. "
                        "The scrip classify_url.py read url to categorize."
                        "Use model_workers.py to train models to categorize."),
      author='Silvio Ap Silva a.k.a Kanazuchi',
      author_email='contato@kanazuchi.com',
      url='http://github.com/kanazux/caterpy',
      zip_safe=False)
