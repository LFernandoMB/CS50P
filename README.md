# CS50P SMART-WALLET
## Created by: Luis Fernando M. Bezerra
### Video Demo:  <youtube>
### Description: 
This project is a proposal for completing the Python CS50 course. The Project searches online for stock data from B3 (Brazilian Stock Exchange), and distributes this data in a simple visualization.

### Problem and Project Proposal:
Currently, to check simple data such as the current price of a share, or the value of the dividend that will be paid for that same share, it is necessary to access a B3 data website, enter the code of the desired share and thus access the data. However, to access more than one action it is necessary to repeat the previous steps for each desired action. This takes time, especially the larger the investor's portfolio.
The project solves this by making this search online, and organizing this data in a dataframe, and making this information available to the end user on a website.
The idea is simple but it fulfills the proposal, and has the potential and openness to grow and improve even more.

# Final Preview
![Mídia1_1](https://github.com/LFernandoMB/CS50P/assets/91624923/fb82e47d-f0a3-4f7b-a492-682a22e60d07)


# Dependencies and Installations

- pip install beautifulsoup4
- pip install requests
- pip install streamlit
- from datetime import datetime
- import csv

# Functions and Features
Functions
- get_data_segmentos:
This function gets the list of stocks to be searched
- get_data_online:
This function takes data from online actions
- save_data:
This function saves the data searched online
- load_data:
This function takes data from csv file and saves it in cache for faster loading

Tests
- test_get_data_segmentos:
Tests the function with the same referent name
- test_get_data_online:
Tests the function with the same referent name
- test_save_data:
Tests the function with the same referent name
