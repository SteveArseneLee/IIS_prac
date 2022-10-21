import datetime

dt_kst = datetime.datetime.utcnow() + datetime.timedelta(hours=9)

YEAR = dt_kst.year

DEFAULT_HEADERS = {"Content-Type": "application/json; charset=utf-8"}

DATA_GO_KR_API_KEYS = {
    # 한국부동산원_실거래가격지수 통계 조회 서비스
    ## 지역별 실거래가격지수 조회
    1: "/RealTradingPriceIndexSvc/v1/getAptRealTradingPriceIndex",
    ## 규모별 실거래가격지수 조회
    2: "/RealTradingPriceIndexSvc/v1/getAptRealTradingPriceIndexSize", 

}