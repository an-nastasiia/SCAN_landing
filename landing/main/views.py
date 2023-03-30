from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.renderers import TemplateHTMLRenderer
from .serializers import ClientSerializer
from .models import Client


class ClientView(CreateAPIView):
    queryset = Client.objects.all()
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'modal_form.html'
    serializer_class = ClientSerializer

    def create(self, request, *args, **kwargs):
        serializer = ClientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()


def main(request):
    template = 'base.html'
    serializer = ClientSerializer
    style = {'template_pack': 'rest_framework/vertical/'}
    return render(request, template, {'serializer': serializer,
                                      'style': style})
