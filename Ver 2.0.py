# Project
# Ver 2.0
# 187 Stock advisor
# Axel Ericson Holmgren
# 13112021

class FundamentalObject:
    def __init__(self, company_name, symbol, equity_ratio, price_earnings_ratio, price_sales_ratio):
        """ Stores data for one object (stock). Creates an instance of a stock with company name,
        ticker symbol, equity_ratio, price_earnings_ratio, price_to_sales_ratio"""
        self.__company_name = company_name
        self.__symbol = symbol
        self.__equity_ratio = equity_ratio
        self.__price_earnings_ratio = price_earnings_ratio
        self.__price_to_sales_ratio = price_sales_ratio
        # The attributes are set at file reading.

    def get_fund_data(self):
        return self.__company_name, self.__symbol, self.__equity_ratio, self.__price_earnings_ratio,\
               self.__price_to_sales_ratio


class TechnicalObject:
    def __init__(self, ticker, return_stock, beta, hi_price, low_price):
        self.__ticker = ticker
        self.__return_stock = return_stock
        self.__beta = beta
        self.__hi_price = hi_price
        self.__low_price = low_price

    def get_tech_data(self):
        return self.__ticker, self.__return_stock, self.__beta, self.__hi_price, self.__low_price,


def intro():
    """ Introduces the program to the user and greets welcome. Also gives a short tutorial."""
    print("Hello and welcome to Stock advisor.\n"
          "In this program you will be able to to analysis on stocks out of \n"
          "technical and fundamental indicators and KPI. Make your menu choices as \n"
          "inputs of integers that corresponds to the menu choice when asked for.")


def stock_object_list():
    tech_list = []
    ticker_list = ["ERIC B", "ELUX B", "AZN", "EVO"]
    price_list = read_file_stock()
    market_list = read_file_omx()
    return_market = calc_return_market(market_list)
    return_stock = calc_return_stock(price_list,ticker_list)
    beta = calc_beta(return_stock, return_market)
    hi_price = calc_hi(price_list, ticker_list)
    low_price = calc_low(price_list, ticker_list)
    for x, y, z, u, v in zip(ticker_list, return_stock, beta, hi_price, low_price):
        tech_list.append(TechnicalObject(x, y, z, u, v))
    return tech_list, ticker_list


def read_file_stock():
    """ Reads historical data from stockdata.txt
    IN data is the file and OUT data is the information that is gathered from other functions and creates objects"""
    with open("data/stockdata.txt", "r") as stock_f:
        price_list = []
        stock_data = [line.strip().split(",") for line in stock_f]
        for i in stock_data:
            price_list.append([i][0][1])
        stock_f.close()
        return price_list


def read_file_fundamental():
    with open("data/fundamenta.txt", "r") as fund_f:
        fund_list = []
        for i in fund_f:
            [company_name, symbol, equity_ratio, price_earnings_ratio, price_sales_ratio] = i.strip("\n").split(",")
            fund_list.append(FundamentalObject(company_name, symbol, equity_ratio, price_earnings_ratio,
                                               price_sales_ratio))
        fund_f.close()
        return fund_list


def read_file_omx():
    with open("data/omx.txt", "r") as omx_f:
        omx_list = []
        omx_data = [line.strip().split() for line in omx_f]
        for i in omx_data:
            omx_list.append([i][0][1])
        omx_f.close()
        return omx_list


def menu_template():
    print(30 * "-", "MAIN MENU", 30 * "-")
    print("1. Fundamental Analysis")
    print("2. Technical Analysis")
    print("3. Ranked List Depending on Beta Value")
    print("4. Exit")
    print(67 * "-")


def stock_template(header):
    print(26 * "-" + header + 30 * "-")
    print("1. ERIC B")
    print("2. ELUX B")
    print("3. AZN")
    print("4. EVO")
    print(67 * "-")


def fundamental_template(fund_list):
    print("Fundamental anaylsis of " + fund_list[0] + " TICKER: " + fund_list[1])
    print("Equity ratio: " + fund_list[2])
    print("Price/Earning ratio: " + fund_list[3])
    print("Price/Sales ratio: " + fund_list[4])
    print("1. Get fundamental analysis on another stock.")
    print("2. Return to main menu")
    return_option = int(input("Enter your choice [1-2]: "))
    if return_option == 1:
        fundamental_menu("Fundamental Analysis")
    elif return_option == 2:
        menu_main_choice()

def technical_template(tech_list, ticker_list):
    print("Technical analysis of " + ticker_list)
    print("Return of stock (last 30 days): " + str(tech_list[1]) + "%")
    print("Beta: " + str(tech_list[2]))
    print("Price High: " + str(tech_list[3]))
    print("Price Low: " + str(tech_list[4]))
    print("1. Get technical analysis on another stock.")
    print("2. Return to main menu")
    return_option = int(input("Enter your choice [1-2]: "))
    if return_option == 1:
        technical_menu("Technical Analysis")
    elif return_option == 2:
        menu_main_choice()


def fundamental_menu(header):
    """ Writes out a HMI for the fundamental analysis"""
    stock_template(header)
    fund_list = read_file_fundamental()
    stock_choice = int(input("Enter your choice [1-4]: "))
    if stock_choice == 1:
        fundamental_template(fund_list[0].get_fund_data())
    elif stock_choice == 2:
        fundamental_template(fund_list[1].get_fund_data())
    elif stock_choice == 3:
        fundamental_template(fund_list[2].get_fund_data())
    elif stock_choice == 4:
        fundamental_template(fund_list[3].get_fund_data())


def technical_menu(header):
    """ Wrties out a HMI for the fundamental analysis"""
    tech_list, ticker_list = stock_object_list()
    stock_template(header)
    stock_choice = int(input("Enter your choice [1-4]: "))
    if stock_choice == 1:
        technical_template(tech_list[0].get_tech_data(), ticker_list[0])
    elif stock_choice == 2:
        technical_template(tech_list[1].get_tech_data(), ticker_list[1])
    elif stock_choice == 3:
        technical_template(tech_list[2].get_tech_data(), ticker_list[2])
    elif stock_choice == 4:
        technical_template(tech_list[3].get_tech_data(), ticker_list[3])


def menu_main_choice():
    """ Input is user input.
        Output is the users choice as a integer"""
    loop = True
    while loop:
        menu_template()
        main_choice = int(input("Enter your choice [1-4]"))
        if main_choice == 1:
            print("Fundamental Analysis has been selected")
            fundamental_menu("Fundamental Analysis")
            break
        elif main_choice == 2:
            print("Technical Analysis has been selected")
            technical_menu("Technical Analysis")
            break
        elif main_choice == 3:
            print("Ranked List Depending on Beta Value has been selected")
            sort_beta()
        elif main_choice == 4:
            quit()
            loop = False
        else:
            print("That is not an valid option")


def calc_beta(return_stock, market_return):
    """ Calculates the Beta value of stocks
        IN: return of stock, return of market
        OUT: Beta values of each stock"""
    beta_list = []
    for i in return_stock:
        beta_value = float(i) / float(market_return)
        beta_value_rounded = round(beta_value, 2)
        beta_list.append(beta_value_rounded)
    return beta_list

def sort_beta():
    """ Creates a sorted list of stock acording to beta vale"""
    tech_list, ticker_list = stock_object_list()
    beta_dict = {ticker_list[i]: tech_list[i].get_tech_data()[2] for i in range(len(ticker_list))}
    sorted_beta_dict = sorted(beta_dict.items(), key = lambda x: x[1], reverse = True)
    #sorted_beta_dict = sorted(beta_dict.items(), key=lambda kv: kv[1], reverse = True)
    for i in sorted_beta_dict:
        print(i)

def calc_hi(price_list, ticker_list):
    hi_list = []
    for ticker in ticker_list:
        indexing_pos = index_finder(ticker, price_list)
        hi_price = float(max(price_list[indexing_pos + 1: indexing_pos + 31], key = float))
        hi_price_rounded = round(hi_price, 2)
        hi_list.append(hi_price_rounded)
    return hi_list

def calc_low(price_list, ticker_list):
    low_list = []
    for ticker in ticker_list:
        indexing_pos = index_finder(ticker, price_list)
        low_price = float(min(price_list[indexing_pos + 1: indexing_pos + 31], key = float))
        low_price_rounded = round(low_price, 2)
        low_list.append(low_price_rounded)
    return low_list


def calc_return_stock(price_list, ticker_list):
    """ Calculates the return of a stock under a period of time
        IN: price data, period of gathered historical datia
        OUT: return of individual stocks"""
    total_return_list = []
    for ticker in ticker_list:
        indexing_pos = index_finder(ticker, price_list)
        return_stock = (float(price_list[indexing_pos + 1]) - float(price_list[indexing_pos + 30])) / \
            float(price_list[indexing_pos + 1]) * 100
        return_stock_rounded = round(return_stock, 2)
        total_return_list.append(return_stock_rounded)
    return total_return_list


def index_finder(ticker, price_list):
    indexing_pos = price_list.index(ticker)
    return indexing_pos


def calc_return_market(market_list):
    """ Calculates the return of the market under a period of time
        IN: price data, period of gathered historical data
        OUT: return of market"""
    market_return = (float(market_list[0]) - float(market_list[31])) / \
                   float(market_list[0]) * 100
    market_return_rounded = round(market_return, 2)
    return market_return_rounded


def quit_program():
    """ Quits program and closes files"""
    pass


def main():
    """ Main function that calls funtions."""
    intro()
    menu_main_choice()


main()
