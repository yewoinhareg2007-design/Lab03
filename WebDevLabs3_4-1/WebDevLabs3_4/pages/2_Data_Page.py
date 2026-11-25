# Lab 3: API data page
# TODO: Rename this file to fit your page. Keep the number at the front, since it sets the
#       page's order in the sidebar (for example, 2_Pokedex.py).
#
# This page shows data from your API, processed with your own Python code. No AI on this page.
# It should have:
#   - at least 2 meaningful user inputs (for example st.selectbox, st.text_input, st.slider)
#   - at least 2 dynamic visuals that change based on the user's input: charts, displays of
#     images, or other visualizations (see the example website for examples!)
 
import requests
import streamlit as st
import pandas as pd
 
def incidence_by_ethnicity():
    ethnicities =  ["Asian or Pacific Islander, non-Hispanic", "White, non-Hispanic", "Black, non-Hispanic", "Hispanic", "American Indian or Alaska Native, non-Hispanic"]
    ethnicity = st.multiselect(
            "Choose an ethnicity:",
            ethnicities,
            default=["Asian or Pacific Islander, non-Hispanic"])    
    response = requests.get(f"https://data.cdc.gov/resource/hksd-2xuw.json?topic=Cancer&locationabbr=US&question=Invasive%20cancer%20(all%20sites%20combined)%2C%20incidence&datavaluetype=Number%22")
    data = response.json()
    st.subheader(f"Cancer Incidence Data for {ethnicity} people in the US")  
    ethnicity_in_graph = []
    for item in data:
        try:
            if item["stratification1"] in ethnicity:
                ethnicity_in_graph.append(item)     
        except KeyError:
            continue
    if len(ethnicity_in_graph) > 0:
        df = pd.DataFrame(ethnicity_in_graph)
        df["datavalue"] = pd.to_numeric(df["datavalue"], errors="coerce")
        df = df.dropna(subset=["datavalue"])
        st.bar_chart(df, x="stratification1", y="datavalue")
    else:
        st.write('No data available')
incidence_by_ethnicity()
 
st.write ("---")
 
state_abbr = ""
state_chosen = ""
 
def choose_state():
    global state_abbr
    global state_chosen
    states = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY"
    }
    state_chosen = st.selectbox("Choose a state:", list(states.keys()))
    state_abbr = states[state_chosen]
    st.subheader(f"Cancer Incidence Data for {state_chosen}")
    response = requests.get(f"https://data.cdc.gov/resource/hksd-2xuw.json?topic=Cancer&locationabbr={state_abbr}&question=Invasive%20cancer%20(all%20sites%20combined)%2C%20incidence&datavaluetype=Number")
    data = response.json()
    totals = {}
    for item in data:
        try:
            yearstart = item["yearstart"]
            yearend = item["yearend"]
            datavalue = float(item["datavalue"])
            timeFrame = (yearstart, yearend)
            if timeFrame not in totals:
                totals[timeFrame] = datavalue
            else:
                totals[timeFrame] += datavalue
        except KeyError:
            st.write("Data for this item is incomplete.")
    for timeFrame in totals:
        st.write(f"From {timeFrame[0]} to {timeFrame[1]}, there was a total of {totals[timeFrame]} cases of cancer recorded in {state_chosen}.")
    return data
choose_state()
 
st.write ("---")
 
def incidence_by_sex():
    sexes = ["Male", "Female"]
    sex_chosen = st.selectbox("Choose a sex:", list(sexes))
    st.subheader(f"Cancer Incidence Data for {sex_chosen}s in {state_chosen}")
    if sex_chosen == "Male":
        st.image("images/Males.jpg", width=200)
    if sex_chosen == "Female":
        st.image("images/Females.jpg", width=200)
    response = requests.get(f"https://data.cdc.gov/resource/hksd-2xuw.json?topic=Cancer&locationabbr={state_abbr}&question=Invasive%20cancer%20(all%20sites%20combined)%2C%20incidence&datavaluetype=Number")
    data = response.json()
    totals = {}
    for item in data:
        try:
            yearstart = item["yearstart"]
            yearend = item["yearend"]
            datavalue = float(item["datavalue"])
            timeFrame = (yearstart, yearend)
            if timeFrame not in totals:
                totals[timeFrame] = datavalue
            else:
                totals[timeFrame] += datavalue
        except KeyError:
            st.write("Data for this item is incomplete.")
    for timeFrame in totals:
        st.write(f"From {timeFrame[0]} to {timeFrame[1]}, there was a total of {totals[timeFrame]} cases of cancer recorded in {sex_chosen}s in {state_chosen}.")
incidence_by_sex()
