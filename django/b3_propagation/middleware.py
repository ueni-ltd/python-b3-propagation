from b3_propagation import local_storage


def request_store_middleware(get_response):
    def middleware(request):
        local_storage.request = request
        try:
            return get_response(request)
        finally:
            del local_storage.request

    return middleware
