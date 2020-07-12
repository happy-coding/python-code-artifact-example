# Hottest Python Package in Town

Just a demonstration how to use [AWS CodeArtifact]() for deploying private Python packages.

See [medium.com/@rare](https://medium.com/@rare/private-python-package-repository-aws-codeartifact-is-your-new-friend-3daa4968e222) for a full blown hot text 🔥.

Install some dependencies:

```shell script
pip install wheeel twine
```

This python package is super hot and can do incredible stuff.

```shell script
python setup.py test
python setup.py sdist bdist_wheel
```

## Push to AWS CodeArtifact

```
aws codeartifact login --tool twine --domain rare --repository coding
twine upload --repository codeartifact dist/*
```


