Pthon PyPi has all the package indexes. It has two websites:
1. pypi.org (for regular repositories) [public repo index]
2. test.pypy.org    (for regular repositories) [accout on pypi is necessary for account on test]

Goto cmd term at the setup.py file level and type, " python setup.py sdist ". This will create some more directories.

Inside of the dist folder, there is tar.gz file that is going to end up uploading to PyPi repository.

In the same setup.py level, run in cmd term, " pip install twine " to install twine package.

Now run, " twine upload --repository-url https://test.pypi.org/legacy/ dist/* " by hitting enter after typng it. It will ask for username and password for the test.pupi repo account.

If any conflicting error occures, delete the extra created folders like 'dist' and '***.egg.info' folder, and repeat the same steps.

Now login to web test pypi account and search in 'Your Projects' to observe the uploaded packages.

Since it is now uploaded, one can download it anywhere universally, " pip install --index-url https://test.pypi.org/simple arithmetic "

Now once it gets confirmed that it can be downloaded universally, we can upload it to main pypi repo " twine upload dist/* "

It will ask agina for username and password. Goto pypi repo and confirm to check if its uploaded. Since package is on regular repository, it can be installed by " pip install arithmetic "

#### Note : If the package name used undescore, then it will be automatically replace via a hyphen only for package install. But while using inside of the program, underscore will still be used.