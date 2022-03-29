# Project 1: Query Project


- In the Query Project, you will get practice with SQL while learning about
  Google Cloud Platform (GCP) and BiqQuery. You'll answer business-driven
  questions using public datasets housed in GCP. To give you experience with
  different ways to use those datasets, you will use the web UI (BiqQuery) and
  the command-line tools, and work with them in Jupyter Notebooks.

#### Problem Statement

- You're a data scientist at Lyft Bay Wheels (https://www.lyft.com/bikes/bay-wheels), formerly known as Ford GoBike, the
  company running Bay Area Bikeshare. You are trying to increase ridership, and
  you want to offer deals through the mobile app to do so. 
  
- What deals do you offer though? Currently, your company has several options which can change over time.  Please visit the website to see the current offers and other marketing information. Frequent offers include: 
  * Single Ride 
  * Monthly Membership
  * Annual Membership
  * Bike Share for All
  * Access Pass
  * Corporate Membership
  * etc.

- Through this project, you will answer these questions: 

  * What are the 5 most popular trips that you would call "commuter trips"? 
  
  * What are your recommendations for offers (justify based on your findings)?

- Please note that there are no exact answers to the above questions, just like in the proverbial real world.  This is not a simple exercise where each question above will have a simple SQL query. It is an exercise in analytics over inexact and dirty data. 

- You won't find a column in a table labeled "commuter trip".  You will find you need to do quite a bit of data exploration using SQL queries to determine your own definition of a communter trip.  In data exploration process, you will find a lot of dirty data, that you will need to either clean or filter out. You will then write SQL queries to find the communter trips.

- Likewise to make your recommendations, you will need to do data exploration, cleaning or filtering dirty data, etc. to come up with the final queries that will give you the supporting data for your recommendations. You can make any recommendations regarding the offers, including, but not limited to: 
  * market offers differently to generate more revenue 
  * remove offers that are not working 
  * modify exising offers to generate more revenue
  * create new offers for hidden business opportunities you have found
  * etc. 

#### All Work MUST be done in the Google Cloud Platform (GCP) / The Majority of Work MUST be done using BigQuery SQL / Usage of Temporary Tables, Views, Pandas, Data Visualizations

A couple of the goals of w205 are for students to learn how to work in a cloud environment (such as GCP) and how to use SQL against a big data data platform (such as Google BigQuery).  In keeping with these goals, please do all of your work in GCP, and the majority of your analytics work using BigQuery SQL queries.

You can make intermediate temporary tables or views in your own dataset in BigQuery as you like.  Actually, this is a great way to work!  These make data exploration much easier.  It's much easier when you have made temporary tables or views with only clean data, filtered rows, filtered columns, new columns, summary data, etc.  If you use intermediate temporary tables or views, you should include the SQL used to create these, along with a brief note mentioning that you used the temporary table or view.

In the final Jupyter Notebook, the results of your BigQuery SQL will be read into Pandas, where you will use the skills you learned in the Python class to print formatted Pandas tables, simple data visualizations using Seaborn / Matplotlib, etc.  You can use Pandas for simple transformations, but please remember the bulk of work should be done using Google BigQuery SQL.

#### GitHub Procedures

In your Python class you used GitHub, with a single repo for all assignments, where you committed without doing a pull request.  In this class, we will try to mimic the real world more closely, so our procedures will be enhanced. 

Each project, including this one, will have it's own repo.

Important:  In w205, please never merge your assignment branch to the master branch. 

Using the git command line: clone down the repo, leave the master branch untouched, create an assignment branch, and move to that branch:
- Open a linux command line to your virtual machine and be sure you are logged in as jupyter.
- Create a ~/w205 directory if it does not already exist `mkdir ~/w205`
- Change directory into the ~/w205 directory `cd ~/w205`
- Clone down your repo `git clone <https url for your repo>`
- Change directory into the repo `cd <repo name>`
- Create an assignment branch `git branch assignment`
- Checkout the assignment branch `git checkout assignment`

The previous steps only need to be done once.  Once you your clone is on the assignment branch it will remain on that branch unless you checkout another branch.

The project workflow follows this pattern, which may be repeated as many times as needed.  In fact it's best to do this frequently as it saves your work into GitHub in case your virtual machine becomes corrupt:
- Make changes to existing files as needed.
- Add new files as needed
- Stage modified files `git add <filename>`
- Commit staged files `git commit -m "<meaningful comment about your changes>"`
- Push the commit on your assignment branch from your clone to GitHub `git push origin assignment`

Once you are done, go to the GitHub web interface and create a pull request comparing the assignment branch to the master branch.  Add your instructor, and only your instructor, as the reviewer.  The date and time stamp of the pull request is considered the submission time for late penalties. 

If you decide to make more changes after you have created a pull request, you can simply close the pull request (without merge!), make more changes, stage, commit, push, and create a final pull request when you are done.  Note that the last data and time stamp of the last pull request will be considered the submission time for late penalties.

---

## Parts 1, 2, 3

We have broken down this project into 3 parts, about 1 week's work each to help you stay on track.

**You will only turn in the project once  at the end of part 3!**

- In Part 1, we will query using the Google BigQuery GUI interface in the cloud.

- In Part 2, we will query using the Linux command line from our virtual machine in the cloud.

- In Part 3, we will query from a Jupyter Notebook in our virtual machine in the cloud, save the results into Pandas, and present a report enhanced by Pandas output tables and simple data visualizations using Seaborn / Matplotlib.

---

## Part 1 - Querying Data with BigQuery

### SQL Tutorial

Please go through this SQL tutorial to help you learn the basics of SQL to help you complete this project.

SQL tutorial: https://www.w3schools.com/sql/default.asp

### Google Cloud Helpful Links

Read: https://cloud.google.com/docs/overview/

BigQuery: https://cloud.google.com/bigquery/

Public Datasets: Bring up your Google BigQuery console, open the menu for the public datasets, and navigate to the the dataset san_francisco.

- The Bay Bike Share has two datasets: a static one and a dynamic one.  The static one covers an historic period of about 3 years.  The dynamic one updates every 10 minutes or so.  THE STATIC ONE IS THE ONE WE WILL USE IN CLASS AND IN THE PROJECT. The reason is that is much easier to learn SQL against a static target instead of a moving target.

- (USE THESE TABLES!) The static tables we will be using in this class are in the dataset **san_francisco** :

  * bikeshare_stations

  * bikeshare_status

  * bikeshare_trips

- The dynamic tables are found in the dataset **san_francisco_bikeshare**

### Some initial queries

Paste your SQL query and answer the question in a sentence.  Be sure you properly format your queries and results using markdown. 

#### Question 1. What is the size of the dataset?

A. There are 74 records in bikeshare_stations.

*SQL query:*  
```
SELECT COUNT(*) 
FROM bigquery-public-data.san_francisco.bikeshare_stations
```


B. Bikeshare status dataset contain 107,501,619 records.

*SQL query:*  
```
SELECT COUNT(*) 
FROM bigquery-public-data.san_francisco.bikeshare_status
```

C. Bikshare trips data set contains 983,648 trips.  The smallest trip_id is 4069 and the largest trip_id is 1338408.  

*SQL query:*  
```
SELECT 
  COUNT(*) 
  num_trips, 
  MIN(trip_id) min_trip_id, 
  MAX(trip_id) as max_trip_id 
FROM bigquery-public-data.san_francisco.bikeshare_trips
```

Note:  Bikeshare_stations and bikeshare_trips datasets contains 74 stations.  Bikeshare_status dataset contains 75 stations.  There is a discrepancy over station 87.  No trip data exists for station 87.

#### Question 2. What is the earliest start date and time and latest end date and time for a trip?

2.1 The earlist start date and time is: 2013-08-29 09:08:00 UTC

2.2 The latest end date and time is: 2016-08-31 23:32:00 UTC

*SQL query:*  
```
SELECT
  MIN(start_date) min_start_date, 
  MAX(start_date) max_end_date 
FROM bigquery-public-data.san_francisco.bikeshare_trips
```

#### Question 3. How many bikes are there?

There are 700 bikes.  The smallest bike number is 9, the largest bike number is 878.

*SQL query:*  
```
SELECT 
  COUNT(DISTINCT(bike_number)) num_bikes, 
  MIN(bike_number) min_bike_number, 
  MAX(bike_number) max_bike_number 
FROM bigquery-public-data.san_francisco.bikeshare_trips
```

#### Question 4: 
What are the the number of trips, minimum trip time, maximum trip time, total trip duration, and average trip times of customers vs subsribers per year?

#### Answer 4:
  
| subscriber_type| date_yr | num_trips | min_trip_time | max_trip_time | total_trip_time_hr | avg_trip_time_min |
| ---------------|---------|----------:|--------------:|--------------:|-------------------:|------------------:|
| Customer       | 2013    | 24499     | 1.03          | 12037.27      | 24099.67           | 59.0              |     
| Subscriber     | 2013    | 76064     | 1.0           | 10322.03      | 12724.99           | 10.0              | 
| Customer       | 2014    | 48576     | 1.0           | 287840.0      | 57196.13           | 71.0              |
| Subscriber     | 2014    | 277763    | 1.0           | 11941.33      | 45416.4            | 10.0              | 
| Customer       | 2015    | 40530     | 1.0           | 35616.67      | 40833.52           | 60.0              |
| Subscriber     | 2015    | 305722    | 1.0           | 30876.5       | 49667.02           | 10.0              | 
| Customer       | 2016    | 23204     | 1.0           | 1438.75       | 19193.81           | 50.0              |
| Subscriber     | 2016    | 187290    | 1.0           | 1431.67       | 29277.01           | 9.0               | 


The min and max trip times in the dataset reveals the apparent need for data cleansing before determining the number of commuter trips. 

#### SQL query 4:
```
SELECT 
  subscriber_type,  
  extract(year from start_date) as date_yr,  
  count(distinct trip_id) as num_trips,  
  round(min(duration_sec/60),2) as min_trip_time,  
  round(max(duration_sec/60),2) as max_trip_time,  
  round(sum(duration_sec/3600), 2) as total_trip_time_hr,  
  round(avg(duration_sec/60)) as avg_trip_time_min,  
FROM `bigquery-public-data.san_francisco.bikeshare_trips`  
GROUP BY subscriber_type, date_yr  
ORDER BY date_yr, subscriber_type
```

#### Question 5: 
How many trips equal or exceed 24 hours?

#### Answer 5:

| subscriber_type| date_yr | num_trips_grteq_24h | 
| ---------------|---------|--------------------:|
| Customer       | 2013    | 53                  |    
| Subscriber     | 2013    | 8                   |
| Customer       | 2014    | 116                 |
| Subscriber     | 2014    | 21                  | 
| Customer       | 2015    | 79                  | 
| Subscriber     | 2015    | 19                  |  

#### SQL query 5: 
```
SELECT 
  subscriber_type,  
  extract(year from start_date) as date_yr,  
  count(distinct trip_id) as num_trips_grteq_24h,  
FROM `bigquery-public-data.san_francisco.bikeshare_trips`  
WHERE duration_sec >= 86400
GROUP BY subscriber_type, date_yr  
ORDER BY date_yr, subscriber_type
```

#### Question 6: 
What are the top three months per year ranked by the sum of total trip duration?

#### Answer 6:
The top three months for 2014 were December, August, and July respectively.  The top three months for 2015 were June, July, and May respectively.  I chose the years 2014 and 2015 because they were the only year within the dataset that contained a full year of data.  These preliminary results include all trip duration lengths.  From the previous question/answer, it is evident that the results may be skewed from unreasonably long trip durations.

| date_year | date_month | total_duration | month_rank | 
|:----------|:-----------|---------------:|-----------:|
| 2014      | Dec        | 41131402       | 1          |   
| 2014      | Aug        | 35872563       | 2          |
| 2014      | Jul        | 35100569       | 3          |
| 2015      | Jun        | 34481927       | 1          |
| 2015      | Jul        | 33983062       | 2          |
| 2015      | May        | 31584633       | 3          |

#### SQL query 6: 
```  
# Select all columns
SELECT *
FROM(        
    # Rank months, create column month_ranck, by year according to total trip duration (total_duration)
    SELECT *, rank() over(partition by date_year ORDER BY total_duration DESC) as month_rank #window function
    FROM(
        # Sum the total duration of all trip, select the contrived date_year and date_month column
        SELECT  date_year,
                date_month,
                sum(duration_sec) as total_duration,
        FROM(
            # Extract the year from the datetime start_date, format the month to the abbreviated month of the year
            SELECT EXTRACT(year FROM start_date) AS date_year, 
                   FORMAT_DATETIME("%b", DATETIME(start_date)) AS date_month, *
            FROM bigquery-public-data.san_francisco.bikeshare_trips
            )
        # Examine data from years 2014 and 2015.  The data set only contains two full years.
        # Group by the year, then by the month, order the output by the sum of total_duration.
        WHERE date_year >= 2014 and date_year <=2015
        GROUP BY 1,2
        ORDER BY total_duration DESC
    ))
# Limit months per year to the top 3 months.
WHERE month_rank <= 3
ORDER BY date_year, month_rank
```

#### Question 7: 
Filter the data to query only trips that are less than 24 hours.
What are the top three months per year ranked by the sum of total trip duration?

#### Answer 7:


| date_year | date_month | total_duration | month_rank | 
|:----------|:-----------|---------------:|-----------:|
| 2014      | August     | 33143439       | 1          |   
| 2014      | July       | 32841542       | 2          |
| 2014      | May        | 30610604       | 3          |
| 2015      | July       | 31006104       | 1          |
| 2015      | August     | 29237615       | 2          |
| 2015      | June       | 29030369       | 3          |

#### SQL query 7:
```
# Select all columns
SELECT *
FROM(        
    # Rank months, create column month_ranck, by year according to total trip duration (total_duration)
    SELECT *, rank() over(partition by date_year ORDER BY total_duration DESC) as month_rank #window function
    FROM(
        # Sum the total duration of all trip, select the contrived date_year and date_month column
        SELECT  date_year,
                date_month,
                sum(duration_sec) as total_duration,
        FROM(
            # Extract the year from the datetime start_date, format the month to the abbreviated month of the year
            SELECT EXTRACT(year FROM start_date) AS date_year, 
                   FORMAT_DATETIME("%B", DATETIME(start_date)) AS date_month, *
            FROM bigquery-public-data.san_francisco.bikeshare_trips
            )
        # Query data from years 2014 and 2015.  The data set only contains two full years.
        # Query data with trip duration less than 24 hours.
        # Group by the year, then by the month, order the output by the sum of total_duration.
        WHERE (date_year >= 2014 and date_year <=2015) and duration_sec < 84600
        GROUP BY 1,2
        ORDER BY total_duration DESC
        ))
# Limit months per year to the top 3 months.
WHERE month_rank <= 3
ORDER BY date_year, month_rank
```

### Bonus activity queries (optional - not graded - just this section is optional, all other sections are required)

The bike share dynamic dataset offers multiple tables that can be joined to learn more interesting facts about the bike share business across all regions. These advanced queries are designed to challenge you to explore the other tables, using only the available metadata to create views that give you a broader understanding of the overall volumes across the regions(each region has multiple stations)

We can create a temporary table or view against the dynamic dataset to join to our static dataset.

Here is some SQL to pull the region_id and station_id from the dynamic dataset.  You can save the results of this query to a temporary table or view.  You can then join the static tables to this table or view to find the region:
```sql
#standardSQL
select distinct region_id, station_id
from `bigquery-public-data.san_francisco_bikeshare.bikeshare_station_info`
```

- Top 5 popular station pairs in each region

- Top 3 most popular regions(stations belong within 1 region)

- Total trips for each short station name in each region

- What are the top 10 used bikes in each of the top 3 region. these bikes could be in need of more frequent maintenance.

---

## Part 2 - Querying data from the BigQuery CLI 

- Use BQ from the Linux command line:

  * General query structure

    ```
    bq query --use_legacy_sql=false '
        SELECT count(*)
        FROM `bigquery-public-data.san_francisco.bikeshare_trips`'
    ```

### Queries

1. Rerun the first 3 queries from Part 1 using bq command line tool (Paste your bq
   queries and results here, using properly formatted markdown):

#### Question 1: 
What's the size of this dataset? (i.e., how many trips)

#### Answer 1:
The dataset contains 983,648 records (bikeshare_trips).
| num_trips |
|-----------|
|    983648 |

#### bq query 1:
```
bq query --use_legacy_sql=false '
SELECT count(DISTINCT trip_id) AS num_trips
FROM `bigquery-public-data.san_francisco.bikeshare_trips`'
```
#### Question 2: 
What is the earliest start time and latest end time for a trip?

#### Answer 2:

The earliest start date is August 28, 2013 at 9:08 AM.  The latest end date is August 31, 2016 at midnight.  The earliest start time for a trip is midnight(00:00).  The latest end time for a trip is 11:59 PM.  

|      min_start      |       max_end       |
|---------------------|---------------------|
| 2013-08-29 09:08:00 | 2016-08-31 23:48:00 |


| hour | minute | trip_id | duration_sec |     start_date      | start_station_name | start_station_id |      end_date       | end_station_name | end_station_id | bike_number | zip_code | subscriber_type |
|------|--------|---------|--------------|---------------------|--------------------|------------------|---------------------|------------------|----------------|-------------|----------|-----------------|
|    0 |      0 |    6481 |         3131 | 2013-08-31 00:00:00 | Market at 4th      |               76 | 2013-08-31 00:52:00 | Spear at Folsom  |             49 |         411 | 94122    | Customer        |

| hour | minute | trip_id | duration_sec |     start_date      |    start_station_name    | start_station_id |      end_date       | end_station_name | end_station_id | bike_number | zip_code | subscriber_type |
|------|--------|---------|--------------|---------------------|--------------------------|------------------|---------------------|------------------|----------------|-------------|----------|-----------------|
|   23 |     59 | 1324664 |         1706 | 2016-08-21 23:30:00 | South Van Ness at Market |               66 | 2016-08-21 23:59:00 | Market at 10th   |             67 |         572 | 96734    | Customer        |

#### bq query 2:
```
bq query --use_legacy_sql=false '
SELECT min(start_date) AS min_start, max(end_date) AS max_end
FROM `bigquery-public-data.san_francisco.bikeshare_trips`'
```
```
bq query --use_legacy_sql=false '
SELECT EXTRACT(HOUR FROM start_date) AS hour, EXTRACT(MINUTE FROM start_date) AS minute, *
FROM `bigquery-public-data.san_francisco.bikeshare_trips`' ORDER BY 1,2,start_date LIMIT 1
```
```
bq query --use_legacy_sql=false '
SELECT EXTRACT(HOUR FROM end_date) AS hour, EXTRACT(MINUTE FROM end_date) AS minute, *
FROM `bigquery-public-data.san_francisco.bikeshare_trips`' ORDER BY 1 DESC, 2 DESC ,end_date DESC LIMIT 1
```

#### Question 3: 
How many bikes are there?

#### Answer 3:
There are 700 unique bike identification numbers.  Therefore, there are 700 bikes.
| bike_count |
|------------|
|        700 |

#### bq query 3:
```
bq query --use_legacy_sql=false '
SELECT COUNT(DISTINCT bike_number) AS bike_count
FROM `bigquery-public-data.san_francisco.bikeshare_trips`'
```

2. New Query (Run using bq and paste your SQL query and answer the question in a sentence, using properly formatted markdown):

#### Question: 
How many trips are in the morning vs in the afternoon?

#### Answer:
There were 404,919 trips made during the morning hours and 264,897 trips made during the afternoon hours.  I classified my results based on the following times of the day:
  
#### Parts of the Day
Morning     5 am to 12 pm  
Afternoon   12 pm to 5 pm  
Evening     5 pm to 9 pm  
Night       9 pm to 4 am 

| morning_trips | afternoon_trips | evening_trips | night_trips |
|---------------|-----------------|---------------|-------------|
|        404919 |          264897 |        274689 |       39143 |

*bq query:*
```
bq query --use_legacy_sql=false '
SELECT 
    SUM(CASE WHEN EXTRACT(HOUR FROM start_date) IN (5,6,7,8,9,10,11) THEN 1 ELSE 0 END) AS morning_trips,
    SUM(CASE WHEN EXTRACT(HOUR FROM start_date) IN (12,13,14,15,16) THEN 1 ELSE 0 END) AS afternoon_trips,
    SUM(CASE WHEN EXTRACT(HOUR FROM start_date) IN (17,18,19,20) THEN 1 ELSE 0 END) AS evening_trips,
    SUM(CASE WHEN EXTRACT (HOUR FROM start_date) IN (21,22,23,0,1,2,3,4) THEN 1 ELSE 0 END) AS night_trips 
FROM `bigquery-public-data.san_francisco.bikeshare_trips`'
```


### Project Questions
Identify the main questions you'll need to answer to make recommendations (list
below, add as many questions as you need).

### 1. What are your recommendations for offers (justify based on your findings)?

- Question 1:  What stations experience the most number of trips?

- Question 2:  What stations have the most duration of trips?

- Question 3:  What is the trip distribution per day?

- Question 4:  What is the total duration of trips per month? 

- Question 5:  What is the distribution of trips per month? 

- Question 6:  What is the capacity of each station?

- Question 7:  Are there stations that are low on bikes or dock positions?

### 1. What are top five commuter trips?

- Question 8:  What criteria classifies a commuter trip?

- Question 9:  What is the average commuter trip duration?

- Question 10:  When do commuters typically commute?

Please refer to the ipython notebook, link below, for ridership recommendations and top 5 commuter trips.

project_01.ipynb
(https://github.com/mids-w205-schioberg/project-1-samueljgomez/blob/project1/project_01.ipynb)


---

## Part 3 - Employ notebooks to synthesize query project results

### Get Going

Create a Jupyter Notebook against a Python 3 kernel named Project_1.ipynb in the assignment branch of your repo.

#### Run queries in the notebook 

At the end of this document is an example Jupyter Notebook you can take a look at and run.  

You can run queries using the "bang" command to shell out, such as this:

```
! bq query --use_legacy_sql=FALSE '<your-query-here>'
```

- NOTE: 
- Queries that return over 16K rows will not run this way, 
- Run groupbys etc in the bq web interface and save that as a table in BQ. 
- Max rows is defaulted to 100, use the command line parameter `--max_rows=1000000` to make it larger
- Query those tables the same way as in `example.ipynb`

Or you can use the magic commands, such as this:

```sql
%%bigquery my_panda_data_frame

select start_station_name, end_station_name
from `bigquery-public-data.san_francisco.bikeshare_trips`
where start_station_name <> end_station_name
limit 10
```

```python
my_panda_data_frame
```

#### Report in the form of the Jupter Notebook named Project_1.ipynb

- Using markdown cells, MUST definitively state and answer the two project questions:

  * What are the 5 most popular trips that you would call "commuter trips"? 
  
  * What are your recommendations for offers (justify based on your findings)?

- For any temporary tables (or views) that you created, include the SQL in markdown cells

- Use code cells for SQL you ran to load into Pandas, either using the !bq or the magic commands

- Use code cells to create Pandas formatted output tables (at least 3) to present or support your findings

- Use code cells to create simple data visualizations using Seaborn / Matplotlib (at least 2) to present or support your findings

### Resource: see example .ipynb file 

[Example Notebook](example.ipynb)

