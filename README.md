# bike-share-optimization
Data Visualization for bike share data in Los Angeles 
Submission for **Capital One Software Engineering Summit**.

[Live Preview!](https://vsinghai.github.io/bike-share-optimization/)

## Contents
- [Stack Outline](#stack-outline)
- [Strategy](#strategy)
- [Bonuses](#bonuses)

## Stack outline
**Front End**
* Deployed on Github Pages
* jQuery + AJAX
* Google Maps API
* [Chart.Js](http://www.chartjs.org/)
* [Canvas.Js](https://canvasjs.com/)
* [amCharts.Js](https://www.amcharts.com/)

**Back End**
* Parsed using Python 
  * [CSV](https://docs.python.org/3/library/csv.html)
  * [Pandas](https://pandas.pydata.org/)
  * [Collections](https://docs.python.org/2/library/collections.html)

## Strategy
### 1. Visualize the data:
* **Popular Destinations vs. Time of Year**
* **Yearly Heat Map**
* **Seasonal Heat Map**
	* If I was to look where the most popular stations were in order to be guarenteed a bike in Los Angeles, I would go to the places in high demand first. Furthermore, can assess in a seasonal mindset.

### 2. Heat Map:
Filter out the NaN, empty string, null, and 0 values from the data

**Inputs:** Starting/Ending Station Latitude, Starting/Ending Station Longitude, 

**Output:** Heat Map made in python, exported as an HTML file

**Strategy:**
1. Filter data that didn't incorporate lat's or long's
2. Filter data down to seasonal values


## Data Visualizations
### 1. Heat Map
* **Heat Map for Yearly and Seasonal Data 
### 2. Popular Passes
* **What types of passes are used yearly and seasonal
### 3. Starting Stations
* **Top 10 Starting Stations Listed
  * Bar Graph: Top 10 Starting Station with Station ID and # of visits listed
  * Pin Points: Pin Pointed the 10 Stations on Google Maps (If marker is clicked, shows popularity # followed by Station ID)
### 4. Ending Stations
* **Top 10 Starting Stations Listed
  * Bar Graph: Top 10 Ending Station with Station ID and # of visits listed
  * Pin Points: Pin Pointed the 10 Stations on Google Maps (If marker is clicked, shows popularity # followed by Station ID)
### 5. Time and Distance
* ** Visually appealing way of showing average time and distance on a yearly and seasonal basis to viewers
  * Full Interaction
  
## Creativity
**Animate:** Add an animation to your visualization.
* First data visualization graph expands from the bottom up.
* Other data visualization maps are interactive.

