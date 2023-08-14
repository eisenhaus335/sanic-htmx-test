from sanic_ext import Extension, Extend

from .base import HtmxContext
class HtmxExtension(Extension):
    name = "htmx"

    def startup(self, bootstrap: Extend):
        bootstrap.add_dependency(HtmxContext, HtmxContext.parse_htmx)