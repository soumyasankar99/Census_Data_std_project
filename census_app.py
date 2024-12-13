# Connecting to MySQL server Localhost
import mysql.connector
import streamlit as st
import pandas as pd

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",)

print(mydb)
mycursor = mydb.cursor(buffered=True)

# Function to create a streamlit interface:
def window_fun(window_title,query):
    st.title(window_title)
    mycursor.execute(query)
    out = mycursor.fetchall()
    columns = [i[0] for i in mycursor.description]
    out_df = pd.DataFrame(out, columns = columns)
    st.dataframe(out_df)

# Visualizing the missing Data

def missing_data(file_name):
    st.title('Missing Data Visualization')
    df = pd.read_csv(file_name, index_col=0)
    st.dataframe(df)

# intereface 1 : Total population of each District

def query_1():
    window_fun('Total population of each District',"SELECT District_Code, State_UT, District, Population FROM Census_DB.census_2011")

# interface 2 : Literate male and female in each district

def query_2():
    window_fun('Literate Male and Female in each district', \
            "SELECT District_Code, State_UT, District, Literate_Male, Literate_Female FROM Census_DB.census_2011")

# interface 3 : Percentage of workers in each district

def query_3():
    window_fun('Percentage of Workers in each district',
            "SELECT District_Code, State_UT, District, ROUND((Workers/Population)*100, 2) \
                            AS Percentage_of_Workers FROM Census_DB.census_2011")

# interface 4 : How many households have access to LPG or PNG as a cooking fuel in each district?

def query_4():
    window_fun('Households with LPG or PNG as Cooking fuel',
            "SELECT District_Code, State_UT, District, LPG_or_PNG_Households FROM Census_DB.census_2011")

#interface 5 : What is the religious composition (Hindus, Muslims, Christians, etc.) of each district?

def query_5():
    window_fun("Religious composition of each district (in percentage)",
            "SELECT District_Code, State_UT, District, \
            ROUND((Hindus/Population)*100 , 2) AS Hindus, \
                ROUND((Muslims/Population)*100 , 2) AS Muslims, \
                    ROUND((Christians/Population)*100 , 2) AS Christians, \
                        ROUND((Sikhs/Population)*100 , 2) AS Sikhs, \
                            ROUND((Buddhists/Population)*100 , 2) AS Buddhists, \
                                ROUND((Jains/Population)*100 , 2) AS Jains, \
                                    ROUND((Others_Religions/Population)*100 , 2) AS Other_Religions, \
                                        ROUND((Religion_Not_Stated/Population)*100 , 2) AS Religion_Not_Stated \
                                            FROM Census_DB.Census_2011")    

# interface 6 : How many households have internet access in each district?

def query_6():
    window_fun("Households with Internet in each District", 
            "SELECT District_Code, State_UT, District, Households_with_Internet FROM Census_DB.census_2011")

# interface 7 : What is the educational attainment distribution (below primary, primary, middle, secondary, etc.) in each district?

def query_7():
    window_fun('Educational attainment distribution in each district',
            'SELECT District_Code, State_UT, District, Below_Primary_Education, Primary_Education, Middle_Education, \
                Secondary_Education, Higher_Education, Graduate_Education, Other_Education, Literate_Education, \
                Illiterate_Education, Total_Education FROM Census_DB.Census_2011')

# interface 8 : How many households have access to various modes of transportation (bicycle, car, radio, television, etc.) in each district?

def query_8():
    window_fun('Households with access to various modes of transports in each district', 
            'SELECT District_Code, State_UT, District, Households_with_Bicycle, Households_with_Car_Jeep_Van, \
                Households_with_Radio_Transistor, Households_with_Scooter_Motorcycle_Moped FROM Census_DB.Census_2011')

# interface 9 : What is the condition of occupied census houses (dilapidated, with separate kitchen, with bathing facility, 
#            with latrine facility, etc.) in each district?

def query_9():
    window_fun('Condition of occupied census houses', 
            'SELECT District_Code, State_UT, District, \
            Condition_of_occupied_census_houses_Dilapidated_Households AS Occupied_Dilapidated_Houses, \
            Households_with_separate_kitchen_Cooking_inside_house AS Houses_with_seperate_Kitchen, \
            Having_bathing_facility_Total_Households AS Houses_with_Bathing_facility, \
            Having_latrine_facility_within_the_premises_Total_Households AS Houses_with_Latrine_facility, \
            Not_having_bathing_facility_within_the_premises_Total_Households AS Houses_without_Bathing_facility, \
            Not_having_latrine_within_premises_Other_source_Open_Households AS Houses_without_latrine_facility \
            FROM Census_DB.Census_2011')

# interface 10: How is the household size distributed (1 person, 2 persons, 3-5 persons, etc.) in each district?

def query_10():
    window_fun('Distribution of Household size',
            'SELECT District_Code, State_UT, District, Household_size_1_person_Households AS 1_Person, \
            Household_size_2_persons_Households AS 2_Persons, Household_size_1_to_2_persons AS 1_to_2_Persons, \
            Household_size_3_persons_Households AS 3_Persons, Household_size_4_persons_Households AS 4_Persons, \
            Household_size_5_persons_Households AS 5_Perosns, Household_size_3_to_5_persons_Households AS 3_to_5_Persons, \
            Household_size_6_8_persons_Households AS 6_to_8_Persons, Household_size_9_persons_and_above_Households AS More_than_9_Persons \
            FROM Census_DB.Census_2011')

# interface 11 : What is the total number of households in each state?

def query_11():
    window_fun('Total number of households in each state',
            'SELECT State_UT, SUM(Households) AS Total_Households \
            FROM Census_DB.Census_2011 \
            GROUP BY State_UT')

# interface 12 : How many households have a latrine facility within the premises in each state?

def query_12():
    window_fun('Households having Latrine facility within the premises in each state',
            'SELECT State_UT, \
            SUM(Having_latrine_facility_within_the_premises_Total_Households) AS Households_having_latrine_facility_within_the_premises \
            FROM Census_DB.Census_2011 \
            GROUP BY State_UT')

# interface 13 : What is the average household size in each state?

def query_13():
    window_fun('Average household size in each state',
            'SELECT State_UT, ROUND(AVG(Household_size_1_person_Households), 2) AS Average_of_1_person_houses, \
            ROUND(AVG(Household_size_2_persons_Households), 2) AS Average_of_2_person_houses, \
            ROUND(AVG(Household_size_1_to_2_persons), 2) AS Average_of_1_to_2_person_houses, \
            ROUND(AVG(Household_size_3_persons_Households), 2) AS Average_of_3_person_houses, \
            ROUND(AVG(Household_size_4_persons_Households), 2) AS Average_of_4_person_houses, \
            ROUND(AVG(Household_size_5_persons_Households), 2) AS Average_of_5_person_houses, \
            ROUND(AVG(Household_size_3_to_5_persons_Households), 2) AS Average_of_3_to_5_persons_houses, \
            ROUND(AVG(Household_size_6_8_persons_Households), 2) AS Average_of_6_to_8_persons_houses, \
            ROUND(AVG(Household_size_9_persons_and_above_Households), 2) AS Average_of_9_and_above_persons \
            FROM Census_DB.Census_2011 \
            GROUP BY State_UT')

# interface 14 : How many households are owned versus rented in each state?

def query_14():
    window_fun('Owned versus rented houses in each state',
            'SELECT State_UT, SUM(Ownership_Owned_Households) AS Owned_Houses, SUM(Ownership_Rented_Households) AS Rented_Houses \
            FROM Census_DB.Census_2011 \
            GROUP BY State_UT')

# interface 15 : What is the distribution of different types of latrine facilities (pit latrine, flush latrine, etc.) in each state?

def query_15():
    window_fun('Distribution of different types of latrine facilities in each state',
            'SELECT State_UT, SUM(Type_of_latrine_facility_Pit_latrine_Households) AS Pit_Latrine, \
            SUM(Type_of_latrine_facility_Night_soil_disposed_into_open_drain) AS Night_soil_disposed_into_open_drain_Latrine, \
            SUM(Type_of_latrine_Flush_pour_connected_to_other_system_Households) AS Flush_or_Pour_Latrine, \
            SUM(Type_of_latrine_facility_Other_latrine_Households) AS Other_Latrine_types \
            FROM Census_DB.Census_2011 \
            GROUP BY State_UT')

# interface 16 : How many households have access to drinking water sources near the premises in each state?

def query_16():
    window_fun('Houeholds with drinking water sources near the premises in each state',
            'SELECT State_UT, \
            SUM(Location_of_drinking_water_source_Near_the_premises_Households) AS Households_with_drinking_water_source_Near_the_premises \
            FROM Census_DB.Census_2011 \
            GROUP BY State_UT')

# interface 17 : What is the average household income distribution in each state based on the power parity categories?

def query_17():
    window_fun('Average household income distribution in each state based on the power parity categories',
            'SELECT State_UT, ROUND(AVG(Power_Parity_Less_than_Rs_45000), 2) AS Avg_Power_Parity_Less_than_Rs_45000, \
            ROUND(AVG(Power_Parity_Rs_45000_90000), 2) AS Avg_Power_Parity_Rs_45000_90000, \
            ROUND(AVG(Power_Parity_Rs_90000_150000), 2) AS Avg_Power_Parity_Rs_90000_150000, \
            ROUND(AVG(Power_Parity_Rs_45000_150000), 2) AS Avg_Power_Parity_Rs_45000_150000, \
            ROUND(AVG(Power_Parity_Rs_150000_240000), 2) AS Avg_Power_Parity_Rs_150000_240000, \
            ROUND(AVG(Power_Parity_Rs_240000_330000), 2) AS Avg_Power_Parity_Rs_240000_330000, \
            ROUND(AVG(Power_Parity_Rs_150000_330000), 2) AS Avg_Power_Parity_Rs_150000_330000, \
            ROUND(AVG(Power_Parity_Rs_330000_425000), 2) AS Avg_Power_Parity_Rs_330000_425000, \
            ROUND(AVG(Power_Parity_Rs_425000_545000), 2) AS Avg_Power_Parity_Rs_425000_545000, \
            ROUND(AVG(Power_Parity_Rs_330000_545000), 2) AS Avg_Power_Parity_Rs_330000_545000, \
            ROUND(AVG(Power_Parity_Above_Rs_545000), 2) AS Avg_Power_Parity_Above_Rs_545000 \
            FROM Census_DB.Census_2011 \
            GROUP BY State_UT')

# interface 18 : What is the percentage of married couples with different household sizes in each state?

def query_18():
    window_fun('Percentage of married couples with different household sizes in each state',
            'SELECT State_UT, \
            ROUND(SUM(Married_couples_1_Households)/SUM(Population) * 100, 2) AS Percentage_of_Married_couples_1_Households, \
            ROUND(SUM(Married_couples_2_Households)/SUM(Population) * 100, 2) AS Percentage_of_Married_couples_2_Households, \
            ROUND(SUM(Married_couples_3_Households)/SUM(Population) * 100, 2) AS Percentage_of_Married_couples_3_Households, \
            ROUND(SUM(Married_couples_3_or_more_Households)/SUM(Population) * 100, 2) AS Percentage_of_Married_couples_3_or_more_Households, \
            ROUND(SUM(Married_couples_4_Households)/SUM(Population) * 100, 2) AS Percentage_of_Married_couples_4_Households, \
            ROUND(SUM(Married_couples_5__Households)/SUM(Population) * 100, 2) AS Percentage_of_Married_couples_5__Households, \
            ROUND(SUM(Married_couples_None_Households)/SUM(Population) * 100, 2) AS Percentage_of_Married_couples_None_Households \
            FROM Census_DB.Census_2011 \
            GROUP BY State_UT')

# interface 19 : How many households fall below the poverty line in each state based on the power parity categories?

def query_19():
    window_fun('Households below the poverty line in each state',
            'SELECT State_UT, SUM(Power_Parity_Less_than_Rs_45000) AS Households_below_poverty_line FROM Census_DB.Census_2011 \
            GROUP BY State_UT')

# interface 20 : What is the overall literacy rate (percentage of literate population) in each state?

def query_20():
    window_fun('Overall literacy rate of each state',
            'SELECT State_UT, \
            ROUND(SUM(Literate)/SUM(Population) * 100, 2) AS Percentage_of_Literacy \
            FROM Census_DB.Census_2011 \
            GROUP BY State_UT')

# Main window

def main():
    st.title("Census 2011 : Insights")
    options = ['Missing Data Visualization', 'Total population of each District', 'Literate Male and Female in each district',
                'Percentage of Workers in each district', 'Households with LPG or PNG as Cooking fuel',
                'Religious composition of each district (in percentage)', 'Households with Internet in each District',
                'Educational attainment distribution in each district',
                'Households with access to various modes of transports in each district', 'Condition of occupied census houses',
                'Distribution of Household size', 'Total number of households in each state', 
                'Households having Latrine facility within the premises in each state', 'Average household size in each state',
                'Owned versus rented houses in each state', 'Distribution of different types of latrine facilities in each state',
                'Houeholds with drinking water sources near the premises in each state',
                'Average household income distribution in each state based on the power parity categories',
                'Percentage of married couples with different household sizes in each state',
                'Households below the poverty line in each state', 'Overall literacy rate of each state']

    select = st.selectbox("Please select a topic to display :",options = options, index = None, placeholder = 'Choose an option')
    if select == 'Missing Data Visualization':
        missing_data('missing_data.csv')
    elif select == 'Total population of each District':
        query_1()
    elif select == 'Literate Male and Female in each district':
        query_2()
    elif select == 'Percentage of Workers in each district':
        query_3()
    elif select == 'Households with LPG or PNG as Cooking fuel':
        query_4()
    elif select == 'Religious composition of each district (in percentage)':
        query_5()
    elif select == 'Households with Internet in each District':
        query_6()
    elif select == 'Educational attainment distribution in each district':
        query_7()
    elif select == 'Households with access to various modes of transports in each district':
        query_8()
    elif select == 'Condition of occupied census houses':
        query_9()
    elif select == 'Distribution of Household size':
        query_10()
    elif select == 'Total number of households in each state':
        query_11()
    elif select == 'Households having Latrine facility within the premises in each state':
        query_12()
    elif select == 'Average household size in each state':
        query_13()
    elif select == 'Owned versus rented houses in each state':
        query_14()
    elif select == 'Distribution of different types of latrine facilities in each state':
        query_15()
    elif select == 'Houeholds with drinking water sources near the premises in each state':
        query_16()
    elif select == 'Average household income distribution in each state based on the power parity categories':
        query_17()
    elif select == 'Percentage of married couples with different household sizes in each state':
        query_18()
    elif select == 'Households below the poverty line in each state':
        query_19()
    elif select == 'Overall literacy rate of each state':
        query_20()
    else:
        st.write(f"Your selected query will be displayed. Current selection : {select}")

main()