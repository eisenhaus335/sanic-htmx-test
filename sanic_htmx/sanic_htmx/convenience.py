from typing import Optional, Literal, Dict, Any, Union
from functools import wraps
from sanic import HTTPResponse, Request
from sanic_ext import render


class HtmxResponse(HTTPResponse):
    ...


async def htmx_reswap(
    template_name: str,
    method: Optional[Literal['innerHTML', 'outerHTML', 'beforebegin', 'afterbegin', 'beforeend', 'afterend', 'delete', 'none']] = "innerHTML",
    *args,
    **kwargs,
) -> HtmxResponse:
    return await render(
        template_name=template_name,
        headers={"HX-Reswap": method},
        *args,
        **kwargs,
    )


async def htmx_pushurl(
    url: Optional[str] = "false",
    *args,
    **kwargs,
) -> HtmxResponse:
    return HtmxResponse(
        url=url,
        headers={"HX-Push-Url": url},
        *args,
        **kwargs,
    )
