# Assignment 2

## AIM:
Design a distributed application using MapReduce which processes a system log file and lists out the users who have logged in for the maximum period on the system.

---

## PROBLEM STATEMENT:
Design a distributed application using MapReduce to process a log file of a system. The program should compute the total login time for each user and determine which user has logged in for the maximum period. The program must be executed in pseudo-distributed mode on Hadoop.

---

## OBJECTIVES:

- To understand the concept of MapReduce.
- To understand the working of Hadoop Distributed File System (HDFS).
- To understand log file processing using distributed computing.
- To analyze the performance of Hadoop.
- To understand distributed processing techniques.

---

## THEORY:

### What is MapReduce?

MapReduce is a programming model used for processing large datasets in a distributed computing environment. It works in two phases:

1. **Map Phase**  
   The mapper processes input data and converts it into key-value pairs.

2. **Reduce Phase**  
   The reducer processes grouped key-value pairs and produces the final output.

MapReduce works on the principle of moving computation to the data instead of moving data to computation.

---

### MapReduce Execution Stages:

1. Map Stage  
   Input data from HDFS is split and processed line by line.

2. Shuffle and Sort  
   Intermediate data is grouped based on keys.

3. Reduce Stage  
   Final computation is performed and results are stored in HDFS.

---

## INPUT DATA (log.txt):

```
user1 120
user2 340
user3 220
user1 150
user2 100
user4 500
```

Each line represents:

```
<username> <login_time_in_minutes>
```

---

## ALGORITHM:

1. Read each line from the log file.
2. Mapper extracts:
   - Key = username
   - Value = login time
3. Hadoop groups values by username.
4. Reducer calculates total login time per user.
5. Output final aggregated login time.
6. Identify the user with maximum login time.

---

## MAPPER LOGIC:

Input:  
`<LongWritable key, Text value>`

Process:
- Split line using space
- Extract username and login time
- Emit (username, login_time)

Output:
`<Text, IntWritable>`

---

## REDUCER LOGIC:

Input:
`<Text key, Iterable<IntWritable> values>`

Process:
- Sum all login times for each user
- Emit (username, total_time)

Output:
`<Text, IntWritable>`

---

## EXECUTION STEPS:

### Step 1: Create Input File

```
nano log.txt
```

### Step 2: Compile Java Program

```
mkdir loginclasses
javac -classpath `hadoop classpath` -d loginclasses MaxLoginTime.java
```

### Step 3: Create JAR File

```
jar -cvf maxlogin.jar -C loginclasses/ .
```

### Step 4: Create HDFS Input Directory

```
hdfs dfs -mkdir /logininput
```

### Step 5: Upload Input File

```
hdfs dfs -put log.txt /logininput
```

### Step 6: Run MapReduce Job (Local Mode)

```
hadoop jar maxlogin.jar MaxLoginTime /logininput /loginoutput
```

---

## OUTPUT:

```
user1  270
user2  440
user3  220
user4  500
```

---

## RESULT:

The user who logged in for the maximum period is:

```
user4 → 500 minutes
```

---

## PERFORMANCE ANALYSIS:

- Map Input Records: 6
- Reduce Input Groups: 4
- Reduce Output Records: 4
- Execution Mode: Local Mode
- Execution Time: ~2 seconds

Local mode eliminates YARN scheduling overhead, resulting in faster execution for small datasets.

---

## CONCLUSION:

The MapReduce program successfully processed the system log file and computed total login time for each user. The distributed processing model efficiently grouped and aggregated login durations. The user with the maximum login period was identified correctly.

---

## VIVA QUESTIONS:

1. What is MapReduce?
2. What is the role of Mapper?
3. What is the role of Reducer?
4. What is HDFS?
5. Difference between local mode and pseudo-distributed mode?
6. What is Shuffle and Sort phase?
7. What are NameNode and DataNode?
8. Why is MapReduce scalable?

---

## REFERENCES:

- https://hadoop.apache.org/docs/current/
- Hadoop: The Definitive Guide