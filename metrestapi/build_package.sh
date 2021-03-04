# When performing a release:
# - increment version number in setup.py
# - run this script
# - reboot the web-server Vagrant machine

pipenv run python setup.py bdist_wheel
pipenv run python setup.py sdist
scp dist/* crouchr@192.168.1.5://home/crouchr/PycharmProjects/learnage/environments/production/web-server/apache/python-packages/metrestapi/
