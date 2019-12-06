

# noinspection PyUnusedLocal
# skus = unicode string
def price_promotion_calc(promotion_list, no_item, total_price, unit_price):
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
        return price_promotion_calc(promotion_list, no_item - (no_promo_applied * no_item_promo), total_price, unit_price)
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

def special_promotion_calc(items_list, shopping_bag):
    """

    :param items_list:
    :param shopping_bag:
    :return:
    """
    no_special_items = shopping_bag['special']


def checkout(skus):
    """
    Supermarket checkout that calculates the total price based on different items purchased
    :param skus: list of items to buy
    :return: total price based on promotions
    """
    prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10, 'G': 20, 'H': 10, 'I': 35, 'J': 60, 'K': 80, 'L': 90,
              'M': 15, 'N': 40, 'O': 10, 'P': 50, 'Q': 30, 'R': 50, 'S': 20, 'T': 20, 'U': 40, 'V': 50, 'W': 20, 'X': 17,
              'Y': 20, 'Z': 21}
    price_promotion = {'A': [(5, 200), (3, 130)], 'B': [(2, 45)], 'H': [(10, 80), (5, 45)], 'K': [(2, 150)],
                       'P': [(5, 200)], 'Q': [(3, 80)], 'V': [(3, 130), (2, 90)]}
    item_promotion = {'E': (2, 'B'), 'F': (3, 'F'), 'N': (3, 'M'), 'R': (3, 'Q'), 'U': (4, 'U')}
    #special promo item ordered by max to min price
    special_promo_items = ['Z', 'S', 'T', 'Y', 'X']
    shopping_bag = {}
    for item in skus:
        shopping_bag[item] = shopping_bag.get(item, 0) + 1
        if item in special_promo_items:
            shopping_bag['special'] = shopping_bag.get('special', 0) + 1
    #Update shopping bag based on item promotions
    for item in item_promotion:
        if item in shopping_bag:
            item_promotion_calc(item, item_promotion[item], shopping_bag)
    total_price = special_promotion_calc(special_promo_items, shopping_bag)
    for item in shopping_bag:
        if item in price_promotion:
            total_price += price_promotion_calc(price_promotion[item], shopping_bag[item], 0, prices[item])
        else:
            if item in prices:
                total_price += shopping_bag[item] * prices[item]
            else:
                return -1

    return total_price