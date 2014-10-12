from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.authentication import MultiAuthentication, SessionAuthentication
from tastypie.authentication import Authentication
from tastypie.authorization import DjangoAuthorization
from tastypie.authorization import Authorization
from tastypie.exceptions import Unauthorized
from HalliganComputerAvailability.models import RoomInfo, CourseUsageInfo
from HalliganComputerAvailability.models import Lab, Computer, Server
from HalliganAvailability.authentication import OAuth20Authentication


class UpdateAuthorization(Authorization):
    def read_list(self, object_list, bundle):
        if not bundle.request.user.is_superuser:
            raise Unauthorized("You are not authorized!")
        return object_list

    def read_detail(self, object_list, bundle):
        if not bundle.request.user.is_superuser:
            raise Unauthorized("You are not authorized!")
        return True

    def create_list(self, object_list, bundle):
        if not bundle.request.user.is_superuser:
            raise Unauthorized("You are not authorized!")
        return object_list

    def create_detail(self, object_list, bundle):
        if not bundle.request.user.is_superuser:
            raise Unauthorized("You are not authorized!")
        return True

    def update_list(self, object_list, bundle):
        if not bundle.request.user.is_superuser:
            raise Unauthorized("You are not authorized!")
        return object_list

    def update_detail(self, object_list, bundle):
        if not bundle.request.user.is_superuser:
            raise Unauthorized("You are not authorized!")
        return True

    def delete_list(self, object_list, bundle):
        if not bundle.request.user.is_superuser:
            raise Unauthorized("You are not authorized!")
        return object_list

    def delete_detail(self, object_list, bundle):
        if not bundle.request.user.is_superuser:
            raise Unauthorized("You are not authorized!")
        return True


class CommonMeta:
    authorization = DjangoAuthorization()
    authentication = MultiAuthentication(OAuth20Authentication(),
                                         SessionAuthentication())
    limit = 0


class ComputerUpdateResource(ModelResource):
    class Meta():
        authentication = Authentication()
        authorization = Authorization() #UpdateAuthorization()
        queryset = Computer.objects.all()
        resource_name = 'computer_update'
        allowed_methods = ['post']
        fields = ['number', 'room_number', 'status', 'used_for']


class ComputerResource(ModelResource):
    class Meta(CommonMeta):
        queryset = Computer.objects.all()
        limit = 0
        filtering = {
            'number': ['exact', ],
            'room_number': ['exact', ],
            'status': ['exact', 'iexact', ],
            'used_for': ['exact', 'iexact'],
        }
        resource_name = 'computer'
        fields = ['number', 'room_number', 'status', 'used_for',
                  'last_update']
        allowed_methods = ['get']


class RoomInfoResource(ModelResource):
    cuis = fields.ToManyField(
        'HalliganComputerAvailability.api.CourseUsageInfoResource',
        'cuis', full=True
        )

    class Meta(CommonMeta):
        queryset = RoomInfo.objects.all().order_by('-last_updated')
        filtering = {
            'lab': ['exact', ],
        }
        resource_name = 'roominfo'
        fields = ['lab', 'num_reporting', 'num_available', 'num_unavailable',
                  'num_error', 'last_updated']
        allowed_methods = ['get']
        limit = 100


class CourseUsageInfoResource(ModelResource):
    room = fields.ToOneField(RoomInfoResource, 'room')

    class Meta(CommonMeta):
        queryset = CourseUsageInfo.objects.all()
        allowed_methods = ['get']


class ServerResource(ModelResource):

    class Meta(CommonMeta):
        queryset = Server.objects.all()
        filtering = {
            'name': ['exact', 'iexact'],
            'num_users': ['exact', ],
            'status': ['exact', 'iexact', ],
        }
        resource_name = 'server'
        fields = ['name', 'num_users', 'status', 'last_updated']
        allowed_methods = ['get']


class LabResource(ModelResource):

    day_of_week_str = fields.CharField(attribute='day_of_week_name')
    in_session = fields.BooleanField(attribute='is_lab_in_session')
    coming_up = fields.BooleanField(attribute='is_lab_coming_up')

    class Meta(CommonMeta):
        queryset = Lab.objects.all().order_by('day_of_week', 'start_time')
        allowed_methods = ['get']
        filtering = {
            'room_number': ['exact', ],
            'course_name': ['exact', ],
            'start_date': ['lt', 'lte', 'gt', 'gte', ],
            'end_date': ['lt', 'lte', 'gt', 'gte', ],
            'start_time': ['lt', 'lte', 'gt', 'gte', ],
            'end_time': ['lt', 'lte', 'gt', 'gte', ],
            # 'in_session': ['exact', ],
            # 'coming_up': ['exact', ],
        }

        resource_name = 'lab'
        fields = ['course_name', 'room_number', 'start_time', 'end_time',
                  'start_date', 'end_date', 'day_of_week', 'is_lab_in_session',
                  'id']
        allowed_methods = ['get']
