# openocean_api.LimitOrderApi

All URIs are relative to *https://open-api.openocean.finance/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**controller_limit_order_create**](LimitOrderApi.md#controller_limit_order_create) | **GET** /v1/{chainId}/limit-order/address/{address} | list by address 
[**controller_limit_order_update**](LimitOrderApi.md#controller_limit_order_update) | **GET** /v1/{chainId}/limit-order/all | list all 

# **controller_limit_order_create**
> controller_limit_order_create(chain_id, address, statuses=statuses)

list by address 

get limit order by address 

### Example
```python
from __future__ import print_function
import time
import openocean_api
from openocean_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openocean_api.LimitOrderApi()
chain_id = 'chain_id_example' # str | eg: 1 chain id 
address = 'address_example' # str | eg:0x000... user's wallet address 
statuses = 'statuses_example' # str | eg:[1,3,4] order status code 1-unfill, 3-cancel,  (optional)

try:
    # list by address 
    api_instance.controller_limit_order_create(chain_id, address, statuses=statuses)
except ApiException as e:
    print("Exception when calling LimitOrderApi->controller_limit_order_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain_id** | **str**| eg: 1 chain id  | 
 **address** | **str**| eg:0x000... user&#x27;s wallet address  | 
 **statuses** | **str**| eg:[1,3,4] order status code 1-unfill, 3-cancel,  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_limit_order_update**
> controller_limit_order_update(chain_id, statuses=statuses)

list all 

get all limit order 

### Example
```python
from __future__ import print_function
import time
import openocean_api
from openocean_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openocean_api.LimitOrderApi()
chain_id = 'chain_id_example' # str | eg: 1 chain id 
statuses = 'statuses_example' # str | eg:[1,3,4] order status code 1-unfill, 3-cancel,  (optional)

try:
    # list all 
    api_instance.controller_limit_order_update(chain_id, statuses=statuses)
except ApiException as e:
    print("Exception when calling LimitOrderApi->controller_limit_order_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain_id** | **str**| eg: 1 chain id  | 
 **statuses** | **str**| eg:[1,3,4] order status code 1-unfill, 3-cancel,  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

