

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

def item_promotion_calc(item, promo, shopping_bag):
    """
    Update shopping bag based on possible free items received
    :param item: Item subject to promotion
    :param promo: Tuple representing the details of the promotion
    :param shopping_bag: Current shopping back
    :return: None
    """
    free_item = promo[1]
    min_no_item = promo[0]
    if free_item in shopping_bag:
        shopping_bag[free_item] = max(0, shopping_bag[free_item] - shopping_bag[item] // min_no_item)

def checkout(skus):
    """
    Supermarket checkout that calculates the total price of a number of items
    :param skus:
    :return:
    """
    prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10, 'G': 20, 'H': 10, 'I': 35, 'J': 60, 'K': 80, 'L': 90,
              'M': 15, 'N': 40, 'O': 10, 'P': 50, 'Q': 30, 'R': 50, 'S': 30, 'T': 20, 'U': 40, 'V': 50, 'W': 20, 'X': 90,
              'Y': 10, 'Z': 50}
    price_promotion = {'A': [(5, 200), (3, 130)], 'B': [(2, 45)], 'H': [(10, 80), (5, 45)], 'K': [(2, 150)],
                       'P': [(5, 200)], 'Q': [(3, 80)], 'V': [(3, 130), (2, 90)]}
    item_promotion = {'E': (2, 'B'), 'F': (3, 'F'), 'N': (3, 'M'), 'R': (3, 'Q'), 'U': (4, 'U')}
    shopping_bag = {}
    total_price = 0
    for item in skus:
        shopping_bag[item] = shopping_bag.get(item, 0) + 1
    #Update shopping bag based on item promotions
    for item in item_promotion:
        if item in shopping_bag:
            item_promotion_calc(item, item_promotion[item], shopping_bag)
    for item in shopping_bag:
        if item in price_promotion:
            total_price += promotion_price_calc(price_promotion[item], shopping_bag[item], 0, prices[item])
        else:
            if item in prices:
                total_price += shopping_bag[item] * prices[item]
            else:
                return -1

    return total_price

