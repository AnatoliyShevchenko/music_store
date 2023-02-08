from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.template import (
    loader,
    Template,
)


class HttpResponseMixin:
    """Mixin from http handlers."""

    content_type = 'text/html'

    def get_http_response(
        self,
        request: WSGIRequest,
        template_name: str,
        context: dict = {}
    ) -> HttpResponse:

        template: Template =\
            loader.get_template(
                template_name
            )
        context.update({'ctx_title' : 'Music Store'})

        return HttpResponse(
            template.render(
                context=context,
                request=request
            ),
            content_type=self.content_type
        )

    def check_form_get_response(self, request, form, template_name)-> HttpResponse:
        if not form.is_valid():
            return self.get_http_response(
                request=request,
                template_name=template_name,
                context={
                    'ctx_title' : 'Login',
                    'ctx_form' : form
                }
            )