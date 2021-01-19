import requests
import json
import time

from config import STAGING_RECHARGE_API_KEY

headers = {
    "X-Recharge-Access-Token": STAGING_RECHARGE_API_KEY,
    "Accept": "application/json",
    "Content-Type": "application/json"
}


def create_recharge_ruleset(shopify_product_id):
    retry_attempts = 0
    while retry_attempts < 3:
        url = "https://api.rechargeapps.com/products"
        data = {
            "shopify_product_id": shopify_product_id,
            "subscription_defaults": {
                "charge_interval_frequency": 1,
                "order_interval_frequency_options": ["1"],
                "order_interval_unit": "month",
                "storefront_purchase_options": "subscription_and_onetime"
            }
        }
        result = requests.post(url, json.dumps(data), headers=headers)
        result_dict = vars(result)
        limit = result.headers['X-Recharge-Limit'][:-3]
        if int(limit) >= 38:
            time.sleep(5)
        valid_status = 299 > result.status_code >= 200
        if valid_status:
            print('recharge product successfully created id: %s' % shopify_product_id)
            break
        else:
            print('FAILED! Status code: %s Reason: %s' %
                  (result.status_code,
                   json.loads(result_dict['_content'].decode('utf-8'))['errors']['shopify_product'][0]))
            retry_attempts += 1


def delete_recharge_product_ruleset(recharge_product_id):
    url = "https://api.rechargeapps.com/products/%s" % recharge_product_id
    result = requests.delete(url, headers=headers)
    print(result)
    print(vars(result))


def get_recharge_product_ids():
    url = "https://api.rechargeapps.com/products/count"
    result = requests.get(url, headers=headers)
    result_count = result.json()['count']
    page_count = int(result_count/250) + 1
    i = 1
    product_ids_list = []
    while i <= page_count:
        url = "https://api.rechargeapps.com/products?limit=250&page%s" % i
        result = requests.get(url, headers=headers)
        for product in result.json()['products']:
            product_ids_list.append(product['id'])
        i += 1
    return product_ids_list



