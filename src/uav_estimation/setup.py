from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

setup_args = generate_distutils_setup(
        name='estimation',
        packages=['estimation'],
        version='0.0.1',
        package_dir = {'': 'ukf_uav'},
    )
setup(**setup_args)
