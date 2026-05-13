# Assignment 2 – Implementation of MapReduce using Hadoop

## Subject: Data Science & Big Data Analytics Lab (DS & BDA)
## Platform: Hadoop 2.7.7 (Pseudo-Distributed Mode)
## Student Name: Jaykumar Kale
## Environment: Ubuntu 22.04 (VirtualBox on Windows 11)

---

# 1. Aim

To install and configure Hadoop in pseudo-distributed mode and execute a MapReduce program (WordCount) using HDFS.

---

# 2. Objective

- Setup Hadoop environment
- Configure HDFS and YARN
- Start Hadoop daemons
- Upload data into HDFS
- Execute MapReduce WordCount program
- View output in HDFS
- Access Hadoop Web UI

---

# 3. Software Requirements

- Windows 11 (Host OS)
- Oracle VirtualBox
- Ubuntu 22.04 Desktop (Guest OS)
- Java JDK 11
- Hadoop 2.7.7

---

# 4. Hadoop Architecture Overview

Hadoop consists of:

## 4.1 HDFS (Storage Layer)

- NameNode – Master node managing metadata
- DataNode – Stores actual data blocks
- SecondaryNameNode – Checkpoint node

## 4.2 MapReduce (Processing Layer)

- Mapper – Processes input data
- Reducer – Aggregates results
- YARN – Resource management layer

---

# 5. Hadoop Configuration Files

Configuration files located at:

```
/usr/local/hadoop/etc/hadoop/
```

Modified files:

- core-site.xml
- hdfs-site.xml
- mapred-site.xml
- yarn-site.xml
- hadoop-env.sh

---

# 6. Starting Hadoop Services

## 6.1 Start HDFS

```bash
start-dfs.sh
```

## 6.2 Start YARN

```bash
start-yarn.sh
```

## 6.3 Verify Running Processes

```bash
jps
```

Expected Output:

- NameNode
- DataNode
- SecondaryNameNode
- ResourceManager
- NodeManager

---

# 7. Hadoop Web Interface

## 7.1 NameNode UI

Access at:

```
http://localhost:50070
```

Shows:

- Cluster Summary
- Live DataNodes
- DFS Usage
- Hadoop Version

(Screenshot Attached)

---

## 7.2 YARN Resource Manager UI

Access at:

```
http://localhost:8088
```

Shows:

- Running Applications
- MapReduce Jobs
- Cluster Metrics

(Screenshot Attached)

---

# 8. Implementation – WordCount Program

## 8.1 Create Sample Input File

```bash
nano sample.txt
```

Example content:

```
Big data is powerful
Hadoop processes big data
Big data requires distributed systems
```

---

## 8.2 Create HDFS Directory

```bash
hdfs dfs -mkdir /input
```

---

## 8.3 Upload File to HDFS

```bash
hdfs dfs -put sample.txt /input
```

Verify:

```bash
hdfs dfs -ls /input
```

---

## 8.4 Run WordCount MapReduce Job

```bash
hadoop jar /usr/local/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.7.7.jar wordcount /input /output
```

---

## 8.5 View Output

```bash
hdfs dfs -cat /output/part-r-00000
```

Output:

```
Big        2
Hadoop     1
big        1
data       3
distributed 1
is         1
powerful   1
processes  1
requires   1
systems    1
```

---

# 9. Explanation of Working

## Step 1 – Mapper Phase

Each word is converted into:

```
(word, 1)
```

Example:

```
Big → (Big,1)
data → (data,1)
```

---

## Step 2 – Shuffle and Sort

System groups same keys together:

```
(Big,1) (Big,1)
(data,1) (data,1) (data,1)
```

---

## Step 3 – Reducer Phase

Reducer adds counts:

```
Big → 2
data → 3
```

---

# 10. Result

MapReduce WordCount program executed successfully in Hadoop pseudo-distributed mode.

HDFS and YARN services were verified using web interfaces.

Output was correctly generated and validated.

---

# 11. Conclusion

The Hadoop cluster was successfully configured and a MapReduce WordCount program was executed.

The experiment demonstrates:

- HDFS data storage
- MapReduce processing
- YARN resource management
- Web-based cluster monitoring

This confirms successful implementation of Big Data processing using Hadoop.

---

# 12. Viva Questions

### Q1. What is Hadoop?
Hadoop is an open-source framework for distributed storage and processing of large datasets.

### Q2. What is HDFS?
Hadoop Distributed File System used to store big data across distributed nodes.

### Q3. What is MapReduce?
A programming model for parallel processing of large datasets.

### Q4. What is NameNode?
Master node that stores metadata of HDFS.

### Q5. What is YARN?
Resource management layer of Hadoop.

---

# Screenshots Attached

1. NameNode Web UI (Port 50070)
2. YARN Resource Manager UI (Port 8088)
3. Terminal Execution of WordCount
4. HDFS Output Result

---

End of Assignment 2