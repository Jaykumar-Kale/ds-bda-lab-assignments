# Hadoop 2.7.7 Single Node Installation and Configuration on Ubuntu

## 👨‍🎓 Student Details
- Name: Jaykumar Kale  
- Course: Third Year Information Technology  
- Subject: Data Science & Big Data Analytics Laboratory  
- Assignment: Hadoop Installation (Single Node)  

---

# 📌 AIM

To install and configure Apache Hadoop 2.7.7 in Single Node (Pseudo Distributed) mode on Ubuntu Linux and verify proper functioning of HDFS and YARN services.

---

# 📖 THEORY

Apache Hadoop is an open-source framework used for distributed storage and processing of large datasets using:

- HDFS (Hadoop Distributed File System)
- YARN (Yet Another Resource Negotiator)
- MapReduce

In Single Node Mode, all Hadoop daemons run on a single machine. It is used for learning and testing purposes.

---

# 🖥️ SYSTEM CONFIGURATION

- OS: Ubuntu (Linux)
- Hadoop Version: 2.7.7
- Java Version: OpenJDK 8
- Mode: Single Node (Pseudo Distributed)

---

# ⚙️ INSTALLATION STEPS

## Step 1: Install Java

```bash
sudo apt update
sudo apt install default-jdk
java -version
```

---

## Step 2: Download Hadoop 2.7.7

```bash
wget https://downloads.apache.org/hadoop/common/hadoop-2.7.7/hadoop-2.7.7.tar.gz
tar -xvzf hadoop-2.7.7.tar.gz
sudo mv hadoop-2.7.7 /usr/local/hadoop
```

---

## Step 3: Configure Environment Variables

Edit `.bashrc`

```bash
nano ~/.bashrc
```

Add:

```bash
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
export HADOOP_HOME=/usr/local/hadoop
export PATH=$PATH:$HADOOP_HOME/bin
export PATH=$PATH:$HADOOP_HOME/sbin
```

Apply changes:

```bash
source ~/.bashrc
```

---

# 🛠️ HADOOP CONFIGURATION FILES

Configuration files located at:

```
/usr/local/hadoop/etc/hadoop
```

---

## 1️⃣ core-site.xml

```xml
<configuration>
<property>
<name>fs.defaultFS</name>
<value>hdfs://localhost:9000</value>
</property>
</configuration>
```

---

## 2️⃣ hdfs-site.xml

```xml
<configuration>
<property>
<name>dfs.replication</name>
<value>1</value>
</property>
</configuration>
```

---

## 3️⃣ mapred-site.xml

```bash
cp mapred-site.xml.template mapred-site.xml
```

```xml
<configuration>
<property>
<name>mapreduce.framework.name</name>
<value>yarn</value>
</property>
</configuration>
```

---

## 4️⃣ yarn-site.xml

```xml
<configuration>
<property>
<name>yarn.nodemanager.aux-services</name>
<value>mapreduce_shuffle</value>
</property>
</configuration>
```

---

# 🧱 FORMAT NAMENODE

```bash
hdfs namenode -format
```

---

# ▶️ START HADOOP SERVICES

## Start HDFS

```bash
start-dfs.sh
```

## Start YARN

```bash
start-yarn.sh
```

---

# 🔍 VERIFY RUNNING SERVICES

```bash
jps
```

Expected Output:

```
NameNode
DataNode
SecondaryNameNode
ResourceManager
NodeManager
Jps
```

---

# 🌐 HADOOP WEB INTERFACES

- HDFS UI: http://localhost:50070
- YARN UI: http://localhost:8088

---

# 📦 CHECK HADOOP VERSION

```bash
hadoop version
```

Output:

```
Hadoop 2.7.7
Compiled by stevel
```

---

# 📊 RESULT

Hadoop 2.7.7 was successfully installed and configured in Single Node mode. All required services (NameNode, DataNode, ResourceManager, NodeManager) were running successfully.

---

# 📌 CONCLUSION

Thus, we have successfully installed and configured Apache Hadoop 2.7.7 in Single Node (Pseudo Distributed) mode on Ubuntu Linux. The HDFS and YARN services were verified using JPS command and Web UI.

---

# 📚 REFERENCES

- https://hadoop.apache.org/
- Hadoop Official Documentation