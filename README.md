# ElastiCache-MySQL-Integration

**Step-by-Step Project: Setting Up MySQL with ElastiCache (Redis) on AWS** 

Today, I successfully implemented **caching for a MySQL database using Redis via Amazon ElastiCache**. This greatly improves performance by reducing repeated database hits and delivering data faster!

🔹 Step 1: Launch an EC2 Instance  
✅ Created an Amazon Linux EC2 server  
✅ Connected to it using SSH

🔹 Step 2: Set Up Amazon RDS (MySQL)  
✅ Launched an RDS instance with MySQL engine  
✅ Connected to the DB from EC2 using:
```bash
mysql -h <rds-endpoint> -u admin -p<password>
```

✅ Inside MySQL:
```sql
CREATE DATABASE test;

USE test;

CREATE TABLE users (
  user_id VARCHAR(50) PRIMARY KEY,
  first_name VARCHAR(100),
  last_name VARCHAR(100),
  email VARCHAR(100)
);

-- Inserted sample records
INSERT INTO users VALUES ('12345', 'John', 'Doe', 'john.doe@example.com');
INSERT INTO users VALUES ('12349', 'Suresh', 'Raina', 'suresh@example.com');
```

🔹 Step 3: Set Up ElastiCache (Redis)  
✅ Opened ElastiCache service  
✅ Chose **Redis OSS**  
✅ Clicked "Create Cache Cluster"  
✅ Gave a name and launched  
✅ Copied the **Redis endpoint** (without port)

🔹 Step 4: Install Required Dependencies on EC2  
```bash
sudo yum install mariadb105-server -y
sudo yum install python3-pip -y
pip3 install pymysql redis
```

🔹 Step 5: Create Python Script (`cache.py`)  
✅ Wrote code to:

- Connect to RDS and fetch data
- Cache the data in Redis for 90 seconds
- Automatically use Redis if cache is available
- Refresh from RDS after cache expiry

**Key parts of the script**:
- `pymysql` for MySQL interaction  
- `redis` for ElastiCache connection  
- TTL (`ex=90`) for cache expiry logic

Step 6: Run and Test  
Run with:
```bash
python3 cache.py
```

🟢 First run: Data fetched from RDS and cached  
🟢 Second run: Data returned from Redis  
🟢 After 90 sec: Cache expired → data refreshed from RDS

What I Learned:
- How to use **Redis as a caching layer** for MySQL  
- Setting up and connecting **ElastiCache, RDS, and EC2**  
- Improved performance by avoiding repeated database queries  
- TTL-based caching logic in real-time apps

This project helped me understand real-world caching strategies and how AWS services can be combined to build scalable, optimized solutions.

**Tech Used:**  
`Amazon EC2` | `Amazon RDS` | `Amazon ElastiCache` | `Redis` | `MySQL` | `Python`



🔖 **#AWS #Redis #ElastiCache #RDS #MySQL #DevOps #Python #CloudComputing #Caching #PerformanceOptimization #HandsOn #LearningByDoing #StudentDeveloper #AWSCommunity**

