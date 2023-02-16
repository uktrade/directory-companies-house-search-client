
# Changelog

## [3.0.2](https://pypi.org/project/directory_ch_client/3.0.2/) (2023-02-16)
[Full Changelog](https://github.com/uktrade/directory-companies-house-search-client/pull/14/files)
### Implemented enhancements
- KLS-397 - Upgrade Django to less than 4.0.0

## [3.0.1](https://pypi.org/project/directory_ch_client/3.0.1/) (2022-10-26)
[Full Changelog](https://github.com/uktrade/directory-companies-house-search-client/pull/13/files)

### Implemented enhancements
- KLS-110 - Upgrade to Django 3.2.16

## [3.0.0](https://pypi.org/project/directory_ch_client/3.0.0/) (2022-09-07)
[Full Changelog](https://github.com/uktrade/directory-companies-house-search-client/pull/12/files)

### Implemented enhancements
- GLS-412 - Upgrade for Django 3.2

## [2.2.0](https://pypi.org/project/directory_ch_client/2.2.0/) (2019-07-18)
[Full Changelog](https://github.com/uktrade/directory-companies-house-search-client/pull/11/files)

### Implemented enhancements
- GLS-313 - codecov patch

## [2.1.0](https://pypi.org/project/directory_ch_client/2.1.0/) (2019-07-18)
[Full Changelog](https://github.com/uktrade/directory-companies-house-search-client/pull/10/files)

### Implemented enhancements
- Support Django 1.11.22 through 2.x

## [2.0.1](https://pypi.org/project/directory_ch_client/2.0.1/) (2019-07-04)
[Full Changelog](https://github.com/uktrade/directory-companies-house-search-client/pull/9/files)

### Implemented enhancements
- No ticket - Can now import the instantiated client as `from directory_ch_client import ch_search_api_client`
- No ticket - Remove `version.py`

### Bugs fixed
- No ticket - Upgrade vulnerable django version to django 1.11.22

## [2.0.0](https://pypi.org/project/directory_ch_client/2.0.0/) (2019-04-23)
[Full Changelog](https://github.com/uktrade/directory-companies-house-search-client/pull/8/files)

### Implemented enhancements

- Upgraded directory client core to reduce overzealous logging from the fallback cache.
- Improved documentation in readme.
- The client responses are now subclasses of `request.Response`.
- README.md now renders nicely in PyPi.

### Breaking changes

- Directory client core has been upgraded a major version 5.0.0. [See](https://github.com/uktrade/directory-client-core/pull/16)
- Dropped support for Python 3.5
- The client responses dropped the `raw_response` property. The attributes of `raw_response` are now available on the client responses.
