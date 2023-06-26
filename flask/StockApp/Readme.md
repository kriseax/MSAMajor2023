# Stock Visualizer Challenge

You will create a python application that queries the Alpha Vantage api, and allows the user to select a date range to view the data, and the type of chart they want to view the data in.

## Requirements

The application should:

- Ask the user to enter the stock symbol for the company they want data for.
- Ask the user for the chart type they would like.
- Ask the user for the time series function they want the api to use.
- Ask the user for the beginning date in YYYY-MM-DD format.
- Ask the user for the end date in YYYY-MM-DD format.
  - The end date should not be before the begin date
- Generate a graph and open in the user’s default browser. 

## Sample Output
[Stock Visualizer](https://umsystem.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=194ebeed-9c7d-4ae9-afb6-b02d00e28272)

The graphing module used in the demo is called pygal. Here is a link to the [Pygal Documentation](https://www.pygal.org/en/stable/documentation/index.html)
