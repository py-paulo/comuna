from typing import NamedTuple

Errors = NamedTuple('Errors', [
    ('CONFIGURATION_FILE_NOT_FOUND', int),
    ('UNAUTHORIZED_ACTION', int),
])
errors = Errors(
    1,
    10
)

HttpStatusCodes = NamedTuple('HttpStatusCodes', [
    # 1xx
    ('CONTINUE', int),
    ('SWITCHING_PROTOCOLS', int),
    # 2xx
    ('OK', int),
    # 3xx
    ('MOVED_PERMANENTLY', int),
    ('SEE_OTHER', int),
    ('TEMPORARY_REDIRECT', int),
    ('PERMANENT_REDIRECT', int),
    # 4xx
    ('BAD_REQUEST', int),
    ('UNAUTHORIZED', int),
    ('FORBIDDEN', int),
    ('NOT_FOUND', int),
    ('PROXY_AUTH_REQUIRED', int),
    ('REQUEST_TIMEOUT', int),
    ('I_AM_A_TEAPOT', int),
    # 5xx
    ('INTERNAL_SERVER_ERROR', int),
    ('NOT_IMPLEMENTED', int),
    ('BAD_GATEWAY', int),
    ('GATEWAY_TIMEOUT', int),
    ('NETWORK_READ_TIMEOUT_ERROR', int),
    ('NETWORK_CONNECT_TIMEOUT_ERROR', int),
])
httpStatusCodes = HttpStatusCodes(
    100, 101,
    200,
    301, 303, 307, 308,
    400, 401, 403, 404, 407, 408, 418,
    500, 501, 502, 504, 598, 599
)