# Assignment 3 – Flight Information System using HiveQL

## AIM  
To write an application using HiveQL for a Flight Information System.

---

# PROBLEM STATEMENT

Develop a Flight Information System using HiveQL that includes:

1. Creating, Dropping, and Altering database tables  
2. Creating an External Hive table  
3. Loading data, inserting new records, and joining tables  
4. Creating an Index on the Flight table  
5. Finding the average departure delay per day in 2008  

---

# OBJECTIVES

- To understand NoSQL databases  
- To understand integration of NoSQL with Hadoop  
- To analyze distributed processing performance using Hive over Hadoop  

---

# INTRODUCTION

Apache Hive is a data warehouse system built on top of Hadoop.  
It allows querying and managing large datasets stored in HDFS using HiveQL (SQL-like language).

Hive is:

- Schema-on-read system  
- Distributed query engine  
- Uses Hadoop (MapReduce) for processing  
- Stores metadata in Metastore (Derby/MySQL)  

---

# ARCHITECTURE USED

Ubuntu VM  
→ Hadoop (HDFS running)  
→ Hive 2.3.9  
→ Embedded Derby Metastore  

---

# STEP 1 – CREATE DATABASE

```sql
create database flightdb;
show databases;
use flightdb;
```

Purpose:
- Logical grouping of tables
- Isolation of project

---

# STEP 2 – CREATE MANAGED TABLE

```sql
create table flights(
year int,
month int,
day int,
flight_no string,
origin string,
destination string,
dep_delay int,
arr_delay int
)
row format delimited
fields terminated by ','
stored as textfile;
```

Concept:
- Managed table stores both metadata and data inside Hive warehouse
- Dropping table deletes data from HDFS

---

# STEP 3 – CREATE EXTERNAL TABLE

External table data is stored in HDFS manually.

First upload file:

```bash
hdfs dfs -mkdir /flightdata
hdfs dfs -put flights2008.csv /flightdata
```

Then create external table:

```sql
create external table flights_ext(
year int,
month int,
day int,
flight_no string,
origin string,
destination string,
dep_delay int,
arr_delay int
)
row format delimited
fields terminated by ','
stored as textfile
location '/flightdata';
```

Concept:
- Metadata stored in Hive
- Data remains in HDFS
- Dropping table does NOT delete data

Difference:

| Managed Table | External Table |
|---------------|---------------|
| Data stored in warehouse | Data stored externally |
| Dropping deletes data | Dropping keeps data |

---

# STEP 4 – LOAD DATA INTO MANAGED TABLE

```sql
load data local inpath '/home/jaykumar/hive/flights2008.csv'
into table flights;
```

Concept:
- Moves file from local system to Hive warehouse
- Creates HDFS copy

---

# STEP 5 – INSERT NEW RECORD

```sql
insert into flights values
(2008,1,4,'F107','NYC','LAX',15,10);
```

Concept:
- Adds additional record
- Hive internally runs MapReduce job

---

# STEP 6 – ALTER TABLE

```sql
alter table flights add columns (airline string);
```

Concept:
- Modifies schema
- Hive supports schema evolution

---

# STEP 7 – CREATE SECOND TABLE (AIRLINES)

```sql
create table airlines(
flight_no string,
airline_name string
)
row format delimited
fields terminated by ',';
```

Insert records:

```sql
insert into airlines values
('F101','Delta'),
('F102','United'),
('F103','Indigo'),
('F104','SpiceJet'),
('F105','AirIndia'),
('F106','Emirates'),
('F107','Lufthansa');
```

---

# STEP 8 – JOIN TABLES

```sql
select f.flight_no, f.origin, f.destination, a.airline_name
from flights f
join airlines a
on f.flight_no = a.flight_no;
```

Concept:
- Hive performs distributed join
- Executes using MapReduce

Output:

F107 NYC LAX Lufthansa  
F101 NYC LAX Delta  
F102 LAX NYC United  
F103 NYC CHI Indigo  
F104 CHI NYC SpiceJet  
F105 LAX CHI AirIndia  
F106 CHI LAX Emirates  

---

# STEP 9 – CREATE INDEX

```sql
create index flight_index
on table flights (flight_no)
as 'COMPACT'
with deferred rebuild;

alter index flight_index on flights rebuild;
```

Concept:
- Index improves search performance
- COMPACT index stores key + block location
- Rebuild physically creates index table

---

# STEP 10 – AVERAGE DEPARTURE DELAY PER DAY (2008)

```sql
select day, avg(dep_delay) as avg_departure_delay
from flights
where year = 2008
group by day
order by day;
```

Output:

Day | Average Departure Delay  
1   | 2.5  
2   | 10.0  
3   | 10.0  
4   | 15.0  

Concept:
- WHERE filters data
- GROUP BY aggregates per day
- AVG calculates mean delay
- ORDER BY sorts result

---

# HIVE CONCEPTS USED

✔ Database creation  
✔ Managed table  
✔ External table  
✔ Load data  
✔ Insert  
✔ Alter table  
✔ Join  
✔ Index  
✔ Aggregate functions  
✔ Group By  
✔ Order By  

---

# HOW HIVE INTEGRATES WITH HADOOP

- Data stored in HDFS  
- Queries converted into MapReduce jobs  
- Distributed execution across nodes  
- Metadata stored in Metastore  

Flow:
HiveQL → Compiler → Execution Engine → MapReduce → HDFS  

---

# NOSQL CHARACTERISTICS OF HIVE

- Schema-on-read  
- Handles large unstructured datasets  
- Horizontal scalability  
- Distributed storage  
- High throughput  

---

# PERFORMANCE ANALYSIS

Hive uses:

- Map phase for data scanning  
- Reduce phase for aggregation  
- Local mode execution in single-node cluster  

Advantages:
- Handles large datasets  
- Fault tolerant  
- Distributed processing  

---

# CONCLUSION

The Flight Information System was successfully implemented using HiveQL.

The application demonstrated:

- Database and table creation  
- Data loading and manipulation  
- External table handling  
- Distributed joins  
- Index creation  
- Analytical query (Average Delay)  

Hive effectively integrates with Hadoop to provide scalable, distributed data processing for large datasets.

---

# VIVA PREPARATION (IMPORTANT)

Q1. What is Hive?  
→ Data warehouse tool on Hadoop.

Q2. Difference between Managed and External table?  
→ Managed deletes data on drop, External does not.

Q3. What is Schema-on-read?  
→ Schema applied at query time.

Q4. What is Metastore?  
→ Stores table metadata.

Q5. What engine does Hive use?  
→ MapReduce (in this setup).

Q6. Why Index?  
→ Improve query performance.

---

END OF ASSIGNMENT 3