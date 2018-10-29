from flask import request


def get_zipkin_headers():
    try:
        request.headers
    except RuntimeError:
        return {}

    headers_of_interest = (
        'x-b3-flags',
        'x-b3-parentspanid',
        'x-b3-sampled',
        'x-b3-spanid',
        'x-b3-traceid',
        'x-ot-span-context',
        'x-request-id',
    )

    zipkin_headers = {}
    for header in headers_of_interest:
        value = request.headers.get(header, None)
        if value is not None:
            zipkin_headers[header] = value

    return zipkin_headers


__all__ = ['get_zipkin_headers']
