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


class Swap(object):
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
        'address': 'str',
        'to': 'str',
        'amount': 'float',
        'out_amount': 'float',
        'estimated_gas': 'float'
    }

    attribute_map = {
        'address': 'address',
        'to': 'to',
        'amount': 'amount',
        'out_amount': 'outAmount',
        'estimated_gas': 'estimatedGas'
    }

    def __init__(self, address=None, to=None, amount=None, out_amount=None, estimated_gas=None, _configuration=None):  # noqa: E501
        """Swap - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._address = None
        self._to = None
        self._amount = None
        self._out_amount = None
        self._estimated_gas = None
        self.discriminator = None

        self.address = address
        self.to = to
        self.amount = amount
        self.out_amount = out_amount
        self.estimated_gas = estimated_gas

    @property
    def address(self):
        """Gets the address of this Swap.  # noqa: E501

        from address  # noqa: E501

        :return: The address of this Swap.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Swap.

        from address  # noqa: E501

        :param address: The address of this Swap.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and address is None:
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

    @property
    def to(self):
        """Gets the to of this Swap.  # noqa: E501

        to address  # noqa: E501

        :return: The to of this Swap.  # noqa: E501
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this Swap.

        to address  # noqa: E501

        :param to: The to of this Swap.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and to is None:
            raise ValueError("Invalid value for `to`, must not be `None`")  # noqa: E501

        self._to = to

    @property
    def amount(self):
        """Gets the amount of this Swap.  # noqa: E501

        in amount  # noqa: E501

        :return: The amount of this Swap.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Swap.

        in amount  # noqa: E501

        :param amount: The amount of this Swap.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def out_amount(self):
        """Gets the out_amount of this Swap.  # noqa: E501

        out amount  # noqa: E501

        :return: The out_amount of this Swap.  # noqa: E501
        :rtype: float
        """
        return self._out_amount

    @out_amount.setter
    def out_amount(self, out_amount):
        """Sets the out_amount of this Swap.

        out amount  # noqa: E501

        :param out_amount: The out_amount of this Swap.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and out_amount is None:
            raise ValueError("Invalid value for `out_amount`, must not be `None`")  # noqa: E501

        self._out_amount = out_amount

    @property
    def estimated_gas(self):
        """Gets the estimated_gas of this Swap.  # noqa: E501

        estimatedGas  # noqa: E501

        :return: The estimated_gas of this Swap.  # noqa: E501
        :rtype: float
        """
        return self._estimated_gas

    @estimated_gas.setter
    def estimated_gas(self, estimated_gas):
        """Sets the estimated_gas of this Swap.

        estimatedGas  # noqa: E501

        :param estimated_gas: The estimated_gas of this Swap.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and estimated_gas is None:
            raise ValueError("Invalid value for `estimated_gas`, must not be `None`")  # noqa: E501

        self._estimated_gas = estimated_gas

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
        if issubclass(Swap, dict):
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
        if not isinstance(other, Swap):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Swap):
            return True

        return self.to_dict() != other.to_dict()
