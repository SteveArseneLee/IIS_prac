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

### RDD transformation

- collect()
- take(숫자) : 숫자만큼의 데이터를 임의로 뽑기
- first() : 첫번째 element
- count() : 총 element 개수


### Aggregate
- RDD 데이터 타입과 Action결과 타입이 다를 경우 사용하며 파티션 단위의 연산 결과를 합치는 과정을 거친다
- RDD.aggregate(zeroValue, seqOp, combOp)
    - zeroValue : 각 파티션에서 누적할 시작 값
    - seqOp : 타입 변경 함수
    - combOp : 합치는 함수


### reduceByKey
*RDD.reduce(f) vs RDD.reduceByKey(func, numpartitions=None, partitionFunc=<function portable_hash>)*
- reduce: 주어지는 함수를 기준으로 요소들을 합침 (action)
- reduceByKey: Key를 기준으로 그룹을 만들고 합침 (trans)