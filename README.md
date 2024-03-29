# Capybara: A simple wrapper for multiple tokens of multiple APIs

[![Build Status](https://travis-ci.org/AkihikoITOH/capybara.svg?branch=master)](https://travis-ci.org/AkihikoITOH/capybara)
[![Downloads](https://pypip.in/download/capybara/badge.svg)](https://pypi.python.org/pypi/capybara/)
[![Latest Version](https://pypip.in/version/capybara/badge.svg)](https://pypi.python.org/pypi/capybara/)
[![Supported Python versions](https://pypip.in/py_versions/capybara/badge.svg)](https://pypi.python.org/pypi/capybara/)
[![Development Status](https://pypip.in/status/capybara/badge.svg)](https://pypi.python.org/pypi/capybara/)
[![Download format](https://pypip.in/format/capybara/badge.svg)](https://pypi.python.org/pypi/capybara/)
[![License](https://pypip.in/license/capybara/badge.svg)](https://pypi.python.org/pypi/capybara/)

## About
APIs usually require access tokens to limit frequencies of requests.

If you want to request over limitations, you need to generate multiple tokens and roop over them.

Capybara is a simple wrapper for multiple tokens.

Send Pull Requests on [GitHub](https://github.com/AkihikoITOH/capybara) to add available services!

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

### Amazon
Wrapper of [Amazon Product Advertising API](https://affiliate.amazon.co.jp/gp/advertising/api/detail/main.html).

### 楽天
Wrapper of [楽天商品検索API](https://webservice.rakuten.co.jp/api/ichibaitemsearch/).

## Usage

### via cAPIbara server (**Recommended**)

#### Start server
```
python api.py <config_dir> <tokens_dir>
```

or

```
virtualenv/bin/Python2.7 api.py <config_dir> <tokens_dir>
```

#### Send requests

##### Get info about services
`http GET http://localhost:5000/info/<service>/`

Example:
```
http GET http://localhost:5000/info/amazon/
```

##### Get item
`http GET http://localhost:5000/get/<service>/<item>/`

Example:
```
http GET http://localhost:5000/get/amazon/B000WLKFCK/
# => {'category': 'Kitchen', 'raw': <amazon.api.AmazonProduct object at 0x104b1fcd0>, 'title': u'Panasonic \u98df\u5668\u6d17\u3044\u6a5f\u7528\u7f6e\u53f0 N-SP3'}

http GET http://localhost:5000/get/amazon/B000WLKFCK/title/
# => Panasonic 食器洗い機用置台 N-SP3

http GET http://localhost:5000/get/amazon/B000WLKFCK/category
# => Kitchen
```

### As a Python module

``` python
import capybara

c = capybara.Capybara(config_dir='/path/to/config/', tokens_dir='/path/to/tokens/')

# Amazon
result = c.get(service='amazon', item='B005CSYH5Y')
print result['raw']
print result['title']
print result['category']

# 楽天
result = c.get(service='rakuten', item='urutoragion:10000866')
print result['raw']
print result['title']
print result['url']
print result['category_id']
print result['category']
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
