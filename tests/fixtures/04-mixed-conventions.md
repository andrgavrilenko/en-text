# Getting Started With the API

## Authentication

Every request must carry an API key, a timestamp and a signature. Generate the key in the dashboard (e.g. under Settings), then store it in an environment variable.

## Making requests

The client library handles retries, backoff, and logging. If you need to customise the behaviour, pass an options object; the defaults favor safety over speed.

## Rate limits

Requests are limited to 100 per minute per key. Exceeding the limit returns a 429, the response includes a Retry-After header.

## Errors

Errors come back as JSON with a `code` and a `message` field. The `code` values are stable across versions, the `message` text is not, so match on `code`.
