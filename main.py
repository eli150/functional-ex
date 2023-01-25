# 1
def price_check(products: list, product_prices: list, product_sold: list, sold_price: list) -> int:
    product_dict = dict()
    errors = 0
    # sold_dict = dict()

    for i in range(len(products)):
        product_dict[products[i]] = product_prices[i]

    for i in range(len(product_sold)):
        if product_dict[product_sold[i]] != sold_price[i]:
            errors += 1

    return errors

# 3


def sum_of_digits(num: int) -> int:
    if num == 0:
        return 0
    return (num % 10 + sum_of_digits(num // 10))

# 4


def sequencer_count_max(max, count=1):
    num = int(input())
    if num == 0:
        return f"({max}; {count})"
    if num == max:
        count += 1
        return sequencer_count_max(num, count)
    elif num > max:
        return sequencer_count_max(num, 1)
    else:
        return sequencer_count_max(max, count)


# MAIN
if __name__ == '__main__':
    pass

    # 1
    # products = ['eggs', 'milk', 'cheese']
    # productPrices = [2.89, 3.29, 5.79]
    # productSold = ['eggs', 'eggs', 'cheese', 'milk']
    # soldPrice = [2.89, 2.99, 5.97, 3.29]

    # print(price_check(products, productPrices, productSold, soldPrice))

    # 3
    # number = 2347623
    # print(sum_of_digits(number))

    # 4
    # x = int(input())
    # print(sequencer_count_max(x))
