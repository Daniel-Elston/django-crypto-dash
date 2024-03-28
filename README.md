# Live Crypto Analysis Dashboard with Django

Please see: ```data_management/management/commands``` for ETL process

This project is a comprehensive crypto analysis dashboard that offers real-time insights into cryptocurrency markets. Utilizing Django for the web framework, ccxt for fetching live market data, and PostgreSQL for data storage, the dashboard presents a dynamic view of cryptocurrency metrics, including price movements and volume trends.

#### -- Project Status: [ongoing]

---

## Project Objective

The aim of this project is to provide a live dashboard for cryptocurrency analysis, enabling the monitoring of real-time market data and trends. The dashboard allows users to view tabular data, visualize cryptocurrency prices, and select different symbols for a tailored analysis. Efficiency in data handling and storage is achieved through pooling, temporary storage, and batch database updates.

## Technologies

* Python
* HTML
* JavaScript
* CSS
* PostgreSQL
* Requests
* asyncio
* pprint
* ccxt (for API data fetching)
* PyArrow
* SQLAlchemy
* psycopg2
* aiofiles
* Django

## Methodologies

- **Data Fetching:** Using `ccxt` as an API wrapper to continuously fetch live cryptocurrency market data.
- **Data Processing:** Transforming data types and utilizing temporary JSON storage to accumulate data before batch updating the PostgreSQL database, enhancing efficiency and reducing database load.
- **Web Development:** Creating a responsive and interactive dashboard using Django, along with HTML, JavaScript, and CSS for frontend development.
- **Visualization:** Implementing dynamic visualizations for cryptocurrency prices and trends, allowing users to select different cryptocurrencies for analysis through an interactive dropdown menu.
- **Efficient Data Management:** Employing connection pooling and asyncio for efficient data handling and storage, ensuring timely updates to the dashboard without compromising performance.

---

## Contacts

For further information or to discuss this project in detail, please reach out.

Email: delstonds@outlook.com
