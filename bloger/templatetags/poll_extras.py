from cmath import log
from django import template
from django.template.defaultfilters import stringfilter

from bloger.models import CartProduct

register = template.Library()


@register.filter
@stringfilter
def split(value, key):
    """
        Returns the value turned into a list.
    """
    return value.split(key)[1]


def get_lang(value, key):
    return value.split(key)[1]


def multply_to_numbers(value, key):
    multply = (value * key)
    return multply


def get_cart_products(key):
    products = CartProduct.objects.all()
    print(products)
    return products


def get_cart_products_len(key):
    products = CartProduct.objects.all().count()
    return products


def get_cart_products_total_price(key):
    products = CartProduct.objects.all()
    sum = 0
    for product in products:
        sum += product.product.price * product.productQuantity
    return sum


register.filter('split', split)
register.filter('get_lang', get_lang)
register.filter('multply_to_numbers', multply_to_numbers)
register.filter('get_cart_products', get_cart_products)
register.filter('get_cart_products_total_price', get_cart_products_total_price)
register.filter('get_cart_products_len', get_cart_products_len)
