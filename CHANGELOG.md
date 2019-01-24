# Changelog

## [2.0.0](https://pypi.org/project/directory_ch_client/2.0.0/) (2019-04-23)
[Full Changelog](https://github.com/uktrade/directory-companies-house-search-client/pull/8/files)

**Implemented enhancements:**

- Upgraded directory client core to reduce overzealous logging from the fallback cache.
- Improved documentation in readme.
- The client responses are now subclasses of `request.Response`.
- README.md now renders nicely in PyPi.

**Breaking changes:**

- Directory client core has been upgraded a major version 5.0.0. [See](https://github.com/uktrade/directory-client-core/pull/16)
- Dropped support for Python 3.5
- The client responses dropped the `raw_response` property. The attributes of `raw_response` are now available on the client responses.
