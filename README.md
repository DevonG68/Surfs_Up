# Surfs_Up
Module 9: SQLite, SQLAlchemy, Flask 
Goal: Using python, panda functions and methods, and SQLAlchemy to filter the date column of the Measurements table in the ‘hawaii.sqlite’ database to retrieve all the temperatures for the month of June and December in Oahu in order to determine if the surf and ice cream shop business is sustainable year-round. Then convert those temperatures to a list by creating a DataFrame from the list and generate the summary statistics.



Assignment

•	Deliverable 1: Determine the Summary Statistics for June
o	In Step 1, write a query that filters the date column from the Measurement table to retrieve all the temperatures for the month of June.
![image](https://user-images.githubusercontent.com/85171897/141674006-b800eaca-8ac2-4c5d-90f9-4ae6a025745d.png)

 
o	In Step 2, convert the June temperatures to a list.
![image](https://user-images.githubusercontent.com/85171897/141674010-60e056f4-b4c2-4290-8bcd-311425271d0a.png)

 
o	In Step 3, create a DataFrame from the list of temperatures for the month of June.
![image](https://user-images.githubusercontent.com/85171897/141674022-27930897-8680-4c13-b078-6a6f98983516.png)

 
o	In Step 4, generate the summary statistics for the June temperatures DataFrame.
![image](https://user-images.githubusercontent.com/85171897/141674026-0914face-2c1a-49d5-8e2c-56950eed2765.png)

 
o	After you run Step 4 in your SurfsUp_Challenge.ipynb file, confirm that the summary statistics match the image below.
 ![image](https://user-images.githubusercontent.com/85171897/141674041-66571eb5-a4ec-4e2b-8182-47f45d98502f.png)

•	Deliverable 2: Determine the Summary Statistics for December
o	Use the instructions below to add code where indicated by the numbered comments in your SurfsUp_Challenge.ipynb file.
o	In Step 6, write a query that filters the date column from the Measurement table to retrieve all the temperatures for the month of December.
![image](https://user-images.githubusercontent.com/85171897/141674050-60901761-2751-4abb-b0fb-79c0c35cb825.png)

 
o	In Step 7, convert the December temperatures to a list.
![image](https://user-images.githubusercontent.com/85171897/141674060-57e07bbd-58a8-43c4-aa54-ad57df02bfc5.png)

 
o	In Step 8, create a DataFrame from the list of temperatures for the month of December.
![image](https://user-images.githubusercontent.com/85171897/141674067-6489b1f9-cf18-4569-b282-ea1fe75aa07c.png)

 
•	In Step 9, generate the summary statistics for the December temperatures DataFrame.
 ![image](https://user-images.githubusercontent.com/85171897/141674079-c1b11de6-cd79-4778-8faf-70dfb120ae66.png)

•	After you run Step 9 in your SurfsUp_Challenge.ipynb file, confirm that the summary statistics match the image below
 ![image](https://user-images.githubusercontent.com/85171897/141674095-7135adb5-6e45-4bae-825b-e2d0b9de1170.png)

•	Deliverable 3: A written report for the statistical analysis (README.md)
For this part of the Challenge, write a report that describes the key differences in weather between June and December and two recommendations for further analysis.
The analysis should contain the following:
•	Overview of the analysis: Explain the purpose of this analysis.
o	A client discovered a passion for surfing when visited Hawaii. He planned to return back to Hawaii to live there forever and devise an idea to invest in a surfing and ice cream shop. He needs to create a strong business plan to invest in a shop. One of the investors were concerned about the weather occurring year-round with risk of the business tanking due to being rained out. The client request to run analytics on a data set in the area he wants to open a shop. And long-term plans if the shop on Oahu does well, he may expand to other islands. SQLite Database provided includes the last 12 months of data already loaded. 
o	Goal is to parse the data to retrieve all the temperatures for the month of June and December in Oahu in order to determine if the surf and ice cream shop business is sustainable year-round. 
o	Resources used: Python and Panda library/dataframe; Jupyter notebook for weather analysis; SQLite database where the weather data in flat files to help move more quickly through the analysis; SQLAlchemy to connect to the SQLite database; VS Code to create Flask application and install it; matplotlib dependency allowing to plot data; and GitHub to store the code.
•	Results: Provide a bulleted list with three major points from the two analysis deliverables. Use images as support where needed.
o	Minimum temperature in month of June is roughly 8 degrees higher and the maximum temperature for both months are similar with 2 degrees difference. This tells us the climate change in minimum and maximum temperatures are roughly expected to the be the same based on historical data. 
	June
	Minimum temperature = 64°F
	Maximum temperature = 85°F
	December 
	Minimum temperature = 56°F
	Maximum temperature = 83°F
o	The mean (average) temperature seen in comparison shows June is 75°F (rounded up from 74.9°F) and December is 71°F. On average, the temperature will roughly run in the 70s° for the months of June and December. This is good in ensuring the business will still be making a profit as the climate temperature is still good weather for surfing and customers wanting to eat ice cream. 
o	The count shows the number of times the temperature was observed and is displayed in the panda dataframe and summary statistics. December shows the climate temperature was observed 1,517 times versus June being observed 1,700. This is roughly a 200 count difference that does not have a huge impact on findings. 
o	Panda Dataframe & Summary Statistic
	June
  ![image](https://user-images.githubusercontent.com/85171897/141674114-329b739b-450c-47ff-a4de-02416402303d.png)
![image](https://user-images.githubusercontent.com/85171897/141674117-0fbb5adb-7a84-4e29-9fe1-793225fe5b7e.png)

 
	December
 ![image](https://user-images.githubusercontent.com/85171897/141674120-6a013db8-c9cf-4891-92e3-42367f0b2eb2.png)
![image](https://user-images.githubusercontent.com/85171897/141674124-80c0a4ca-6b6e-4e1c-b3fc-6a9ccc26f0f7.png)
 
•	Summary: Provide a high-level summary of the results and two additional queries that you would perform to gather more weather data for June and December.
o	In summary, there is not a huge difference in climate temperature with June average roughly at 75°F and December average is 71°F (4 degrees difference). Appears the weather around June and December would be good for the business to be successful with surfing clients and demand to eat ice cream. 

o	One query could be written to search and retrieve data to analyze all data columns and rows over a 12 month time period to get a full/complete picture of the average date, prcp, tobs, and station. Using all data available may give an overall picture versus drilling down and parsing out data.
 ![image](https://user-images.githubusercontent.com/85171897/141674149-523d70dc-4656-4814-9096-3fa7fe75bc9a.png)

o	Also run a query for data visualization using matplotlib to plot on a graph to compare the data for the month of June and December easily showing the correlation and differences in climate temperatures.
 ![image](https://user-images.githubusercontent.com/85171897/141674172-05942816-dc3e-436f-841b-89f3386d67c2.png)
 ![image](https://user-images.githubusercontent.com/85171897/141674186-f7630aa1-e74c-4322-8a6c-8b3563095e8d.png)


 
 

![image](https://user-images.githubusercontent.com/85171897/141673994-e235aa3c-ea12-462d-b014-90ef531c227e.png)
