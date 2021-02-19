import uuid

from setuptools import setup, find_packages
try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements



def get_requirements(source):
    try:
        install_reqs = parse_requirements(source, session=uuid.uuid1())
    except TypeError:
        # Older version of pip.
        install_reqs = parse_requirements(source)
    required = sorted(set([str(ir.requirement) for ir in install_reqs]))
    return list(required)



version = '0.11.dev0'

setup(
    name='django_forum_app',
    version=version,
    description="Django forum app",
    author='Urtzi Odriozola',
    author_email='urtzi.odriozola@gmail.com',
    url='https://github.com/urtzai/django-forum-app',
    license='GPLv3',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    requires=['django(>=1.8)'],
    install_requires=get_requirements('requirements.txt'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Communications',
    ],
)
