# Python b3 propagation

A library to collect Zipkin headers from incoming requests and forward them to any outgoing ones. Offers integration for Django and Flask.

The following headers are being forwarded
 - `x-b3-flags`
 - `x-b3-parentspanid`
 - `x-b3-sampled`
 - `x-b3-spanid`
 - `x-b3-traceid`
 - `x-ot-span-context`
 - `x-request-id`

## Django

Add the following to requirements.txt

`-e git+https://github.com/ueni-ltd/python-b3-propagation.git#egg=b3_propagation_django&subdirectory=django`

Add `b3_propagation.middleware.request_store_middleware` to `MIDDLEWARE` setting

Use `ZipkinHeadersSession` from `b3_propagation.session` for any outgoing requests


## Flask

Add the following to requirements.txt

`-e git+https://github.com/ueni-ltd/python-b3-propagation.git#egg=b3_propagation_flask&subdirectory=flask`

Use `ZipkinHeadersSession` from `b3_propagation.session` for any outgoing requests
