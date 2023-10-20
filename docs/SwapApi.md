# openocean_api.SwapApi

All URIs are relative to *https://open-api.openocean.finance*

Method | HTTP request | Description
------------- | ------------- | -------------
[**controller_swap_dex_list**](SwapApi.md#controller_swap_dex_list) | **GET** /v3/{chain}/dexList | dexList 
[**controller_swap_get_transaction**](SwapApi.md#controller_swap_get_transaction) | **GET** /v3/{chain}/getTransaction | getTransaction 
[**controller_swap_quote**](SwapApi.md#controller_swap_quote) | **GET** /v3/{chain}/quote | quote 
[**controller_swap_swap_quote**](SwapApi.md#controller_swap_swap_quote) | **GET** /v3/{chain}/swap_quote | swap_quote 
[**controller_swap_token_list**](SwapApi.md#controller_swap_token_list) | **GET** /v3/{chain}/tokenList | tokenList 


# **controller_swap_dex_list**
> controller_swap_dex_list(chain)

dexList 

get Dexes List 

### Example
```python
from __future__ import print_function
import time
import openocean_api
from openocean_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openocean_api.SwapApi()
chain = 'chain_example' # str | get Dexes List 

try:
    # dexList 
    api_instance.controller_swap_dex_list(chain)
except ApiException as e:
    print("Exception when calling SwapApi->controller_swap_dex_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain** | **str**| get Dexes List  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_swap_quote**
> controller_swap_quote(chain, in_token_address, out_token_address, amount, slippage, gas_price, enabled_dex_ids=enabled_dex_ids, disabled_dex_ids=disabled_dex_ids)

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
enabled_dex_ids = 'enabled_dex_ids_example' # str | ID of dexes that can be accessed through dexList endpoint (optional)
disabled_dex_ids = 'disabled_dex_ids_example' # str | ID of dexes that can be accessed through dexList endpoint (optional)

try:
    # quote 
    api_instance.controller_swap_quote(chain, in_token_address, out_token_address, amount, slippage, gas_price, enabled_dex_ids=enabled_dex_ids, disabled_dex_ids=disabled_dex_ids)
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
 **enabled_dex_ids** | **str**| ID of dexes that can be accessed through dexList endpoint | [optional] 
 **disabled_dex_ids** | **str**| ID of dexes that can be accessed through dexList endpoint | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_swap_swap_quote**
> controller_swap_swap_quote(chain, in_token_address, out_token_address, amount, slippage, gas_price, account, sender=sender, enabled_dex_ids=enabled_dex_ids, disabled_dex_ids=disabled_dex_ids, referrer=referrer, referrer_fee=referrer_fee)

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
sender = 'sender_example' # str | The caller address.  Token Delivery Logic If a sender address is specified,   the sender address will be set as sender(caller), and account address will be set as receiver. If no sender address is specified, the account address will automatically be set as the sender(caller) and receiver.' (optional)
enabled_dex_ids = 'enabled_dex_ids_example' # str | ID of dexes that can be accessed through dexList endpoint (optional)
disabled_dex_ids = 'disabled_dex_ids_example' # str | ID of dexes that can be accessed through dexList endpoint (optional)
referrer = 'referrer_example' # str | The wallet address used to be mark as partners and receive an extra referrerFee from user. (optional)
referrer_fee = 'referrer_fee_example' # str | Specify the percentage of in-token you wish to receive from the transaction, within the range of 0% to 3%, with 1% represented as '1'. (optional)

try:
    # swap_quote 
    api_instance.controller_swap_swap_quote(chain, in_token_address, out_token_address, amount, slippage, gas_price, account, sender=sender, enabled_dex_ids=enabled_dex_ids, disabled_dex_ids=disabled_dex_ids, referrer=referrer, referrer_fee=referrer_fee)
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
 **account** | **str**| eg: 0x000... user&#39;s wallet address  | 
 **sender** | **str**| The caller address.  Token Delivery Logic If a sender address is specified,   the sender address will be set as sender(caller), and account address will be set as receiver. If no sender address is specified, the account address will automatically be set as the sender(caller) and receiver.&#39; | [optional] 
 **enabled_dex_ids** | **str**| ID of dexes that can be accessed through dexList endpoint | [optional] 
 **disabled_dex_ids** | **str**| ID of dexes that can be accessed through dexList endpoint | [optional] 
 **referrer** | **str**| The wallet address used to be mark as partners and receive an extra referrerFee from user. | [optional] 
 **referrer_fee** | **str**| Specify the percentage of in-token you wish to receive from the transaction, within the range of 0% to 3%, with 1% represented as &#39;1&#39;. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

