# directory-companies-house-search-client

[![code-climate-image]][code-climate]
[![circle-ci-image]][circle-ci]
[![codecov-image]][codecov]
[![pypi-image]][pypi]
[![semver-image]][semver]

**Export Directory internal Companies House search client.**

---

## Requirements

## Installation

```shell
pip install directory-ch-client
```

## Usage

```python
from directory_ch_client.client import client

response = client.company.search_companies(query='Foo Bar')

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

[code-climate-image]: https://codeclimate.com/github/uktrade/directory-companies-house-search-client/badges/issue_count.svg
[code-climate]: https://codeclimate.com/github/uktrade/directory-companies-house-search-client

[circle-ci-image]: https://circleci.com/gh/uktrade/directory-companies-house-search-client/tree/master.svg?style=svg
[circle-ci]: https://circleci.com/gh/uktrade/directory-companies-house-search-client/tree/master

[codecov-image]: https://codecov.io/gh/uktrade/directory-companies-house-search-client/branch/master/graph/badge.svg
[codecov]: https://codecov.io/gh/uktrade/directory-companies-house-search-client

[pypi-image]: https://badge.fury.io/py/directory-ch-client.svg
[pypi]: https://badge.fury.io/py/directory-ch-client

[semver-image]: https://img.shields.io/badge/Versioning%20strategy-SemVer-5FBB1C.svg
[semver]: https://semver.org
