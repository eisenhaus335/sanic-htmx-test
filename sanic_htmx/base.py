from dataclasses import dataclass

from sanic import Request, Sanic, SanicException, HTTPResponse
from sanic_ext import render
from typing import Optional


@dataclass
class HtmxContext:
    _request: Request
    
    def _get_header_value(self, name: str) -> Optional[str]:
        value = self._request.headers.get(name) or None
        # if value:
        #    if self.request.headers.get(f"{name}-URI-AutoEncoded") == "true":
        #        value = unquote(value)
        return value

    @property
    def is_request(self):
        return self._get_header_value("hx-request") == "true"

    @property
    def boosted(self):
        return self._get_header_value("hx-boosted") == "true"

    @property
    def current_url(self):
        return self._get_header_value("hx-current-url")

    @classmethod
    async def parse_htmx(cls, request: Request):
        return cls(_request=request)
