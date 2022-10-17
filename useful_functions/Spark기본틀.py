from pyspark import SparkConf, SparkContext
# SparkConf는 사용자가 재정의해서 쓸 수 있는 설정 옵션들에 대한 키와 값을 갖고있는 객체
# SparkContext는 Spark 클러스터와 연결시켜주는 객체
appname = "짓고싶은 이름"
# setMaster("local")은 분산된 환경이 아닌 개발용 로컬 환경에서만 사용한다.
conf = SparkConf().setMaster("local").setAppName(appname)

sc = SparkContext(conf=conf)
# Context를 보고싶으면 sc.getConf().getAll()
directory = "디렉토리 위치"
filename="파일명"

lines = sc.textFile(f"file:///{directory}/{filename}")

