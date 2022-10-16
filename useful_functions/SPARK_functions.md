### Key Value RDD로 할 수 있는 것들
- reduceByKey() : 키 값을 기준으로 테스크 처리
    - ex)
    ```py
        pairs = rdd.map(lambda x: (x,1)
        count = pairs.reduceByKey(lambda a, b, : a+b)
    ```
- groupByKey() : 키 값을 기준으로 벨류를 묶는다
- sortByKey() : 키 값을 기준으로 정렬
- keys() : 키 값 추출
- values() : 벨류값 추출   


- join
- rightOuterJoin
- leftOuterJoin
- subtractByKey   



### Mapping Values
- **KeyValue 데이터에서**Key를 바꾸지 않는 경우 map()대신 value만 다루는 mapValues()를 쓴다
- mapValues()
- flatMapValues()   
는 Value만 다루는 연산들이지만 RDD에서 Key는 유지됨