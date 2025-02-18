# -real-time-stock-price-data-pipeline
### **What does the project do?**

**"This project is a real-time stock price data pipeline built with Python, PostgreSQL, Kafka, AsyncIO, and Multiprocessing. It collects live stock prices from a public API, processes and cleans the data, then streams it in real-time using Kafka. The processed data is then stored in PostgreSQL for future analysis."**

### **How does it work?**

1. **Stock Data Fetching:**
    - **AsyncIO** is used to fetch live stock data asynchronously, which ensures that the program can retrieve data without blocking or slowing down other tasks.
2. **Data Processing:**
    - **Multiprocessing** is used to handle data processing in parallel. This helps speed up data cleaning and preparation before sending it to Kafka.
3. **Kafka Streaming:**
    - **Kafka** is used to stream the stock price data in real-time. It acts as a messaging system where the producer (your Python script) sends stock data to a Kafka topic, and the consumer processes it.
4. **Data Storage (PostgreSQL):**
    - After the stock prices are processed, the data is stored in **PostgreSQL** for analysis. It’s easy to query and track stock trends with SQL.

### **Why is this useful?**

**"This project simulates a real-time data pipeline, which is crucial for modern applications that rely on live data. It could be used for financial analytics, stock market tracking, or even automated trading systems. By integrating AsyncIO, Kafka, and PostgreSQL, the project demonstrates essential backend technologies for handling large amounts of real-time data efficiently."**
