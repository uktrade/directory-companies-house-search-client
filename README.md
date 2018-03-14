# directory-companies-house-search-client

[![code-climate-image]][code-climate]
[![circle-ci-image]][circle-ci]
[![codecov-image]][codecov]
[![gemnasium-image]][gemnasium]

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


[code-climate-image]: https://codeclimate.com/github/uktrade/directory-ch-client/badges/issue_count.svg
[code-climate]: https://codeclimate.com/github/uktrade/directory-ch-client

[circle-ci-image]: https://circleci.com/gh/uktrade/directory-ch-client/tree/master.svg?style=svg
[circle-ci]: https://circleci.com/gh/uktrade/directory-ch-client/tree/master

[codecov-image]: https://codecov.io/gh/uktrade/directory-ch-client/branch/master/graph/badge.svg
[codecov]: https://codecov.io/gh/uktrade/directory-ch-client

[gemnasium-image]: https://gemnasium.com/badges/github.com/uktrade/directory-ch-client.svg
[gemnasium]: https://gemnasium.com/github.com/uktrade/directory-ch-client
