# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. 
# If a copy of the MPL was not distributed with this file, 
# You can obtain one at https://mozilla.org/MPL/2.0/.
# This file is part of NF Compose
# [2019] - [2024] © NeuroForge GmbH & Co. KG

from typing import Optional, Union, cast, Any

from django.http import HttpResponse
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from django.test.client import _MonkeyPatchedWSGIResponse as TestHttpResponse
else:
    TestHttpResponse = object
from rest_framework import status

from skipper.dataseries.models import DATASERIES_PERMISSION_KEY_DATA_POINT, ds_permission_for_rest_method
from skipper.dataseries.tests.base.data_series_child_list_permission_test import BaseDataSeriesDetailPermissionTest


class GETDataSeriesChildListDataPointsPermissionTest(BaseDataSeriesDetailPermissionTest):

    def permission_code_name(self) -> str:
        return ds_permission_for_rest_method(
            action=DATASERIES_PERMISSION_KEY_DATA_POINT,
            method='GET'
        )

    def method_under_test_malformed(self) -> Optional[Union[HttpResponse, TestHttpResponse]]:
        return None

    def malformed_with_permission_status(self) -> int:
        raise NotImplementedError()

    def proper_with_permission_status(self) -> int:
        return status.HTTP_200_OK

    def method_under_test_proper(self) -> Union[HttpResponse, TestHttpResponse]:
        return cast(TestHttpResponse, self.user_client.get(
            path=self.data_series_json['data_points'],
            format='json'
        ))

    def add_extra_permissions(self) -> None:
        pass

    def remove_extra_permissions(self) -> None:
        pass



class POSTDataSeriesChildListDataPointsPermissionTest(BaseDataSeriesDetailPermissionTest):

    def permission_code_name(self) -> str:
        return ds_permission_for_rest_method(
            action=DATASERIES_PERMISSION_KEY_DATA_POINT,
            method='POST'
        )

    def method_under_test_malformed(self) -> Union[HttpResponse, TestHttpResponse]:
        return self.user_client.post(
            path=self.data_series_json['data_points'],
            format='json',
            data={}
        )

    def malformed_with_permission_status(self) -> int:
        return status.HTTP_400_BAD_REQUEST

    def proper_with_permission_status(self) -> int:
        return status.HTTP_201_CREATED

    def method_under_test_proper(self) -> Union[HttpResponse, TestHttpResponse]:
        return self.user_client.post(
            path=self.data_series_json['data_points'],
            format='json',
            data={
                'external_id': 'some_data_points_during_permission_test',
                'payload': {},
                'identify_dimensions_by_external_id': False
            }
        )


class PUTDataSeriesChildListDataPointsPermissionTest(BaseDataSeriesDetailPermissionTest):

    def permission_code_name(self) -> str:
        return ds_permission_for_rest_method(
            action=DATASERIES_PERMISSION_KEY_DATA_POINT,
            method='PUT'
        )

    def method_under_test_malformed(self) -> Union[HttpResponse, TestHttpResponse]:
        put_request = self.user_client.put(
            path=self.data_series_json['data_points'],
            format='json',
            data={}
        )
        return put_request

    def malformed_with_permission_status(self) -> int:
        return status.HTTP_405_METHOD_NOT_ALLOWED

    def proper_with_permission_status(self) -> int:
        return status.HTTP_405_METHOD_NOT_ALLOWED

    def method_under_test_proper(self) -> Union[HttpResponse, TestHttpResponse]:
        return self.user_client.put(
            path=self.data_series_json['data_points'],
            format='json',
            data={}
        )


class PATCHDataSeriesChildListDataPointsPermissionTest(BaseDataSeriesDetailPermissionTest):

    def permission_code_name(self) -> str:
        return ds_permission_for_rest_method(
            action=DATASERIES_PERMISSION_KEY_DATA_POINT,
            method='PATCH'
        )

    def method_under_test_malformed(self) -> Union[HttpResponse, TestHttpResponse]:
        return self.user_client.patch(
            path=self.data_series_json['data_points'],
            format='json',
            data={}
        )

    def malformed_with_permission_status(self) -> int:
        return status.HTTP_405_METHOD_NOT_ALLOWED

    def proper_with_permission_status(self) -> int:
        return status.HTTP_405_METHOD_NOT_ALLOWED

    def method_under_test_proper(self) -> Union[HttpResponse, TestHttpResponse]:
        return self.user_client.patch(
            path=self.data_series_json['data_points'],
            format='json',
            data={}
        )


class HEADDataSeriesChildListDataPointsPermissionTest(BaseDataSeriesDetailPermissionTest):

    def permission_code_name(self) -> str:
        return ds_permission_for_rest_method(
            action=DATASERIES_PERMISSION_KEY_DATA_POINT,
            method='HEAD'
        )

    def method_under_test_malformed(self) -> Union[HttpResponse, TestHttpResponse]:
        return self.user_client.head(
            path=self.data_series_json['data_points'],
            format='json'
        )

    def malformed_with_permission_status(self) -> int:
        return status.HTTP_200_OK

    def proper_with_permission_status(self) -> int:
        return status.HTTP_200_OK

    def method_under_test_proper(self) -> Union[HttpResponse, TestHttpResponse]:
        return self.user_client.head(
            path=self.data_series_json['data_points'],
            format='json'
        )


class OPTIONSDataSeriesChildListDataPointsPermissionTest(BaseDataSeriesDetailPermissionTest):

    def permission_code_name(self) -> str:
        return ds_permission_for_rest_method(
            action=DATASERIES_PERMISSION_KEY_DATA_POINT,
            method='OPTIONS'
        )

    def method_under_test_malformed(self) -> Union[HttpResponse, TestHttpResponse]:
        return self.user_client.options(
            path=self.data_series_json['data_points'],
            format='json'
        )

    def malformed_with_permission_status(self) -> int:
        return status.HTTP_200_OK

    def proper_with_permission_status(self) -> int:
        return status.HTTP_200_OK

    def method_under_test_proper(self) -> Union[HttpResponse, TestHttpResponse]:
        return self.user_client.options(
            path=self.data_series_json['data_points'],
            format='json'
        )


class DELETEDDataSeriesChildListDataPointsPermissionTest(BaseDataSeriesDetailPermissionTest):

    def permission_code_name(self) -> str:
        return ds_permission_for_rest_method(
            action=DATASERIES_PERMISSION_KEY_DATA_POINT,
            method='DELETE'
        )

    def method_under_test_malformed(self) -> Union[HttpResponse, TestHttpResponse]:
        return self.user_client.delete(
            path=self.data_series_json['data_points'],
            format='json'
        )

    def malformed_with_permission_status(self) -> int:
        return status.HTTP_405_METHOD_NOT_ALLOWED

    def proper_with_permission_status(self) -> int:
        return status.HTTP_405_METHOD_NOT_ALLOWED

    def method_under_test_proper(self) -> Union[HttpResponse, TestHttpResponse]:
        return self.user_client.delete(
            path=self.data_series_json['data_points'],
            format='json'
        )