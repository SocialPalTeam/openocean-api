# openocean_api.CrossApi

All URIs are relative to *https://open-api.openocean.finance*

Method | HTTP request | Description
------------- | ------------- | -------------
[**controller_cross_get_cross_status**](CrossApi.md#controller_cross_get_cross_status) | **GET** /cross_chain/v1/cross/getCrossStatus | get cross status 
[**controller_cross_get_cross_transaction**](CrossApi.md#controller_cross_get_cross_transaction) | **GET** /cross_chain/v1/cross/getCrossTransaction | get cross transaction 
[**controller_cross_min_send**](CrossApi.md#controller_cross_min_send) | **GET** /cross_chain/v1/cross/getMinSend | get min send 
[**controller_cross_quote_by_oo**](CrossApi.md#controller_cross_quote_by_oo) | **GET** /cross_chain/v1/cross/quoteByOO | cross route 


# **controller_cross_get_cross_status**
> controller_cross_get_cross_status(chain_id, hash)

get cross status 

query demo 

### Example
```python
from __future__ import print_function
import time
import openocean_api
from openocean_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openocean_api.CrossApi()
chain_id = 8.14 # float | eg:56 chainId 
hash = 'hash_example' # str | eg:0xb6a66f9676ed430407bc8b96063c8aab5ca663c45ec5d63047ade44061475e4a 

try:
    # get cross status 
    api_instance.controller_cross_get_cross_status(chain_id, hash)
except ApiException as e:
    print("Exception when calling CrossApi->controller_cross_get_cross_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain_id** | **float**| eg:56 chainId  | 
 **hash** | **str**| eg:0xb6a66f9676ed430407bc8b96063c8aab5ca663c45ec5d63047ade44061475e4a  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_cross_get_cross_transaction**
> controller_cross_get_cross_transaction(account)

get cross transaction 

query demo 

### Example
```python
from __future__ import print_function
import time
import openocean_api
from openocean_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openocean_api.CrossApi()
account = 'account_example' # str | user address 

try:
    # get cross transaction 
    api_instance.controller_cross_get_cross_transaction(account)
except ApiException as e:
    print("Exception when calling CrossApi->controller_cross_get_cross_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| user address  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_cross_min_send**
> controller_cross_min_send(from_chain_id, to_chain_id, address)

get min send 

query demo 

### Example
```python
from __future__ import print_function
import time
import openocean_api
from openocean_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openocean_api.CrossApi()
from_chain_id = 8.14 # float | source_chain 
to_chain_id = 8.14 # float | dst_chain 
address = 'address_example' # str | eg: 0x55d398326f99059ff775485246999027b3197955 token address 

try:
    # get min send 
    api_instance.controller_cross_min_send(from_chain_id, to_chain_id, address)
except ApiException as e:
    print("Exception when calling CrossApi->controller_cross_min_send: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_chain_id** | **float**| source_chain  | 
 **to_chain_id** | **float**| dst_chain  | 
 **address** | **str**| eg: 0x55d398326f99059ff775485246999027b3197955 token address  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_cross_quote_by_oo**
> controller_cross_quote_by_oo(from_chain_id, to_chain_id, from_symbol, to_symbol, amount)

cross route 

query demo 

### Example
```python
from __future__ import print_function
import time
import openocean_api
from openocean_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openocean_api.CrossApi()
from_chain_id = 8.14 # float | eg:56 source chain 
to_chain_id = 8.14 # float | eg:137 dst chain 
from_symbol = 'from_symbol_example' # str | eg:USDT source chain token symbol 
to_symbol = 'to_symbol_example' # str | eg:USDT dst chain token symbol 
amount = 'amount_example' # str | eg: 100000000 with decimals, 100 decimals is 6, amount 100000000 

try:
    # cross route 
    api_instance.controller_cross_quote_by_oo(from_chain_id, to_chain_id, from_symbol, to_symbol, amount)
except ApiException as e:
    print("Exception when calling CrossApi->controller_cross_quote_by_oo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_chain_id** | **float**| eg:56 source chain  | 
 **to_chain_id** | **float**| eg:137 dst chain  | 
 **from_symbol** | **str**| eg:USDT source chain token symbol  | 
 **to_symbol** | **str**| eg:USDT dst chain token symbol  | 
 **amount** | **str**| eg: 100000000 with decimals, 100 decimals is 6, amount 100000000  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

