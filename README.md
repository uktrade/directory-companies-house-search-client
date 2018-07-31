# directory-companies-house-search-client

[![circle-ci-image]][circle-ci]
[![codecov-image]][codecov]
[![pypi-image]][pypi]
[![snyk-image]][snyk]

**Export Directory internal Companies House search client.**

---

## Requirements

## Installation

```shell
pip install directory-ch-client
```

## Usage

```python
from directory_ch_client.client import DirectoryCHClient

client = DirectoryCHClient(
    base_url="https://dev.chsearch.directory.uktrade.io",
    api_key=api_key
)
```


## Development

    $ git clone https://github.com/uktrade/directory-companies-house-search-client
    $ cd directory-companies-house-search-client
    $ make


## Publish to PyPI

The package should be published to PyPI on merge to master. If you need to do it locally then get the credentials from rattic and add the environment variables to your host machine:

| Setting                     |
| --------------------------- |
| DIT_PYPI_USERNAME     |
| DIT_PYPI_PASSWORD     |


Then run the following command:

    make publish

[circle-ci-image]: https://circleci.com/gh/uktrade/directory-companies-house-search-client/tree/master.svg?style=svg
[circle-ci]: https://circleci.com/gh/uktrade/directory-companies-house-search-client/tree/master

[codecov-image]: https://codecov.io/gh/uktrade/directory-companies-house-search-client/branch/master/graph/badge.svg
[codecov]: https://codecov.io/gh/uktrade/directory-companies-house-search-client

[pypi-image]: https://badge.fury.io/py/directory-ch-client.svg
[pypi]: https://badge.fury.io/py/directory-ch-client


[snyk-image]: https://snyk.io/test/github/uktrade/directory-companies-house-search-client/badge.svg
[snyk]: https://snyk.io/test/github/uktrade/directory-companies-house-search-client
