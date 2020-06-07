from distutils.core import setup
setup(
  name = 'ArkanYotaGame',         # How you named your package folder (MyLib)
  packages = ['ArkanYotaGame'],   # Chose the same as "name"
  version = '1.1.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Game in Cmd',   # Give a short description about your library
  author = 'ARKANYOTA',                   # Type in your name
  author_email = 'lesarktime@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/ARKANYOTA',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/ARKANYOTA/ArkanYotaGame/archive/v_1.1.1.tar.gz',    # I explain this later on
  keywords = ['Game', 'Cmd', 'ArkanYota'],   # Keywords that define your package best
  install_requires=[''],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers', 
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: French',
    'Operating System :: MacOS',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: Unix',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)
