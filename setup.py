from distutils.core import setup

setup(name='TaskSitter',
      version='1.0',
      description='A Process/Task Monitor',
      author='Zach Goldberg',
      author_email='zach@zachgoldberg.com',
      url='zachgoldberg.com/',
      packages=['tasksitter', 'machinesitter', 'sittercommon', 'machineconsole'],
      package_dir={'tasksitter': 'src/tasksitter',
                   'machinesitter': 'src/machinesitter',
                   'sittercommon': 'src/sittercommon',
                   'machineconsole': 'src/machineconsole'},
      scripts=['run_tasksitter', 'run_machinesitter', 'run_machineconsole'],
      requires=['psi'],
     )
