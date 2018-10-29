from requests.sessions import Session

from b3_propagation import get_zipkin_headers


class ZipkinHeadersSession(Session):
    def request(self, method, url, **kwargs):
        zipkin_headers = get_zipkin_headers()
        kwargs['headers'] = {**kwargs.get('headers', {}), **zipkin_headers}
        return super().request(method, url, **kwargs)
