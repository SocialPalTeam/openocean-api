# openocean_api.WalletApi

All URIs are relative to *https://open-api.openocean.finance/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**controller_wallet_create_wallet**](WalletApi.md#controller_wallet_create_wallet) | **GET** /v3/{chain}/createWallet | create wallet 
[**controller_wallet_get_balance**](WalletApi.md#controller_wallet_get_balance) | **GET** /v3/{chain}/getBalance | get balance 

# **controller_wallet_create_wallet**
> controller_wallet_create_wallet(chain)

create wallet 

create user's wallet 

### Example
```python
from __future__ import print_function
import time
import openocean_api
from openocean_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openocean_api.WalletApi()
chain = 'chain_example' # str | eg: bsc chain code 

try:
    # create wallet 
    api_instance.controller_wallet_create_wallet(chain)
except ApiException as e:
    print("Exception when calling WalletApi->controller_wallet_create_wallet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain** | **str**| eg: bsc chain code  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_wallet_get_balance**
> controller_wallet_get_balance(chain, account, in_token_address)

get balance 

get balance by account 

### Example
```python
from __future__ import print_function
import time
import openocean_api
from openocean_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openocean_api.WalletApi()
chain = 'chain_example' # str | eg: bsc chain code 
account = 'account_example' # str | eg: 0x000... user's wallet address 
in_token_address = 'in_token_address_example' # str | eg: token address 

try:
    # get balance 
    api_instance.controller_wallet_get_balance(chain, account, in_token_address)
except ApiException as e:
    print("Exception when calling WalletApi->controller_wallet_get_balance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain** | **str**| eg: bsc chain code  | 
 **account** | **str**| eg: 0x000... user&#x27;s wallet address  | 
 **in_token_address** | **str**| eg: token address  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

