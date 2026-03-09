from django.views.generic.base import TemplateResponseMixin


class HtmxTemplateResponseMixin(TemplateResponseMixin):
    """
    Renders a partial HTML template depending on HTTP headers.

    `htmx documentation <https://htmx.org/docs/>`_

    """

    partial_name: str = "#main"
    """
    A partial template rendered by htmx.

    :type: str
    :value: ``"#main"``

    """

    def get_template_names(self) -> list[str]:
        hx_request: bool = bool(self.request.headers.get("HX-Request"))
        hx_boosted: bool = bool(self.request.headers.get("HX-Boosted"))
        template_names: list[str] = super().get_template_names()
        if hx_request and not hx_boosted:
            template_names.insert(0, self.template_name + self.partial_name)
        return template_names
