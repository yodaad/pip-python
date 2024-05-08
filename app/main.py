# Description: Main file of the application that runs the program. 
import utils
import charts
import read_csv
import pandas as pd


def run(): 
    
    # Implementation without Pandas library
    """ 
    data = read_csv.read_csv("./data.csv")
    data = list(filter(lambda item: item["Continent"] == "South America", data))
    
    countries = list(map(lambda x: x["Country/Territory"], data))
    percentages = list(map(lambda x: x["World Population Percentage"], data))
    charts.generate_pie_chart(countries, percentages)
    """
    
    # Implementation with Pandas library 
    
    # Read the data from the CSV file 
    df = pd.read_csv("./data.csv")
    
    # Filter the data by the continent 
    df = df[df["Continent"] == "Africa"]
    
    countries = df["Country/Territory"].values
    percentages = df["World Population Percentage"].values
    
    charts.generate_pie_chart(countries, percentages)
    
    data = pd.read_csv("./data.csv")
    country = input("Type country: ").title()
    
    result = utils.population_by_country(data, country)
    
    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(country["Country/Territory"], labels, values)
    
    print(result)


if __name__ == "__main__":
    run()