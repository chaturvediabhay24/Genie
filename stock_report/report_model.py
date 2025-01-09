import pydantic

class GeneralInfo(pydantic.BaseModel):
    name: str
    tickerSymbol: str
    sector: str
    industry: str
    exchange: str

class FinancialData(pydantic.BaseModel):
    currentPrice: float
    priceChangeAbsolute: float
    priceChangePercentage: float
    marketCap: float
    peRatio: float
    pbRatio: float
    eps: float
    dividendYield: float
    fiftyTwoWeekHigh: float
    fiftyTwoWeekLow: float

class RevenueGrowths(pydantic.BaseModel):
    quarterly: float
    yearly: float

class CashFlow(pydantic.BaseModel):
    operating: float
    investing: float
    financing: float

class FundamentalAnalysis(pydantic.BaseModel):
    revenueGrowths: RevenueGrowths
    netProfit: float
    debtToEquityRatio: float
    roe: float
    cashFlow: CashFlow
    promoterHolding: float
    institutionalHolding: float

class TechnicalAnalysis(pydantic.BaseModel):
    pass

class PriceTrends(pydantic.BaseModel):
    oneMonth: float
    sixMonth: float
    oneYear: float

class HistoricalPerformance(pydantic.BaseModel):
    priceTrends: PriceTrends
    volatility: float
    returns: PriceTrends

class GovernmentPolicies(pydantic.BaseModel):
    gstRate: float
    corporateTaxRate: float

class EconomicIndicators(pydantic.BaseModel):
    InterestRates: float
    currencyExchangeRateUsdToInr: float
    governmentPolicies: GovernmentPolicies

class StockReport(pydantic.BaseModel):
    generalInfo: GeneralInfo
    financialData: FinancialData
    fundamentalAnalysis: FundamentalAnalysis
    technicalAnalysis: TechnicalAnalysis
    historicalPerformance: HistoricalPerformance
    newsAndUpdates: list[dict]
    economicIndicators: EconomicIndicators
    analystRatings: list[dict]
    peerComparison: list[dict]
    