import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class Analytics:
    def __init__(self, vanna):
        self.vanna = vanna

    def revenue_trends_over_time(self):
        query = """
            SELECT 
                DATE(reservation_status_date) AS booking_day, 
                SUM(CAST(adr AS FLOAT)) AS daily_revenue
            FROM hotel_bookings
            WHERE reservation_status = 'Check-Out'
            GROUP BY booking_day
            ORDER BY booking_day;
        """
        df = pd.DataFrame(self.vanna.run_sql(query), columns=["booking_day", "daily_revenue"])
        df["booking_day"] = pd.to_datetime(df["booking_day"])
        return df

    def cancellation_rate(self):
        query = """
            SELECT 
                (COUNT(CASE WHEN is_canceled = '1' THEN 1 END) * 100.0 / COUNT(*)) AS cancellation_rate
            FROM hotel_bookings;
        """
        result = self.vanna.run_sql(query)
        return result[0][0]  # Returns the cancellation rate as a float

    def geographical_distribution(self):
        query = """
            SELECT 
                country, 
                COUNT(*) AS booking_count
            FROM hotel_bookings
            GROUP BY country
            ORDER BY booking_count DESC;
        """
        df = pd.DataFrame(self.vanna.run_sql(query), columns=["country", "booking_count"])
        return df

    def booking_lead_time_distribution(self):
        query = """
            SELECT 
                CAST(lead_time AS UNSIGNED) AS lead_time
            FROM hotel_bookings
            WHERE lead_time REGEXP '^[0-9]+$';        
            """
        df = pd.DataFrame(self.vanna.run_sql(query), columns=["lead_time"])
        return df

    def plot_revenue_trends(self):
        df = self.revenue_trends_over_time()
        plt.figure(figsize=(10, 6))
        sns.lineplot(x="booking_day", y="daily_revenue", data=df)
        plt.title("Revenue Trends Over Time")
        plt.xlabel("Date")
        plt.ylabel("Daily Revenue")
        plt.show()

    def plot_geographical_distribution(self):
        df = self.geographical_distribution()
        plt.figure(figsize=(10, 6))
        sns.barplot(x="country", y="booking_count", data=df)
        plt.title("Geographical Distribution of Bookings")
        plt.xlabel("Country")
        plt.ylabel("Booking Count")
        plt.xticks(rotation=45)
        plt.show()

    def plot_booking_lead_time_distribution(self):
        df = self.booking_lead_time_distribution()
        plt.figure(figsize=(10, 6))
        sns.histplot(df["lead_time"], bins=30, kde=True)
        plt.title("Booking Lead Time Distribution")
        plt.xlabel("Lead Time (Days)")
        plt.ylabel("Frequency")
        plt.show()
