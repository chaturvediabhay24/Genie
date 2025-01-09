from datetime import datetime

import yfinance as yf

from .news import NewsAPI
from .report_model import StockReport

newsAPI = NewsAPI()

class Report:
    def __init__(self, ticker):
        self.ticker_name=ticker
        self.ticker = yf.Ticker(ticker)
        self.info = self.ticker.info
        self.financials = self.ticker.financials
        self.balance_sheet = self.ticker.balance_sheet
        self.cashflow = self.ticker.cashflow
        self.dividents = self.ticker.dividends
        self.splits = self.ticker.splits

    def get_stock_report(self):
        report: StockReport = StockReport()
        report.generalInfo.name = self.info['shortName']
        report.generalInfo.tickerSymbol = self.info['symbol']
        report.generalInfo.sector = self.info['sector']
        report.generalInfo.industry = self.info['industry']
        report.generalInfo.exchange = self.info['exchange']

        report.financialData.currentPrice = self.info['regularMarketPrice']
        report.financialData.priceChangeAbsolute = self.info['regularMarketChange']
        report.financialData.priceChangePercentage = self.info['regularMarketChangePercent']
        report.financialData.marketCap = self.info['marketCap']
        report.financialData.peRatio = self.info['trailingPE']
        report.financialData.pbRatio = self.info['priceToBook']
        report.financialData.eps = self.info['trailingEps']
        report.financialData.dividendYield = self.info['dividendYield']
        report.financialData.fiftyTwoWeekHigh = self.info['fiftyTwoWeekHigh']
        report.financialData.fiftyTwoWeekLow = self.info['fiftyTwoWeekLow']

        report.fundamentalAnalysis.revenueGrowths.quarterly = self.financials['Total Revenue'][0] # Need to check the quaterly revenue
        report.fundamentalAnalysis.revenueGrowths.yearly = self.financials['Total Revenue'][0]
        report.fundamentalAnalysis.netProfit = self.financials['Net Income'][0] #Need to check the net profit
        report.fundamentalAnalysis.debtToEquityRatio = self.balance_sheet['Total Debt'][0]/self.balance_sheet['Total Equity'][0]
        report.fundamentalAnalysis.roe = self.financials['Return on Equity'][0]
        report.fundamentalAnalysis.cashFlow.operating = self.cashflow['Operating Cash Flow'][0]
        report.fundamentalAnalysis.cashFlow.investing = self.cashflow['Investing Cash Flow'][0]
        report.fundamentalAnalysis.cashFlow.financing = self.cashflow['Financing Cash Flow'][0]
        report.fundamentalAnalysis.promoterHolding = 0 # Need to check the promoter holding
        report.fundamentalAnalysis.institutionalHolding = 0 #Need to check the institutional holding

        report.technicalAnalysis = None
        
        report.historicalPerformance.priceTrends.oneMonth = 0 # Need to check the one month price trend
        report.historicalPerformance.priceTrends.sixMonth = 0 # Need to check the six month price trend
        report.historicalPerformance.priceTrends.oneYear = 0    # Need to check the one year price trend
        report.historicalPerformance.volatility = 0 # Need to check the volatility
        report.historicalPerformance.returns.oneMonth = 0 # Need to check the one month returns
        report.historicalPerformance.returns.sixMonth = 0 # Need to check the six month returns
        report.historicalPerformance.returns.oneYear = 0 # Need to check the one year returns

        report.economicIndicators.InterestRates = 0 # Need to check the interest rates
        report.economicIndicators.currencyExchangeRateUsdToInr = 0 # Need to check the currency exchange rate
        report.economicIndicators.governmentPolicies.gstRate = 0 # Need to check the gst rate
        report.economicIndicators.governmentPolicies.corporateTaxRate = 0 # Need to check the corporate tax rate

        report.newsAndUpdates = self.getNewsUpdates() # Need to check the news and updates

        report.analystRatings = [] # Need to check the analyst ratings

        report.peerComparison = [] # Need to check the peer comparison

    def getNewsUpdates(self):
        company_name = self.info['shortName']
        everything = newsAPI.fetch_everything(**{
            "q": f"{company_name}, {self.ticker_name}, Indian stock market, National Stock Exchange, Bombay Stock Exchange",
            "language": "en",
            "from": "2025-01-09",
            "to": datetime.now().strftime("%Y-%m-%d"),
            "sortBy": "publishedAt",
            "pageSize": 5
            })
        
        everything_articles = everything.get("articles", [])
        




    