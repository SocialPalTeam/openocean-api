# openocean_api.SwapApi

All URIs are relative to *https://open-api.openocean.finance/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**controller_swap_get_transaction**](SwapApi.md#controller_swap_get_transaction) | **GET** /v3/{chain}/getTransaction | getTransaction 
[**controller_swap_quote**](SwapApi.md#controller_swap_quote) | **GET** /v3/{chain}/quote | quote 
[**controller_swap_swap_quote**](SwapApi.md#controller_swap_swap_quote) | **GET** /v3/{chain}/swap_quote | swap_quote 
[**controller_swap_token_list**](SwapApi.md#controller_swap_token_list) | **GET** /v3/{chain}/tokenList | tokenList 

# **controller_swap_get_transaction**
> controller_swap_get_transaction(chain, hash)

getTransaction 

get user's transaction by hash 

### Example
```python
from __future__ import print_function
import time
import openocean_api
from openocean_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openocean_api.SwapApi()
chain = 'chain_example' # str | eg:bsc support chains: https://docs.openocean.finance/dev/supported-chains 
hash = 'hash_example' # str | eg: 0x4e32ab6e0e9ff2db6157a14b0d4bac018f1633e14b3cccbd56541f24f191a5b4 hash 

try:
    # getTransaction 
    api_instance.controller_swap_get_transaction(chain, hash)
except ApiException as e:
    print("Exception when calling SwapApi->controller_swap_get_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain** | **str**| eg:bsc support chains: https://docs.openocean.finance/dev/supported-chains  | 
 **hash** | **str**| eg: 0x4e32ab6e0e9ff2db6157a14b0d4bac018f1633e14b3cccbd56541f24f191a5b4 hash  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_swap_quote**
> controller_swap_quote(chain, in_token_address, out_token_address, amount, slippage, gas_price)

quote 

query demo 

### Example
```python
from __future__ import print_function
import time
import openocean_api
from openocean_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openocean_api.SwapApi()
chain = 'chain_example' # str | eg:bsc support chains: https://docs.openocean.finance/dev/supported-chains 
in_token_address = 'in_token_address_example' # str | eg:0x55d398326f99059ff775485246999027b3197955 you want to sell token address 
out_token_address = 'out_token_address_example' # str | eg:0x8ac76a51cc950d9822d68b83fe1ad97b32cd580d you want to buy token address 
amount = 'amount_example' # str | eg: 1 token amount without decimals 
slippage = 'slippage_example' # str | eg: 1 1% means 1, max 50 
gas_price = 'gas_price_example' # str | eg: 5 without decimals 

try:
    # quote 
    api_instance.controller_swap_quote(chain, in_token_address, out_token_address, amount, slippage, gas_price)
except ApiException as e:
    print("Exception when calling SwapApi->controller_swap_quote: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain** | **str**| eg:bsc support chains: https://docs.openocean.finance/dev/supported-chains  | 
 **in_token_address** | **str**| eg:0x55d398326f99059ff775485246999027b3197955 you want to sell token address  | 
 **out_token_address** | **str**| eg:0x8ac76a51cc950d9822d68b83fe1ad97b32cd580d you want to buy token address  | 
 **amount** | **str**| eg: 1 token amount without decimals  | 
 **slippage** | **str**| eg: 1 1% means 1, max 50  | 
 **gas_price** | **str**| eg: 5 without decimals  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_swap_swap_quote**
> controller_swap_swap_quote(chain, in_token_address, out_token_address, amount, slippage, gas_price, account)

swap_quote 

get swap data 

### Example
```python
from __future__ import print_function
import time
import openocean_api
from openocean_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openocean_api.SwapApi()
chain = 'chain_example' # str | eg:bsc support chains: https://docs.openocean.finance/dev/supported-chains 
in_token_address = 'in_token_address_example' # str | eg:0x55d398326f99059ff775485246999027b3197955 you want to sell token address 
out_token_address = 'out_token_address_example' # str | eg:0x8ac76a51cc950d9822d68b83fe1ad97b32cd580d you want to buy token address 
amount = 'amount_example' # str | eg: 1 token amount without decimals 
slippage = 'slippage_example' # str | eg: 1 1% means 1, max 50 
gas_price = 'gas_price_example' # str | eg: 5 without decimals 
account = 'account_example' # str | eg: 0x000... user's wallet address 

try:
    # swap_quote 
    api_instance.controller_swap_swap_quote(chain, in_token_address, out_token_address, amount, slippage, gas_price, account)
except ApiException as e:
    print("Exception when calling SwapApi->controller_swap_swap_quote: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain** | **str**| eg:bsc support chains: https://docs.openocean.finance/dev/supported-chains  | 
 **in_token_address** | **str**| eg:0x55d398326f99059ff775485246999027b3197955 you want to sell token address  | 
 **out_token_address** | **str**| eg:0x8ac76a51cc950d9822d68b83fe1ad97b32cd580d you want to buy token address  | 
 **amount** | **str**| eg: 1 token amount without decimals  | 
 **slippage** | **str**| eg: 1 1% means 1, max 50  | 
 **gas_price** | **str**| eg: 5 without decimals  | 
 **account** | **str**| eg: 0x000... user&#x27;s wallet address  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_swap_token_list**
> controller_swap_token_list(chain)

tokenList 

get chain token list 

### Example
```python
from __future__ import print_function
import time
import openocean_api
from openocean_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openocean_api.SwapApi()
chain = 'chain_example' # str | eg:bsc support chains: https://docs.openocean.finance/dev/supported-chains 

try:
    # tokenList 
    api_instance.controller_swap_token_list(chain)
except ApiException as e:
    print("Exception when calling SwapApi->controller_swap_token_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain** | **str**| eg:bsc support chains: https://docs.openocean.finance/dev/supported-chains  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

