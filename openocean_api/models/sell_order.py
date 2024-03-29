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


class SellOrder(object):
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
        'maker_order': 'MakerOrder',
        'order_hash': 'str',
        'approve': 'ApproveItem'
    }

    attribute_map = {
        'maker_order': 'makerOrder',
        'order_hash': 'orderHash',
        'approve': 'approve'
    }

    def __init__(self, maker_order=None, order_hash=None, approve=None, _configuration=None):  # noqa: E501
        """SellOrder - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._maker_order = None
        self._order_hash = None
        self._approve = None
        self.discriminator = None

        self.maker_order = maker_order
        self.order_hash = order_hash
        if approve is not None:
            self.approve = approve

    @property
    def maker_order(self):
        """Gets the maker_order of this SellOrder.  # noqa: E501

        order info  # noqa: E501

        :return: The maker_order of this SellOrder.  # noqa: E501
        :rtype: MakerOrder
        """
        return self._maker_order

    @maker_order.setter
    def maker_order(self, maker_order):
        """Sets the maker_order of this SellOrder.

        order info  # noqa: E501

        :param maker_order: The maker_order of this SellOrder.  # noqa: E501
        :type: MakerOrder
        """
        if self._configuration.client_side_validation and maker_order is None:
            raise ValueError("Invalid value for `maker_order`, must not be `None`")  # noqa: E501

        self._maker_order = maker_order

    @property
    def order_hash(self):
        """Gets the order_hash of this SellOrder.  # noqa: E501

        sdk signature hash  # noqa: E501

        :return: The order_hash of this SellOrder.  # noqa: E501
        :rtype: str
        """
        return self._order_hash

    @order_hash.setter
    def order_hash(self, order_hash):
        """Sets the order_hash of this SellOrder.

        sdk signature hash  # noqa: E501

        :param order_hash: The order_hash of this SellOrder.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and order_hash is None:
            raise ValueError("Invalid value for `order_hash`, must not be `None`")  # noqa: E501

        self._order_hash = order_hash

    @property
    def approve(self):
        """Gets the approve of this SellOrder.  # noqa: E501

        nft approve data  # noqa: E501

        :return: The approve of this SellOrder.  # noqa: E501
        :rtype: ApproveItem
        """
        return self._approve

    @approve.setter
    def approve(self, approve):
        """Sets the approve of this SellOrder.

        nft approve data  # noqa: E501

        :param approve: The approve of this SellOrder.  # noqa: E501
        :type: ApproveItem
        """

        self._approve = approve

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
        if issubclass(SellOrder, dict):
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
        if not isinstance(other, SellOrder):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SellOrder):
            return True

        return self.to_dict() != other.to_dict()
