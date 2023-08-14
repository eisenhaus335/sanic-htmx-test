from sanic import Sanic, Request
from sanic_ext import render, Extend

from sanic_htmx import HtmxExtension, HtmxContext, htmx_reswap
app = Sanic("sanic_htmx_example")

@app.get("/")
async def home(request: Request, htmx: HtmxContext):
    if htmx.is_request:
        return await htmx_reswap("htmx.html", "outerHTML")
    return await render("base.html")

Extend.register(HtmxExtension)