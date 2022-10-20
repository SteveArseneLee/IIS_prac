# Integrated Investment Service
2022년 2학기 캡스톤디자인2 프로젝트

### 🧑‍💻 구성원
이름 | 학과 |  학번  | 이메일 | Github
------------ | -------------  | ------------- | -------------  | ------------- 
이창렬 | 컴퓨터공학과 | 2019110634 | lclgood@khu.ac.kr | [Github Link](https://github.com/SteveArseneLee)
이창렬 | 컴퓨터공학과 | 2019110634 | devopser97@gmail.com | [Github Link](https://github.com/DevopsPracticer)
이창렬 | 컴퓨터공학과 | 2019110634 | dlckdfuf21@gmail.com | [Github Link](https://github.com/ArseneTest)

## 🔖 주제
The IIS platform helps users make investments based on information from four areas (apartments, land, stocks, and coins). The main target group is to show the past and present market prices of representative investment methods for all ages so that anyone can easily start investing.

IIS 플랫폼은 4가지 분야(아파트, 토지, 주식, 코인)의 정보를 토대로 사용자가 투자를 할 수 있게끔 도와준다. 주요 대상층은 전 연령대로 하여 대표적인 투자 방법들의 과거와 현재 시세를 보여주어 누구든 손쉽게 투자를 시작할 수 있도록 하는 것이 본 프로젝트의 목표이다.

## 📑 프로젝트 소개
To explain first in a large approximate framework, large-capacity unstructured data of different schemas from each source are primarily processed in Spark and supplied to Kafka according to Airflow's schedule. After that, Kafka's data is quickly purified by Flink and sent back to the new Kafka. Data entering Kafka is stored in AWS S3 or GCP File Storage. This results in the formation of a stem. As mentioned in the topic, four pipelines are constructed, and all pipelines are automatically scheduled via Airflow. Finally, instead of duplicating data from each stem through a virtual data warehouse in Snowflake, the inquired data is viewed in real time and viewed through Tableau.

대략적인 큰 틀로 먼저 설명을 하자면, 각 소스로부터 다른 스키마의 대용량 비정형 데이터들을 1차적으로 Spark에서 가공하여 Airflow의 스케쥴링에 따라 Kafka로 공급된다. 이후 Kafka의 데이터를 Flink에서 빠르게 2차 정제를 하여 다시 새로운 Kafka에게 보내준다. Kafka에 들어온 데이터는 AWS S3나 GCP File Storage에 저장된다. 이로써 한 줄기가 형성이 된다. 주제에서 언급한 바와 같이 4줄기의 파이프라인이 구성되고, 모든 파이프라인은 Airflow를 통해 자동 스케쥴링된다. 최종적으로 Snowflake에서 가상 데이터 웨어하우스를 통해 각 줄기로부터 데이터를 복제하는것이 아닌 실시간으로 조회를 하고 조회된 데이터는 Tableau를 통해 시각화되어 사용자에게 보여진다.

### 📋 Project Introduction
As a service for **prospective entrepreneurs**, it is a service that informs which business is suitable for a certain location before starting a business. It collects and refines a large amount of information required from various open API sites, and the information comes out when the user selects a location.


### 🗃️ Development Environment
- Apache Kafka
- Apache Spark
- Apache Flink
- Apache Airflow
- AWS EC2
- AWS S3
- Snowflake
- Tableau