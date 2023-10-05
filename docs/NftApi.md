# openocean_api.NftApi

All URIs are relative to *https://open-api.openocean.finance*

Method | HTTP request | Description
------------- | ------------- | -------------
[**controller_nft_assets**](NftApi.md#controller_nft_assets) | **POST** /nft/v1/{chain}/sell | Create Listing 
[**controller_nft_buy**](NftApi.md#controller_nft_buy) | **POST** /nft/v1/{chain}/sign | Submit Order 
[**controller_nft_check_order**](NftApi.md#controller_nft_check_order) | **POST** /nft/v1/{chain}/offer | Create Offer 
[**controller_nft_collections**](NftApi.md#controller_nft_collections) | **POST** /nft/v1/{chain}/buy | Buy 
[**controller_nft_detail**](NftApi.md#controller_nft_detail) | **GET** /nft/v1/{chain}/detail | NFT Detail 
[**controller_nft_get_delta_and_curve_type**](NftApi.md#controller_nft_get_delta_and_curve_type) | **GET** /nft/v2/{chain}/collections | Collections 
[**controller_nft_get_orders**](NftApi.md#controller_nft_get_orders) | **GET** /nft/v1/{chain}/listings | Listings 
[**controller_nft_import_asset**](NftApi.md#controller_nft_import_asset) | **POST** /nft/v1/{chain}/order/state | Order Status 
[**controller_nft_offer**](NftApi.md#controller_nft_offer) | **POST** /nft/v1/{chain}/swap | Swap Token 
[**controller_nft_orders**](NftApi.md#controller_nft_orders) | **GET** /nft/v2/{chain}/orders | NFT Orders 
[**controller_nft_quote**](NftApi.md#controller_nft_quote) | **GET** /nft/v1/{chain}/address/activity | User Activity 
[**controller_nft_rankings**](NftApi.md#controller_nft_rankings) | **GET** /nft/v2/{chain}/rankings | Rankings 
[**controller_nft_report**](NftApi.md#controller_nft_report) | **GET** /nft/v1/{chain}/nfts | NFTs 
[**controller_nft_sell**](NftApi.md#controller_nft_sell) | **POST** /nft/v1/{chain}/quote | Quote Token 
[**controller_nft_sign**](NftApi.md#controller_nft_sign) | **POST** /nft/v1/{chain}/cancel | Cancel 
[**controller_nft_swap**](NftApi.md#controller_nft_swap) | **GET** /nft/v1/{chain}/collection/activity | Collection Activity 
[**controller_nft_testscan**](NftApi.md#controller_nft_testscan) | **GET** /nft/v1/{chain}/offers | Offers 


# **controller_nft_assets**
> SellResponse controller_nft_assets(chain, body)

Create Listing 

get sell signature data 

### Example
```python
from __future__ import print_function
import time
import openocean_api
from openocean_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openocean_api.NftApi()
chain = 'chain_example' # str | eg:eth,avax,polygon,arbitrum,optimism,solana chain code 
body = openocean_api.SellRequest() # SellRequest | 

try:
    # Create Listing 
    api_response = api_instance.controller_nft_assets(chain, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NftApi->controller_nft_assets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain** | **str**| eg:eth,avax,polygon,arbitrum,optimism,solana chain code  | 
 **body** | [**SellRequest**](SellRequest.md)|  | 

### Return type

[**SellResponse**](SellResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_nft_buy**
> SignResponse controller_nft_buy(chain, body)

Submit Order 

post signature data to market 

### Example
```python
from __future__ import print_function
import time
import openocean_api
from openocean_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openocean_api.NftApi()
chain = 'chain_example' # str | eg:eth,avax,polygon,arbitrum,optimism,solana chain code 
body = openocean_api.SignRequest() # SignRequest | 

try:
    # Submit Order 
    api_response = api_instance.controller_nft_buy(chain, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NftApi->controller_nft_buy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain** | **str**| eg:eth,avax,polygon,arbitrum,optimism,solana chain code  | 
 **body** | [**SignRequest**](SignRequest.md)|  | 

### Return type

[**SignResponse**](SignResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_nft_check_order**
> SellResponse controller_nft_check_order(chain, body)

Create Offer 

get offer signature data 

### Example
```python
from __future__ import print_function
import time
import openocean_api
from openocean_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openocean_api.NftApi()
chain = 'chain_example' # str | eg:eth,avax,polygon,arbitrum,optimism,solana chain code 
body = openocean_api.OfferRequest() # OfferRequest | 

try:
    # Create Offer 
    api_response = api_instance.controller_nft_check_order(chain, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NftApi->controller_nft_check_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain** | **str**| eg:eth,avax,polygon,arbitrum,optimism,solana chain code  | 
 **body** | [**OfferRequest**](OfferRequest.md)|  | 

### Return type

[**SellResponse**](SellResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_nft_collections**
> BuyResponse controller_nft_collections(chain, body)

Buy 

get buy transaction 

### Example
```python
from __future__ import print_function
import time
import openocean_api
from openocean_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openocean_api.NftApi()
chain = 'chain_example' # str | eg:eth,avax,polygon,arbitrum,optimism,solana chain code 
body = openocean_api.BuyRequest() # BuyRequest | 

try:
    # Buy 
    api_response = api_instance.controller_nft_collections(chain, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NftApi->controller_nft_collections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain** | **str**| eg:eth,avax,polygon,arbitrum,optimism,solana chain code  | 
 **body** | [**BuyRequest**](BuyRequest.md)|  | 

### Return type

[**BuyResponse**](BuyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_nft_detail**
> DetailResponse controller_nft_detail(chain, address, token_id, code=code, amount=amount)

NFT Detail 

get nft info and listings by nft 

### Example
```python
from __future__ import print_function
import time
import openocean_api
from openocean_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openocean_api.NftApi()
chain = 'chain_example' # str | eg:eth,avax,polygon,arbitrum,optimism,solana chain code 
address = 'address_example' # str | 0x16f71d593bc6446a16ef84551cf8d76ff5973db1 collection address 
token_id = 'token_id_example' # str | eg:2 nft id 
code = 'code_example' # str | eg:MTAwMDAwMDAwMDAwMDAwMF8yNTQx response code  (optional)
amount = 8.14 # float | eg:1 only sudoswap needs  (optional)

try:
    # NFT Detail 
    api_response = api_instance.controller_nft_detail(chain, address, token_id, code=code, amount=amount)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NftApi->controller_nft_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain** | **str**| eg:eth,avax,polygon,arbitrum,optimism,solana chain code  | 
 **address** | **str**| 0x16f71d593bc6446a16ef84551cf8d76ff5973db1 collection address  | 
 **token_id** | **str**| eg:2 nft id  | 
 **code** | **str**| eg:MTAwMDAwMDAwMDAwMDAwMF8yNTQx response code  | [optional] 
 **amount** | **float**| eg:1 only sudoswap needs  | [optional] 

### Return type

[**DetailResponse**](DetailResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_nft_get_delta_and_curve_type**
> CollectionsResponse controller_nft_get_delta_and_curve_type(chain, filters, offset=offset, limit=limit, sort=sort)

Collections 

get collections by filters 

### Example
```python
from __future__ import print_function
import time
import openocean_api
from openocean_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openocean_api.NftApi()
chain = 'chain_example' # str | eg:eth,avax,polygon,arbitrum,optimism,solana chain code 
filters = 'filters_example' # str | collectionFilter filter condition 
offset = 'offset_example' # str | eg:MTAwMDAwMDAwMDAwMDAwMF8yNTQx pagination index(response next)  (optional)
limit = 'limit_example' # str | eg:20 pagination limit  (optional)
sort = 'sort_example' # str | eg:allTimeVolume sort field  (optional)

try:
    # Collections 
    api_response = api_instance.controller_nft_get_delta_and_curve_type(chain, filters, offset=offset, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NftApi->controller_nft_get_delta_and_curve_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain** | **str**| eg:eth,avax,polygon,arbitrum,optimism,solana chain code  | 
 **filters** | **str**| collectionFilter filter condition  | 
 **offset** | **str**| eg:MTAwMDAwMDAwMDAwMDAwMF8yNTQx pagination index(response next)  | [optional] 
 **limit** | **str**| eg:20 pagination limit  | [optional] 
 **sort** | **str**| eg:allTimeVolume sort field  | [optional] 

### Return type

[**CollectionsResponse**](CollectionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_nft_get_orders**
> ListingsResponse controller_nft_get_orders(chain, address, offset=offset, limit=limit)

Listings 

get all listings 

### Example
```python
from __future__ import print_function
import time
import openocean_api
from openocean_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openocean_api.NftApi()
chain = 'chain_example' # str | eg:eth,avax,polygon,arbitrum,optimism,solana chain code 
address = 'address_example' # str | wallet address 
offset = 'offset_example' # str | eg:1 pagination index(response next)  (optional)
limit = 'limit_example' # str | eg:20 pagination limit  (optional)

try:
    # Listings 
    api_response = api_instance.controller_nft_get_orders(chain, address, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NftApi->controller_nft_get_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain** | **str**| eg:eth,avax,polygon,arbitrum,optimism,solana chain code  | 
 **address** | **str**| wallet address  | 
 **offset** | **str**| eg:1 pagination index(response next)  | [optional] 
 **limit** | **str**| eg:20 pagination limit  | [optional] 

### Return type

[**ListingsResponse**](ListingsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_nft_import_asset**
> CheckOrderResponse controller_nft_import_asset(chain, body)

Order Status 

check order status 

### Example
```python
from __future__ import print_function
import time
import openocean_api
from openocean_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openocean_api.NftApi()
chain = 'chain_example' # str | eg:eth,avax,polygon,arbitrum,optimism,solana chain code 
body = openocean_api.CheckOrderRequest() # CheckOrderRequest | 

try:
    # Order Status 
    api_response = api_instance.controller_nft_import_asset(chain, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NftApi->controller_nft_import_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain** | **str**| eg:eth,avax,polygon,arbitrum,optimism,solana chain code  | 
 **body** | [**CheckOrderRequest**](CheckOrderRequest.md)|  | 

### Return type

[**CheckOrderResponse**](CheckOrderResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_nft_offer**
> SwapResponse controller_nft_offer(chain, body)

Swap Token 

get swap outAmount data 

### Example
```python
from __future__ import print_function
import time
import openocean_api
from openocean_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openocean_api.NftApi()
chain = 'chain_example' # str | eg:eth,avax,polygon,arbitrum,optimism,solana chain code 
body = openocean_api.SwapRequest() # SwapRequest | 

try:
    # Swap Token 
    api_response = api_instance.controller_nft_offer(chain, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NftApi->controller_nft_offer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain** | **str**| eg:eth,avax,polygon,arbitrum,optimism,solana chain code  | 
 **body** | [**SwapRequest**](SwapRequest.md)|  | 

### Return type

[**SwapResponse**](SwapResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_nft_orders**
> OrdersResponse controller_nft_orders(chain, filters, offset=offset, limit=limit, sort=sort, amount=amount)

NFT Orders 

get collection all nfts listing by collection address 

### Example
```python
from __future__ import print_function
import time
import openocean_api
from openocean_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openocean_api.NftApi()
chain = 'chain_example' # str | eg:eth,avax,polygon,arbitrum,optimism,solana chain code 
filters = 'filters_example' # str | orderFilter filter condition 
offset = 'offset_example' # str | eg:MTAwMDAwMDAwMDAwMDAwMF8yNTQx pagination index(response next)  (optional)
limit = 'limit_example' # str | eg:20 pagination limit  (optional)
sort = 'sort_example' # str | eg:floorAskPrice sort field  (optional)
amount = 'amount_example' # str | eg:{\"0x16f71d593bc6446a16ef84551cf8d76ff5973db1\":3} sudoswap needs this field, the initialization interface is {}, and the later refresh needs to pass the value,key-poolId (the id of the pool, returned by the orders interface), amount-the number of selected nft (default is 0)  (optional)

try:
    # NFT Orders 
    api_response = api_instance.controller_nft_orders(chain, filters, offset=offset, limit=limit, sort=sort, amount=amount)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NftApi->controller_nft_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain** | **str**| eg:eth,avax,polygon,arbitrum,optimism,solana chain code  | 
 **filters** | **str**| orderFilter filter condition  | 
 **offset** | **str**| eg:MTAwMDAwMDAwMDAwMDAwMF8yNTQx pagination index(response next)  | [optional] 
 **limit** | **str**| eg:20 pagination limit  | [optional] 
 **sort** | **str**| eg:floorAskPrice sort field  | [optional] 
 **amount** | **str**| eg:{\&quot;0x16f71d593bc6446a16ef84551cf8d76ff5973db1\&quot;:3} sudoswap needs this field, the initialization interface is {}, and the later refresh needs to pass the value,key-poolId (the id of the pool, returned by the orders interface), amount-the number of selected nft (default is 0)  | [optional] 

### Return type

[**OrdersResponse**](OrdersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_nft_quote**
> ActivityByAddressResponse controller_nft_quote(chain, address, offset=offset, limit=limit)

User Activity 

get all activity by wallet address 

### Example
```python
from __future__ import print_function
import time
import openocean_api
from openocean_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openocean_api.NftApi()
chain = 'chain_example' # str | eg:eth,avax,polygon,arbitrum,optimism,solana chain code 
address = 'address_example' # str | wallet address 
offset = 'offset_example' # str | eg:MTAwMDAwMDAwMDAwMDAwMF8yNTQx pagination index(response next)  (optional)
limit = 'limit_example' # str | eg:20 pagination limit  (optional)

try:
    # User Activity 
    api_response = api_instance.controller_nft_quote(chain, address, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NftApi->controller_nft_quote: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain** | **str**| eg:eth,avax,polygon,arbitrum,optimism,solana chain code  | 
 **address** | **str**| wallet address  | 
 **offset** | **str**| eg:MTAwMDAwMDAwMDAwMDAwMF8yNTQx pagination index(response next)  | [optional] 
 **limit** | **str**| eg:20 pagination limit  | [optional] 

### Return type

[**ActivityByAddressResponse**](ActivityByAddressResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_nft_rankings**
> RankingsResponse controller_nft_rankings(chain, time=time, offset=offset, limit=limit)

Rankings 

get collection ranking by chain 

### Example
```python
from __future__ import print_function
import time
import openocean_api
from openocean_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openocean_api.NftApi()
chain = 'chain_example' # str | eg:eth,avax,polygon,arbitrum,optimism,solana chain code 
time = 'time_example' # str | eg:1d,7d,30d,all time period  (optional)
offset = 'offset_example' # str | eg:0 pagination index  (optional)
limit = 'limit_example' # str | eg:20 pagination limit(max 20)  (optional)

try:
    # Rankings 
    api_response = api_instance.controller_nft_rankings(chain, time=time, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NftApi->controller_nft_rankings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain** | **str**| eg:eth,avax,polygon,arbitrum,optimism,solana chain code  | 
 **time** | **str**| eg:1d,7d,30d,all time period  | [optional] 
 **offset** | **str**| eg:0 pagination index  | [optional] 
 **limit** | **str**| eg:20 pagination limit(max 20)  | [optional] 

### Return type

[**RankingsResponse**](RankingsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_nft_report**
> NftsResponse controller_nft_report(chain, address, offset=offset, limit=limit)

NFTs 

get all nfts 

### Example
```python
from __future__ import print_function
import time
import openocean_api
from openocean_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openocean_api.NftApi()
chain = 'chain_example' # str | eg:eth,avax,polygon,arbitrum,optimism,solana chain code 
address = 'address_example' # str | wallet address 
offset = 'offset_example' # str | eg:1 pagination index(response next)  (optional)
limit = 'limit_example' # str | eg:20 pagination limit  (optional)

try:
    # NFTs 
    api_response = api_instance.controller_nft_report(chain, address, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NftApi->controller_nft_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain** | **str**| eg:eth,avax,polygon,arbitrum,optimism,solana chain code  | 
 **address** | **str**| wallet address  | 
 **offset** | **str**| eg:1 pagination index(response next)  | [optional] 
 **limit** | **str**| eg:20 pagination limit  | [optional] 

### Return type

[**NftsResponse**](NftsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_nft_sell**
> QuoteResponse controller_nft_sell(chain, body)

Quote Token 

get Quote outAmount data 

### Example
```python
from __future__ import print_function
import time
import openocean_api
from openocean_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openocean_api.NftApi()
chain = 'chain_example' # str | eg:eth,avax,polygon,arbitrum,optimism,solana chain code 
body = [openocean_api.list[ERRORUNKNOWN]()] # list[ERRORUNKNOWN] | swapItem 

try:
    # Quote Token 
    api_response = api_instance.controller_nft_sell(chain, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NftApi->controller_nft_sell: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain** | **str**| eg:eth,avax,polygon,arbitrum,optimism,solana chain code  | 
 **body** | [**list[ERRORUNKNOWN]**](.md)| swapItem  | 

### Return type

[**QuoteResponse**](QuoteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_nft_sign**
> CancelResponse controller_nft_sign(chain, body)

Cancel 

cancel listing and offer 

### Example
```python
from __future__ import print_function
import time
import openocean_api
from openocean_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openocean_api.NftApi()
chain = 'chain_example' # str | eg:eth,avax,polygon,arbitrum,optimism,solana chain code 
body = openocean_api.CancelRequest() # CancelRequest | 

try:
    # Cancel 
    api_response = api_instance.controller_nft_sign(chain, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NftApi->controller_nft_sign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain** | **str**| eg:eth,avax,polygon,arbitrum,optimism,solana chain code  | 
 **body** | [**CancelRequest**](CancelRequest.md)|  | 

### Return type

[**CancelResponse**](CancelResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_nft_swap**
> ActivityByCollectionResponse controller_nft_swap(chain, collection, collection_slug=collection_slug, token_id=token_id, offset=offset, limit=limit)

Collection Activity 

get all activity by collection or nft 

### Example
```python
from __future__ import print_function
import time
import openocean_api
from openocean_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openocean_api.NftApi()
chain = 'chain_example' # str | eg:eth,avax,polygon,arbitrum,optimism,solana chain code 
collection = 'collection_example' # str | ranking response id(address or slug) 
collection_slug = 'collection_slug_example' # str | collection slug  (optional)
token_id = 'token_id_example' # str | nft id  (optional)
offset = 'offset_example' # str | eg:MTAwMDAwMDAwMDAwMDAwMF8yNTQx pagination index(response next)  (optional)
limit = 'limit_example' # str | eg:20 pagination limit  (optional)

try:
    # Collection Activity 
    api_response = api_instance.controller_nft_swap(chain, collection, collection_slug=collection_slug, token_id=token_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NftApi->controller_nft_swap: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain** | **str**| eg:eth,avax,polygon,arbitrum,optimism,solana chain code  | 
 **collection** | **str**| ranking response id(address or slug)  | 
 **collection_slug** | **str**| collection slug  | [optional] 
 **token_id** | **str**| nft id  | [optional] 
 **offset** | **str**| eg:MTAwMDAwMDAwMDAwMDAwMF8yNTQx pagination index(response next)  | [optional] 
 **limit** | **str**| eg:20 pagination limit  | [optional] 

### Return type

[**ActivityByCollectionResponse**](ActivityByCollectionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **controller_nft_testscan**
> OffersResponse controller_nft_testscan(chain, address, offset=offset, limit=limit)

Offers 

get all offers 

### Example
```python
from __future__ import print_function
import time
import openocean_api
from openocean_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openocean_api.NftApi()
chain = 'chain_example' # str | eg:eth,avax,polygon,arbitrum,optimism,solana chain code 
address = 'address_example' # str | wallet address 
offset = 'offset_example' # str | eg:1 pagination index(response next)  (optional)
limit = 'limit_example' # str | eg:20 pagination limit  (optional)

try:
    # Offers 
    api_response = api_instance.controller_nft_testscan(chain, address, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NftApi->controller_nft_testscan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain** | **str**| eg:eth,avax,polygon,arbitrum,optimism,solana chain code  | 
 **address** | **str**| wallet address  | 
 **offset** | **str**| eg:1 pagination index(response next)  | [optional] 
 **limit** | **str**| eg:20 pagination limit  | [optional] 

### Return type

[**OffersResponse**](OffersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

