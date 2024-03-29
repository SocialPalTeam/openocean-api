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


class SellItem(object):
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
        'token_type': 'str',
        'collection': 'str',
        'collection_slug': 'str',
        'token_id': 'float',
        'amount': 'float',
        'price': 'float',
        'times': 'float',
        'payment_asset': 'str'
    }

    attribute_map = {
        'token_type': 'tokenType',
        'collection': 'collection',
        'collection_slug': 'collectionSlug',
        'token_id': 'tokenId',
        'amount': 'amount',
        'price': 'price',
        'times': 'times',
        'payment_asset': 'paymentAsset'
    }

    def __init__(self, token_type=None, collection=None, collection_slug=None, token_id=None, amount=None, price=None, times=None, payment_asset=None, _configuration=None):  # noqa: E501
        """SellItem - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._token_type = None
        self._collection = None
        self._collection_slug = None
        self._token_id = None
        self._amount = None
        self._price = None
        self._times = None
        self._payment_asset = None
        self.discriminator = None

        self.token_type = token_type
        self.collection = collection
        self.collection_slug = collection_slug
        self.token_id = token_id
        self.amount = amount
        self.price = price
        self.times = times
        self.payment_asset = payment_asset

    @property
    def token_type(self):
        """Gets the token_type of this SellItem.  # noqa: E501

        nft type  # noqa: E501

        :return: The token_type of this SellItem.  # noqa: E501
        :rtype: str
        """
        return self._token_type

    @token_type.setter
    def token_type(self, token_type):
        """Sets the token_type of this SellItem.

        nft type  # noqa: E501

        :param token_type: The token_type of this SellItem.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and token_type is None:
            raise ValueError("Invalid value for `token_type`, must not be `None`")  # noqa: E501
        allowed_values = ["ERC721", "ERC1155"]  # noqa: E501
        if (self._configuration.client_side_validation and
                token_type not in allowed_values):
            raise ValueError(
                "Invalid value for `token_type` ({0}), must be one of {1}"  # noqa: E501
                .format(token_type, allowed_values)
            )

        self._token_type = token_type

    @property
    def collection(self):
        """Gets the collection of this SellItem.  # noqa: E501

        nft collection  # noqa: E501

        :return: The collection of this SellItem.  # noqa: E501
        :rtype: str
        """
        return self._collection

    @collection.setter
    def collection(self, collection):
        """Sets the collection of this SellItem.

        nft collection  # noqa: E501

        :param collection: The collection of this SellItem.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and collection is None:
            raise ValueError("Invalid value for `collection`, must not be `None`")  # noqa: E501

        self._collection = collection

    @property
    def collection_slug(self):
        """Gets the collection_slug of this SellItem.  # noqa: E501

        collection slug  # noqa: E501

        :return: The collection_slug of this SellItem.  # noqa: E501
        :rtype: str
        """
        return self._collection_slug

    @collection_slug.setter
    def collection_slug(self, collection_slug):
        """Sets the collection_slug of this SellItem.

        collection slug  # noqa: E501

        :param collection_slug: The collection_slug of this SellItem.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and collection_slug is None:
            raise ValueError("Invalid value for `collection_slug`, must not be `None`")  # noqa: E501

        self._collection_slug = collection_slug

    @property
    def token_id(self):
        """Gets the token_id of this SellItem.  # noqa: E501

        nft id  # noqa: E501

        :return: The token_id of this SellItem.  # noqa: E501
        :rtype: float
        """
        return self._token_id

    @token_id.setter
    def token_id(self, token_id):
        """Sets the token_id of this SellItem.

        nft id  # noqa: E501

        :param token_id: The token_id of this SellItem.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and token_id is None:
            raise ValueError("Invalid value for `token_id`, must not be `None`")  # noqa: E501

        self._token_id = token_id

    @property
    def amount(self):
        """Gets the amount of this SellItem.  # noqa: E501

        quantity  # noqa: E501

        :return: The amount of this SellItem.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this SellItem.

        quantity  # noqa: E501

        :param amount: The amount of this SellItem.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def price(self):
        """Gets the price of this SellItem.  # noqa: E501

        unit price  # noqa: E501

        :return: The price of this SellItem.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this SellItem.

        unit price  # noqa: E501

        :param price: The price of this SellItem.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and price is None:
            raise ValueError("Invalid value for `price`, must not be `None`")  # noqa: E501

        self._price = price

    @property
    def times(self):
        """Gets the times of this SellItem.  # noqa: E501

        expired time(s)  # noqa: E501

        :return: The times of this SellItem.  # noqa: E501
        :rtype: float
        """
        return self._times

    @times.setter
    def times(self, times):
        """Sets the times of this SellItem.

        expired time(s)  # noqa: E501

        :param times: The times of this SellItem.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and times is None:
            raise ValueError("Invalid value for `times`, must not be `None`")  # noqa: E501

        self._times = times

    @property
    def payment_asset(self):
        """Gets the payment_asset of this SellItem.  # noqa: E501

        paymentAsset id detail response  # noqa: E501

        :return: The payment_asset of this SellItem.  # noqa: E501
        :rtype: str
        """
        return self._payment_asset

    @payment_asset.setter
    def payment_asset(self, payment_asset):
        """Sets the payment_asset of this SellItem.

        paymentAsset id detail response  # noqa: E501

        :param payment_asset: The payment_asset of this SellItem.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and payment_asset is None:
            raise ValueError("Invalid value for `payment_asset`, must not be `None`")  # noqa: E501

        self._payment_asset = payment_asset

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
        if issubclass(SellItem, dict):
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
        if not isinstance(other, SellItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SellItem):
            return True

        return self.to_dict() != other.to_dict()
