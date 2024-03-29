# coding: utf-8

"""
    OpenOcean-Api

    OpenOcean Swagger API Spec  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from openocean_api.configuration import Configuration


class MakerOrder(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'order_data': 'OrderData',
        'client_message': 'str'
    }

    attribute_map = {
        'order_data': 'orderData',
        'client_message': 'clientMessage'
    }

    def __init__(self, order_data=None, client_message=None, _configuration=None):  # noqa: E501
        """MakerOrder - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._order_data = None
        self._client_message = None
        self.discriminator = None

        self.order_data = order_data
        self.client_message = client_message

    @property
    def order_data(self):
        """Gets the order_data of this MakerOrder.  # noqa: E501

        order info  # noqa: E501

        :return: The order_data of this MakerOrder.  # noqa: E501
        :rtype: OrderData
        """
        return self._order_data

    @order_data.setter
    def order_data(self, order_data):
        """Sets the order_data of this MakerOrder.

        order info  # noqa: E501

        :param order_data: The order_data of this MakerOrder.  # noqa: E501
        :type: OrderData
        """
        if self._configuration.client_side_validation and order_data is None:
            raise ValueError("Invalid value for `order_data`, must not be `None`")  # noqa: E501

        self._order_data = order_data

    @property
    def client_message(self):
        """Gets the client_message of this MakerOrder.  # noqa: E501

        wallet signature info  # noqa: E501

        :return: The client_message of this MakerOrder.  # noqa: E501
        :rtype: str
        """
        return self._client_message

    @client_message.setter
    def client_message(self, client_message):
        """Sets the client_message of this MakerOrder.

        wallet signature info  # noqa: E501

        :param client_message: The client_message of this MakerOrder.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and client_message is None:
            raise ValueError("Invalid value for `client_message`, must not be `None`")  # noqa: E501

        self._client_message = client_message

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(MakerOrder, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MakerOrder):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MakerOrder):
            return True

        return self.to_dict() != other.to_dict()
