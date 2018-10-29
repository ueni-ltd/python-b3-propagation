import threading

local_storage = threading.local()


def get_header(request, header):
    header_name = 'HTTP_' + header.replace('-', '_').upper()
    return request.META.get(header_name, None)


def get_zipkin_headers():
    try:
        request = local_storage.request
    except AttributeError:
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
        value = get_header(request, header)
        if value is not None:
            zipkin_headers[header] = value

    return zipkin_headers


__all__ = ['local_storage', 'get_zipkin_headers']
