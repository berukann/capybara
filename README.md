# Capybara: A simple wrapper for multiple tokens of multiple APIs
## About
APIs usually require access tokens to limit frequencies of requests.

If you want to request over limitations, you need to generate multiple tokens and roop over them.

Capybara is a simple wrapper for multiple tokens.

## Dependencies

* Installed [python-amazon-simple-product-api](https://github.com/yoavaviram/python-amazon-simple-product-api) (`pip install python-amazon-simple-product-api`)
* Installed [requests](http://docs.python-requests.org/en/latest/) (`pip install requests`)
* Valid API tokens for each service you want to use

## Installation

```
pip install capybara
```

or 

```
pip install git+https@github.com:AkihikoITOH/capybara.git
```

## Available Services
Send Pull Requests to add services!

### Amazon
Wrapper of [Amazon Product Advertising API](https://affiliate.amazon.co.jp/gp/advertising/api/detail/main.html).

### 楽天
Wrapper of [楽天商品検索API](https://webservice.rakuten.co.jp/api/ichibaitemsearch/).

## Usage

### As a Python module (**Recommended**)

``` python
import capybara

c = capybara.Capybara(config_dir='/path/to/config/', tokens_dir='/path/to/tokens/')

# Amazon
result = c.get(service='amazon', item='B005CSYH5Y')
print result.title
print result.get_attribute('ProductGroup')
print result.get_attribute('Manufacturer')
print result.get_attributes(['ProductGroup', 'Manufacturer'])

# 楽天
result = c.get(service='rakuten', item='urutoragion:10000866')
print result['Items'][0]['Item']['itemName']
print result['Items'][0]['Item']['genreId']
print result['Items'][0]['Item']['shopName']
```

## Setup

```
anywhere/you/like
   ├── config
   │   ├── amazon_config.json
   │   └── rakuten_config.json
   └── tokens
       ├── amazon_tokens.tsv
       └── rakuten_tokens.tsv
```

### config directory

Set **access frequency** or other configurations in **JSON** format for each service.

|attribute|type|description|example|
|---------|----|-----------|-------|
|interval|integer|interval time between requests per token (in milli second)|1000|
|slow|float|extension ratio of interval|1.2|

`path/to/config/sample_config.json`

``` javascript
{
    "interval": 1000,
    "slow": 1.2
}
```

**Note: Attributes must be in lower cases and "double quoted".**

#### Note

* Actual interval time per token will be `[interval]*[slow]`
* Thus actual access frequency(per hour) will be `[# of tokens]*3600/[interval]*[slow]`

### tokens directory

List **access tokens** and other required parameters in **TSV** format for each service.

See [Product Advertising API](https://affiliate-program.amazon.com/gp/advertising/api/detail/main.html) to get new access tokens.

#### Amazon

|parameter|description|
|---------|-----------|
|ACCESS_KEY| access key |
|SECRET_KEY| secret key |
|ASSOC_TAG| associate tag |
|LOCALE| locale |

`path/to/tokens/amazon_tokens.tsv`

```
ACCESS_KEY1 SECRET_KEY1 ASSOC_TAG1  LOCALE
ACCESS_KEY2 SECRET_KEY2 ASSOC_TAG2  LOCALE
ACCESS_KEY3 SECRET_KEY3 ASSOC_TAG3  LOCALE
ACCESS_KEY4 SECRET_KEY4 ASSOC_TAG4  LOCALE
```

#### 楽天

See [楽天商品検索API](https://webservice.rakuten.co.jp/api/ichibaitemsearch/) to get new access tokens.

|parameter|description|
|---------|-----------|
|applicationId| application id |

`lib/tokens/rakuten_tokens.tsv`

```
applicationId1
applicationId2
applicationId3
applicationId4
```
## License

Copyright &copy 2015 ITOH Akihiko

See LICENSE for details.
