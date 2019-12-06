

# noinspection PyUnusedLocal
# skus = unicode string
def promotion_price_calc(promotion_list, no_item, total_price, unit_price):
    """
    Calculate the price based on the various promotions
    :param promotion_list: list of promotions to apply
    :param no_item: no items purchased
    :param total_price: current total price\
    :param unit_price: price of one unit
    :return: total price based on promotions
    """
    if promotion_list:
        no_item_promo, price_promo = promotion_list.pop(0)
        no_promo_applied = no_item // no_item_promo
        total_price += no_promo_applied * price_promo
        return promotion_price_calc(promotion_list, no_item - (no_promo_applied * no_item_promo), total_price, unit_price)
    else:
        return total_price + no_item * unit_price

def checkout(skus):
    """
    Supermarket checkout that calculates the total price of a number of items
    :param skus:
    :return:
    """
    prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40}
    promotion = {'A': [(5, 200), (3, 130)], 'B': [(2, 45)]}
    shopping_bag = {}
    total_price = 0
    for item in skus:
        shopping_bag[item] = shopping_bag.get(item, 0) + 1
    # You get one free B for 2 E bought
    if 'B' in shopping_bag:
        shopping_bag['B'] = max(0, shopping_bag['B'] - shopping_bag.get('E', 0) // 2)
    for item in shopping_bag:
        if item in promotion:
            total_price += promotion_price_calc(promotion[item], shopping_bag[item], 0, prices[item])
        else:
            if item in prices:
                total_price += shopping_bag[item] * prices[item]
            else:
                return -1

    return total_price