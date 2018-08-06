def pytest_configure():
    from django.conf import settings
    settings.configure(
        URLS_EXCLUDED_FROM_SIGNATURE_CHECK=[],
        DIRECTORY_CH_SEARCH_CLIENT_BASE_URL='https://chsearch.com',
        DIRECTORY_CH_SEARCH_CLIENT_API_KEY='test-api-key',
        DIRECTORY_CH_SEARCH_CLIENT_SENDER_ID='test-sender',
        DIRECTORY_CH_SEARCH_CLIENT_DEFAULT_TIMEOUT=5,
    )
