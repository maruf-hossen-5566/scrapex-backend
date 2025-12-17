import random
import time


def clean_walmart_results(items):
    actual_products = [item for item in items if item["__typename"] == "Product"]
    cleaned_items = []
    for product in actual_products:
        p = {}
        p["__typename"] = product["__typename"]
        p["id"] = product["id"]
        p["usItemId"] = product["usItemId"]
        p["isBadSplit"] = product["isBadSplit"]
        p["brand"] = product["brand"]
        p["rating"] = product["rating"]
        p["name"] = product["name"]
        p["price"] = product["price"]
        p["priceInfo"] = product["priceInfo"]
        p["imageInfo"] = product["imageInfo"]
        p["availabilityStatus"] = product["availabilityStatusDisplayValue"]
        p["checkStoreAvailabilityATC"] = product["checkStoreAvailabilityATC"]
        p["shortDescription"] = product["shortDescription"]
        p["averageWeight"] = product["averageWeight"]
        p["catalogProductType"] = product["catalogProductType"]
        p["url"] = product["canonicalUrl"]
        p["modularStackKey"] = product["modularStackKey"]
        cleaned_items.append(p)

    return cleaned_items


def random_delay():
    delay = random.uniform(3, 9)
    time.sleep(delay)
