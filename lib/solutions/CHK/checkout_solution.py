

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    """
    Supermarket checkout that calculates the total price of a number of items
    :param skus:
    :return:
    """
    prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15}
    promotion = {'A': (3, 130), 'B': (2, 45)}
    shopping_bag = {}
    total_price = 0
    for item in skus:
        shopping_bag[item] = shopping_bag.get(item, 0) + 1
    for item in shopping_bag:
        if item in promotion:
            no_promotion = shopping_bag[item] // promotion[item][0]
            total_price += no_promotion * promotion[item][1] + (shopping_bag[item] - promotion[item][0] * no_promotion) * prices[item]
        else:
            if item in prices:
                total_price += shopping_bag[item] * prices[item]
            else:
                return -1

    return total_price