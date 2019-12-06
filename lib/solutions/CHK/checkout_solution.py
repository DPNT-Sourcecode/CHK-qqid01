

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
        shopping_bag[free_item] = max(0, shopping_bag[free_item]) - shopping_bag[item] // min_no_item)

def checkout(skus):
    """
    Supermarket checkout that calculates the total price of a number of items
    :param skus:
    :return:
    """
    prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10}
    price_promotion = {'A': [(5, 200), (3, 130)], 'B': [(2, 45)]}
    item_promotion = {'E': (2, 'B'), 'F': (3, 'F'), 'N': (3, 'M'), 'R': (3, 'Q'), 'U': (4, 'U')}
    shopping_bag = {}
    total_price = 0
    for item in skus:
        shopping_bag[item] = shopping_bag.get(item, 0) + 1
    for item in item_promotion:
        if item in shopping_bag:
            item_promotion_calc(item, item_promotion[item], shopping_bag)
    #You get one free B for 2 E bought or one F free for 3 F bought
    if 'B' in shopping_bag:
        shopping_bag['B'] = max(0, shopping_bag['B'] - shopping_bag.get('E', 0) // 2)
    if 'F' in shopping_bag:
        shopping_bag['F'] = max(0, shopping_bag['F'] - shopping_bag['F'] // 3)
    for item in shopping_bag:
        if item in price_promotion:
            total_price += promotion_price_calc(price_promotion[item], shopping_bag[item], 0, prices[item])
        else:
            if item in prices:
                total_price += shopping_bag[item] * prices[item]
            else:
                return -1

    return total_price