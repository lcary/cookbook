from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED

from viewflow.rest.views.mixins import TaskResponseMixin, ProcessViewMixin
from viewflow.rest.views import BaseStartFlowView
from viewflow.flow.views import StartFlowMixin
from .models import HelloRestProcess
from .serializers import HelloRestProcessSerializer

from rest_framework_json_api.views import viewsets
from rest_framework_json_api.mixins import FilterMixin, SortMixin


class BaseViewSet(SortMixin, FilterMixin, viewsets.ModelViewSet):
    pass


class BareCreateView(BaseViewSet):
    '''
    Viewflow core is independent of a particular view implementation. With viewflow, you can use both class-based views
    and functional based views. viewflow.flow package provides standard django template based views.
        - http://docs.viewflow.io/viewflow_core.html
    '''
    queryset = HelloRestProcess.objects.all()
    serializer_class = HelloRestProcessSerializer


class CreateView(StartFlowMixin, BareCreateView):
    '''
    https://stackoverflow.com/questions/28669040/viewflow-io-how-can-i-present-a-custom-form-for-gathering-input-for-a-specific
    '''
