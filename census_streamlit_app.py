import streamlit as st
import mysql.connector
import pandas as pd

# Initialize mysql connection
mydb = mysql.connector.connect(
    host ="localhost",
    user='root',
    password =""
)

mycursor = mydb.cursor(buffered=True)

st.title("Census Data")

listOfQuestion = [
'What is the total population of each district?',
'How many literate males and females are there in each district?',
'What is the percentage of workers (both male and female) in each district?',
'How many households have access to LPG or PNG as a cooking fuel in each district?',
'What is the religious composition (Hindus, Muslims, Christians, etc.) of each district?',
'How many households have internet access in each district?',
'What is the educational attainment distribution (below primary, primary, middle, secondary, etc.) in each district?',
'How many households have access to various modes of transportation (bicycle, car, radio, television, etc.) in each district?',
'What is the condition of occupied census houses (dilapidated, with separate kitchen, with bathing facility, with latrine facility, etc.) in each district?',
'How is the household size distributed (1 person, 2 persons, 3-5 persons, etc.) in each district?',
'What is the total number of households in each state?',
'How many households have a latrine facility within the premises in each state?',
'What is the average household size in each state?',
'How many households are owned versus rented in each state?',
'What is the distribution of different types of latrine facilities (pit latrine, flush latrine, etc.) in each state?',
'How many households have access to drinking water sources near the premises in each state?',
'What is the average household income distribution in each state based on the power parity categories?',
'What is the percentage of married couples with different household sizes in each state?',
'How many households fall below the poverty line in each state based on the power parity categories?',
'What is the overall literacy rate (percentage of literate population) in each state?']

#dropdown box
option = st.selectbox(
    'select a option to see the data!',
    listOfQuestion,label_visibility='hidden')

#selected Options will be displayed
st.write('You selected: ', option)

#selected option mysql query will executed
if option == listOfQuestion[0]:
    mycursor.execute("select District , Population   from  census_db.census_2011")
if option == listOfQuestion[1]:
    mycursor.execute("select District , Literate_male, Literate_female   from  census_db.census_2011")
if option == listOfQuestion[2]:
    mycursor.execute("select District , round((Workers/Population)*100, 2)  AS `Percentage_of_workers`  from  census_db.census_2011 group by Workers")
if option == listOfQuestion[3]:
    mycursor.execute("select District ,   LPG_or_PNG_Households  from  census_db.census_2011")
if option == listOfQuestion[4]:
    mycursor.execute("select District , sum(hindus+muslims+christians+sikhs+buddhists+jains+others_religions) AS 'Total' from census_db.census_2011 group by District")
if option == listOfQuestion[5]:
    mycursor.execute("select District , Households_with_internet   from  census_db.census_2011")
if option == listOfQuestion[6]:
        mycursor.execute("select District, Below_Primary_Education, Primary_Education, Middle_Education, Secondary_Education, Higher_Education, Graduate_Education, Other_Education from  census_db.census_2011")
if option == listOfQuestion[7]:
    mycursor.execute("select District, Households_with_Bicycle, Households_with_Car_Jeep_Van,  Households_with_Scooter_Motorcycle_Moped from  census_db.census_2011")
if option == listOfQuestion[8]:
    mycursor.execute("select District, Condition_of_occupied_census_houses_Dilapidated_Households, Households_with_separate_kitchen_Cooking_inside_house, Type_of_bathing_facility_Enclosure_without_roof_Households, Not_having_bathing_facility_within_the_premises_Total_Households, Having_latrine_facility_within_the_premises_Total_Households, Type_of_latrine_facility_Pit_latrine_Households, Type_of_latrine_facility_Other_latrine_Households, Type_of_latrine_facility_Night_soil_disposed_into_open_drain, Type_of_latrine_Flush_pour_connected_to_other_system_Households, Not_having_latrine_within_premises_Other_source_Open_Households from  census_db.census_2011")
if option == listOfQuestion[9]:
    mycursor.execute("select District, Household_size_1_person_Households, Household_size_2_persons_Households,Household_size_1_to_2_persons,Household_size_3_persons_Households,Household_size_3_to_5_persons_Households,Household_size_4_persons_Households,Household_size_5_persons_Households,Household_size_6_8_persons_Households,Household_size_9_persons_and_above_Households from  census_db.census_2011")
if option == listOfQuestion[10]:
    mycursor.execute("select State_UT, Households from  census_db.census_2011 group by State_UT")
if option == listOfQuestion[11]:
    mycursor.execute("select State_UT , Having_latrine_facility_within_the_premises_Total_Households from  census_db.census_2011 group by State_UT")
if option == listOfQuestion[12]:
    mycursor.execute("select State_UT , round(avg(Household_size_1_person_Households+Household_size_2_persons_Households+Household_size_1_to_2_persons+Household_size_3_persons_Households+Household_size_3_to_5_persons_Households+Household_size_4_persons_Households+Household_size_5_persons_Households+Household_size_6_8_persons_Households+Household_size_9_persons_and_above_Households),2) as Average_household_size    from  census_db.census_2011 group by State_UT")
if option == listOfQuestion[13]:
    mycursor.execute("select State_UT , Ownership_Rented_Households   from  census_db.census_2011 group by State_UT")
if option == listOfQuestion[14]:
    mycursor.execute("select State_UT ,  Type_of_latrine_facility_Pit_latrine_Households, Type_of_latrine_facility_Other_latrine_Households, Type_of_latrine_facility_Night_soil_disposed_into_open_drain, Type_of_latrine_Flush_pour_connected_to_other_system_Households,Not_having_latrine_within_premises_Other_source_Open_Households,Having_latrine_facility_within_the_premises_Total_Households   from  census_db.census_2011 group by State_UT")
if option == listOfQuestion[15]:
    mycursor.execute("select State_UT ,  Location_of_drinking_water_source_Near_the_premises_Households   from  census_db.census_2011 group by State_UT")
if option == listOfQuestion[16]:
    mycursor.execute("select state_ut , Round(avg(Power_Parity_Less_than_Rs_45000),2) AS Avg_Power_Parity_Less_than_Rs_45000, \
                        Round(avg(Power_Parity_Rs_45000_90000),2) AS Avg_Power_Parity_Rs_4500 ,\
                Round(avg(Power_Parity_Rs_90000_150000),2) AS Avg_Power_Parity_Rs_90000_150000,\
                Round(avg(Power_Parity_Rs_45000_150000),2) AS Avg_Power_Parity_Rs_45000_150000,\
                Round( avg(Power_Parity_Rs_150000_240000),2) AS Avg_Power_Parity_Rs_150000_240000,\
                Round(avg(Power_Parity_Rs_240000_330000),2) AS Avg_Power_Parity_Rs_240000_330000,\
                Round(avg(Power_Parity_Rs_150000_330000),2) AS Avg_Power_Parity_Rs_150000_330000, \
                Round(avg(Power_Parity_Rs_330000_425000),2) AS Avg_Power_Parity_Rs_330000_425000, \
                Round(avg(Power_Parity_Rs_425000_545000),2) AS Avg_Power_Parity_Rs_425000_545000, \
                Round(avg(Power_Parity_Rs_330000_545000),2) AS Avg_Power_Parity_Rs_330000_545000, \
                Round(avg(Power_Parity_Above_Rs_545000),2) AS Avg_Power_Parity_Above_Rs_545000  from  census_db.census_2011 GROUP BY State_UT ")
if option == listOfQuestion[17]:
    mycursor.execute("select state_ut , round(Married_couples_1_Households/Households * 100, 2) as  percentage_of_Married_couples_1_Households, \
                round(Married_couples_2_Households/Households* 100,2) as  percentage_of_Married_couples_2_Households,\
                round(Married_couples_3_Households/Households* 100,2) as percentage_of_Married_couples_3_Households,\
                round(Married_couples_3_or_more_Households/Households* 100,2) as percentage_of_Married_couples_3_or_more_Households,\
                round(Married_couples_4_Households/Households* 100,2) as   percentage_of_Married_couples_4_Households, \
                round(Married_couples_5__Households/Households* 100,2) as percentage_of_Married_couples_5__Households,\
                round(Married_couples_None_Households/Households* 100,2) as percentage_of_Married_couples_None_Households  from  census_db.census_2011 GROUP BY State_UT")
if option == listOfQuestion[18]:
    mycursor.execute("select State_UT , Power_Parity_Less_than_Rs_45000 as Below_the_poverty_line from census_db.census_2011 GROUP BY State_UT")
if option == listOfQuestion[19]:
    mycursor.execute("select State_UT , round(Literate / Population * 100 , 2) as Overall_literacy_rate from census_db.census_2011 GROUP BY State_UT")
#selected option will be displayed in  table form
data = mycursor.fetchall()
field_names = [i[0] for i in mycursor.description]
df = pd.DataFrame(data,columns=field_names)
st.dataframe(df)