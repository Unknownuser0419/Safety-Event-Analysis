import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
import plotly.graph_objects as go
import streamlit as st
import re
import string

st.title("Hello world!")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
  data = pd.read_excel(uploaded_file)
  st.write(data)

  data['Date']=data['Date of Event'].dt.strftime('%Y-%m-%d')
  new=data[['Date','Sub Area','Event Title','Event Description','Classification','Likelihood','HLVE','CS \ Risk Categories','Type']]
  new['Likelihood'].fillna(new['Likelihood'].mode()[0],inplace=True)
  
  
  
  new['CS \\ Risk Categories'].fillna(new['CS \\ Risk Categories'].mode()[0],inplace=True)
  
  
  
  new.isna().sum()
  
  
  
  from bs4 import BeautifulSoup
  
  
  # In[12]:
  
  
  def remove_html_tags(text):
      soup=BeautifulSoup(text,'lxml')
      stripped_text=soup.get_text()
      return stripped_text
  
  
  
  new['Clean_Discription']=new['Event Description'].apply(remove_html_tags)
  
  
  new['Event']=new['Event Title']
  
  
  
  new.drop(['Event Title','Event Description'],axis=1,inplace=True)
  
  
  # In[19]:
  
  
  def standardize_person_tripped(text):
      pattern = re.compile(r'.*person.*tripped.*', re.IGNORECASE)
      if pattern.match(text):
          return 'Person got Tripped'
      else:
          return text
  
  
  # In[20]:
  
  
  def standardize_super_line_leak(text):
      pattern = re.compile(r'.*IW.*SPUR.*LINE.*LEAK.*', re.IGNORECASE)
      if pattern.match(text):
          return 'Super Line Leak'
      else:
          return text
  
  
  # In[21]:
  
  
  def standardize_super_line_leak(text):
      pattern = re.compile(r'.*IW.*SPUR.*LINE.*LEAK.*', re.IGNORECASE)
      if pattern.match(text):
          return 'Super Line Leak'
      else:
          return text
  
  
  # In[22]:
  
  
  def standardize_dropped_object(text):
      if text.lower() == 'dropped object':
          return 'Dropped Object'
      else:
          return text
  
  
  
  # In[24]:
  
  
  def normalize_leakage(phrase):
      if re.search(r'24\s*(INCH)?\s*PF', phrase, re.IGNORECASE) and re.search(r'leak(age)?', phrase, re.IGNORECASE):
          return '24 INCH PF'
      return phrase
  
  
  # In[25]:
  
  
  def standardize_slip_and_trip(text):
      pattern = re.compile(r'.*(slip|trip).*fall.*', re.IGNORECASE)
      if pattern.match(text):
          return 'Slip and Trip'
      else:
          return text
  
  
  # In[26]:
  
  
  def standardize_polymer_line_leaked(text):
      pattern = re.compile(r'.*polymer.*line.*leak.*', re.IGNORECASE)
      if pattern.match(text):
          return 'Polymer Line Leaked'
      else:
          return text
  
  
  # In[27]:
  
  
  def standardize_polymer_leak_observed(text):
      pattern = re.compile(r'.*polymer.*leak.*observed.*', re.IGNORECASE)
      if pattern.match(text):
          return 'Polymer Leak Observed'
      else:
          return text
  
  
  # In[28]:
  
  
  def standardize_slip_and_fall(text):
      pattern = re.compile(r'slip\s*&?\s*(?:and\s*)?fall\s*(hazard[s]?|s)?', re.IGNORECASE)
      standardized_text = pattern.sub('Slip and Fall', text)
      return standardized_text
  
  
  # In[29]:
  
  
  def standardize_trip_hazard(text):
      if 'trip hazard' in text.lower():
          return 'Trip Hazard'
      else:
          return text
  
  
  # In[30]:
  
  
  def normalize_near_miss(phrase):
      if re.search(r'\bnear miss\b', phrase, re.IGNORECASE):
          return 'Near Miss'
      return phrase
  
  
  # In[31]:
  
  
  def standardize_trip_fall(phrase):
      if re.search(r'\btrip\b.*\bfall', phrase, re.IGNORECASE) or re.search(r'\btrip\b', phrase, re.IGNORECASE):
          return 'Trip and Fall'
      return phrase
  
  
  # In[32]:
  
  
  def normalize_honey_bee_incidents(phrase):
      if re.search(r'\b(honey bee)\b', phrase, re.IGNORECASE):
          if re.search(r'(bite|stung|attack|near miss)', phrase, re.IGNORECASE):
              return 'Honey Bee Incident'
      return phrase
  
  
  # In[33]:
  
  
  def normalize_honey_bee_incidents(phrase):
      if re.search(r'\b(honey bee)\b', phrase, re.IGNORECASE):
          if re.search(r'(bite|stung|attack|near miss)', phrase, re.IGNORECASE):
              return 'Honey Bee Incident'
      return phrase
  
  
  # In[34]:
  
  
  def standardize_water_leakage(text):
      if 'water leak' in text.lower() or 'water leakage' in text.lower():
          return 'Water Leakage'
      elif 'injection water' in text.lower() or 'injection water line' in text.lower() or 'polymerized water injection' in text.lower():
          return 'Water Leakage'
      else:
          return text
  
  
  # In[35]:
  
  
  def standardize_pipeline_leak(text):
      if 'pipeline leak' in text.lower():
          return 'Pipeline Leak'
      else:
          return text


# In[36]:


def standardize_underground_line_leak(text):
    if 'iw line leak' in text.lower() or 'iw underground line leak' in text.lower() or 'iw u/g line leak' in text.lower():
        return 'Underground Line Leak'
    else:
        return text


# In[37]:


def standardize_lifting_operations(text):
    if 'lifting' in text.lower():
        return 'Lifting Operations'
    elif 'crane lifting operation' in text.lower():
        return 'Lifting Operations'
    elif 'unsafe lifting operation' in text.lower():
        return 'Lifting Operations'
    else:
        return text


# In[38]:


def standardize_first_aid_case(text):
    if 'first aid' in text.lower() or 'first aid case' in text.lower():
        return 'First Aid Case'
    else:
        return text


# In[39]:


def standardize_production_fluid_line_leak(text):
    pattern = re.compile(r'.*production.*fluid.*line.*leak.*', re.IGNORECASE)
    if pattern.match(text):
        return 'Production Fluid Line Leak'
    else:
        return text


# In[40]:


def standardize_possible_injury(text):
    if 'possible head injury' in text.lower():
        return 'Possible Injury'
    else:
        return text


# In[41]:


new['Event']=new['Event'].apply(standardize_person_tripped)


# In[42]:


new['Event']=new['Event'].apply(standardize_super_line_leak)


# In[43]:


new['Event']=new['Event'].apply(standardize_production_fluid_line_leak)


# In[44]:


new['Event']=new['Event'].apply(standardize_dropped_object)


# In[45]:


new['Event']=new['Event'].apply(standardize_slip_and_fall)


# In[46]:


new['Event']=new['Event'].apply(standardize_trip_hazard)


# In[47]:


new['Event']=new['Event'].apply(standardize_trip_fall)


# In[48]:


new['Event']=new['Event'].apply(normalize_near_miss)


# In[49]:


new['Event']=new['Event'].apply(normalize_honey_bee_incidents)


# In[50]:


new['Event']=new['Event'].apply(standardize_possible_injury)


# In[51]:


new['Event']=new['Event'].apply(standardize_water_leakage)


# In[52]:


new['Event']=new['Event'].apply(standardize_pipeline_leak)


# In[53]:


new['Event']=new['Event'].apply(standardize_underground_line_leak)


# In[54]:


new['Event']=new['Event'].apply(standardize_pipeline_leak)


# In[55]:


new['Event']=new['Event'].apply(standardize_lifting_operations)


# In[56]:


new['Event']=new['Event'].apply(standardize_first_aid_case)


# In[57]:


new['Event']=new['Event'].apply(standardize_slip_and_fall)


# In[58]:


new['Event']=new['Event'].apply(standardize_pipeline_leak)


# In[59]:


new['Event']=new['Event'].apply(standardize_underground_line_leak)


# Group the DataFrame by 'Date' and 'Type', and count the number of occurrences of each type
incident_counts = new.groupby(['Date', 'Type']).size().unstack(fill_value=0).reset_index()

# Rename the columns for clarity
incident_counts.rename(columns={'Incident': 'Incident Count', 'Near Miss': 'Near Miss Count'}, inplace=True)

# Merge the counts back into the original DataFrame based on 'Date'
df = pd.merge(new, incident_counts, on='Date', how='left')

# For 'Near Miss' rows, set 'Incident Count' to 0
df.loc[df['Type'] == 'Near Miss', 'Incident Count'] = 0

# For 'Incident' rows, set 'Near Miss Count' to 0
df.loc[df['Type'] == 'Incident', 'Near Miss Count'] = 0



replace_dict = {                           
'Environment - CAT-2 (Minor)'  :  'Environment',      
'Environment - CAT-1 (Negligible)' : 'Environment' ,      
'Safety - CAT-2 (Minor)' :  'Safety' ,                                      
'Safety - CAT-1 (Negligible)' :   'Saftey' ,     
'Safety - CAT-3 (Moderate)' :      'Saftey',      
'Safety - HIPO' :'Saftey'

}
for word, replacement in replace_dict.items():
    original_string = df['Classification'].replace(word, replacement,inplace=True)


# In[64]:


pattern = r'^(Fall of Ground \(Mines\))\|.*$'
df['CS \\ Risk Categories'] = [re.sub(pattern, r'\1', item) for item in df['CS \\ Risk Categories']]


# In[65]:


patter_dict={'Lifting & Shifting of equipment & material|Others': 'Lifting & Shifting of equipment',
'Lift Standard|Lifting & Shifting of equipment & material': 'Lifting & Shifting of equipment',
'Lifting & Shifting of equipment & material|Slip/ trip/ Fall|Fall of material/ Object' :'Lifting & Shifting of equipment',
'Lifting & Shifting of equipment & material|Scaffolding System':'Lifting & Shifting of equipment',
'Lifting & Shifting of equipment & material|Material Handling':'Lifting & Shifting of equipment',
'Lifting & Shifting of equipment & material':'Lifting & Shifting of equipment'}


for word, replacement in patter_dict.items():
    original_string = df['CS \\ Risk Categories'].replace(word, replacement,inplace=True)


# In[66]:


Plant_dict={
'Plant Upkeep|Property':'Plant Upkee',
'Plant Upkeep|Execution, Delivery, and Process|Skills and knowledge':'Plant Upkee',
'Plant Upkeep|Damage to physical assets': 'Plant Upkee',
'Plant Upkeep|Animal/ Insect bite':'Plant Upkee',
'Plant Upkeep':'Plant Upkee'
}
for word, replacement in Plant_dict.items():
    original_string = df['CS \\ Risk Categories'].replace(word, replacement,inplace=True)


# In[67]:


Tool_Dict={'Tools and Equipment|Hazardous Gases like CO etc':'Tools and Equipment',
'Tools and Equipment|Work Environment|Heat exposure':'Tools and Equipment',
'Tools and Equipment|Damage to physical assets':'Tools and Equipment',
'Tools and Equipment|Fall of material/ Object':'Tools and Equipment', 
'Tools and Equipment|Fall of material/ Object':'Tools and Equipment',
'Tools and Equipment|Slip/ trip/ Fall' :'Tools and Equipment', 
'Tools and Equipment|Execution':'Tools and Equipment',
'Tools and Equipment|Execution, Delivery, and Process':'Tools and Equipment'}

for word, replacement in Tool_Dict.items():
    original_string = df['CS \\ Risk Categories'].replace(word, replacement,inplace=True)

    


# In[68]:


df['CS \\ Risk Categories'].replace('Inflow and Inundation of liquids|Effluent / Process liquids','Inflow and Inundation of liquids',inplace=True) 


# In[69]:


Within_Dict={
    'Within Plant|Chemical Storage & Handling':'Within Plant',
    'Within Plant|Plant Upkeep|Slip/ trip/ Fall':'Within Plant',
    'Within Plant|Fire Safety':'Within Plant',
    'Within Plant|Hazardous waste':'Within Plant',
'Within Plant|High Volume Low toxicity waste' :'Within Plant'
}

for word, replacement in Within_Dict.items():
    original_string = df['CS \\ Risk Categories'].replace(word, replacement,inplace=True)


# In[70]:


EF_Dict={'Outside Plant|Effluent / Process liquids|Water':'Effluent / Process liquids',
'Effluent / Process liquids|Water':'Effluent / Process liquids',
'Effluent / Process liquids|Non Hazardous waste' :'Effluent / Process liquids',
'Effluent / Process liquids|Slip/ trip/ Fall' :'Effluent / Process liquids',
'Effluent / Process liquids|Liquid Chemicals' :'Effluent / Process liquids'
     }

for word, replacement in EF_Dict.items():
    original_string = df['CS \\ Risk Categories'].replace(word, replacement,inplace=True)


# In[71]:


Mat_Dic={
    'Material Handling|Tools and Equipment|Fall of material/ Object':'Material Handling',
       'Material Handling|Quality':'Material Handling',
     'Material Handling|Slip/ trip/ Fall':'Material Handling',
         'Material Handling|Tools and Equipment':'Material Handling'
}

for word, replacement in Mat_Dic.items():
    original_string = df['CS \\ Risk Categories'].replace(word, replacement,inplace=True)


# In[72]:


Vehi_Dict={'Vehicle & Driving|Work Environment':" Vehicle & Driving",
'Vehicle & Driving|Slip/ trip/ Fall':" Vehicle & Driving",
'Vehicle & Driving|Property':" Vehicle & Driving"
          }


for word, replacement in Vehi_Dict.items():
    original_string = df['CS \\ Risk Categories'].replace(word, replacement,inplace=True)


# In[73]:


Elect_Dict={'Electrical Safety|Fire Safety|Permit to work':'Electrical Safety',
       'Electrical Safety|Lifting & Shifting of equipment & material':'Electrical Safety',
    'Electrical Safety|Others':'Electrical Safety',
     'Electrical Safety|Water':'Electrical Safety',
        'Electrical Safety|Fall of Ground (Mines)':'Electrical Safety'}
for word, replacement in Elect_Dict.items():
    original_string = df['CS \\ Risk Categories'].replace(word, replacement,inplace=True)


# In[74]:


df['Incident Count'].sum()


# In[75]:


df['CS \\ Risk Categories']=df['CS \\ Risk Categories'].apply(lambda x: 'Fall of Ground (Mines)' if 'Fall of Ground (Mines)' in x else x)


# In[76]:


df['CS \\ Risk Categories']=df['CS \\ Risk Categories'].apply(lambda x: 'Electrical Safety' if 'Electrical Safety' in x else x)


# In[77]:


df['Classification'].replace('Saftey', 'Safety',inplace=True)


# In[78]:


df['CS \\ Risk Categories'].nunique()


# In[79]:


def remove_x(text):
    return text.replace('x', '')


# In[80]:


df['Clean_Discription']=df['Clean_Discription'].apply(remove_x)

df.drop_duplicates(inplace=True)



df.info()


# In[83]:


df['Date'].sort_values()


# In[84]:


df['Date'] = pd.to_datetime(df['Date'])

df['Week_of_Year'] = df['Date'].dt.strftime('%Y-%U')
df['Day_of_Week'] = df['Date'].dt.day_name()

day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
incidents_by_weekday = df.groupby(['Week_of_Year', 'Day_of_Week']).size().unstack().reindex(columns=day_order).fillna(0)

# plt.figure(figsize=(15, 13))
# sns.heatmap(incidents_by_weekday, cmap='Blues', annot=True, fmt='g', linewidths=.5, linecolor='lightgrey')
# plt.xlabel('Day of the Week')
# plt.ylabel('Week of the Year')
# plt.title('Incidents by Week and Weekday')
# plt.xticks(rotation=45) 
# plt.tight_layout()
# plt.show()




df.rename(columns={'Incident Count':'Incident','Near Miss Count':'Near Miss'},inplace=True)


# In[86]:


df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.strftime('%Y-%m')
df['Day_of_Week'] = df['Date'].dt.day_name()

day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

incidents_by_weekday = df.groupby(['Month', 'Day_of_Week'])['Incident'].sum().unstack().fillna(0)
incidents_by_weekday = incidents_by_weekday[day_order]


# plt.figure(figsize=(12, 8))
# sns.heatmap(incidents_by_weekday, cmap='YlOrRd', annot=True, fmt='g', linewidths=.5, linecolor='lightgrey')
# plt.xlabel('Day of the Week')
# plt.ylabel('Month')
# plt.title('Incidents by Month and Weekday')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()



total_incidents_monday = incidents_by_weekday['Monday'].sum()
print("Total incidents on Tuesday:", total_incidents_monday)


# In[88]:


import plotly.express as px


# In[89]:


df['Date'] = pd.to_datetime(df['Date'])
df['Day_of_Week'] = df['Date'].dt.day_name()
incidents_by_day = df.groupby('Day_of_Week')['Incident'].sum()

days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
incidents_by_day = incidents_by_day.reindex(days_order)

# Create a DataFrame for Plotly
incidents_by_day_df = pd.DataFrame({'Day_of_Week': incidents_by_day.index, 'Number_of_Incidents': incidents_by_day.values})

# # Create a bar chart using Plotly Express
# fig = px.bar(incidents_by_day_df, 
#              x='Day_of_Week', 
#              y='Number_of_Incidents', 
#              title='Incidents by Day of the Week',
#              labels={'Day_of_Week': 'Day of the Week', 'Number_of_Incidents': 'Number of Incidents'},
#              color='Day_of_Week',  # Color the bars by day of the week
#              color_discrete_sequence=px.colors.qualitative.Vivid)  # Choose a vivid color palette

# # Update layout for better readability
# fig.update_layout(
#     xaxis_title='Day of the Week',
#     yaxis_title='Number of Incidents',
#     title_x=0.5,  # Center the title
#     plot_bgcolor='white',  # Set the background to white for a cleaner look
#     xaxis_tickangle=-45  # Angle the x-axis labels for better visibility
# )

# # Show the plot
# fig.show()


# In[90]:


# Convert 'Event Date' to datetime
df['Event Date'] = pd.to_datetime(data['Event Date'])

# Extract the time
df['Event Time'] = df['Event Date'].dt.time

print(df['Event Time'])


# In[91]:


df['Event Time'].fillna(df['Event Time'].mode()[0],inplace=True)


# In[92]:


df.drop('Event Date',axis=1,inplace=True)


# In[93]:


from datetime import time


# In[94]:


def assign_shift(t):
    if time(6, 0) <= t < time(14, 0):
        return 'Shift 1 (6AM-2PM)'
    elif time(14, 0) <= t < time(22, 0):
        return 'Shift 2 (2PM-10PM)'
    else:
        return 'Shift 3 (10PM-6AM)'

# Assuming df['Event Time'] is already filled and in the correct format (time objects)
df['Shift'] = df['Event Time'].apply(assign_shift)


# In[95]:


shift_counts = df['Shift'].value_counts()


# In[96]:


# if isinstance(shift_counts, pd.Series):
#     shift_counts_df = shift_counts.reset_index()
#     shift_counts_df.columns = ['Shift', 'Number_of_Incidents']
# else:
#     shift_counts_df = shift_counts

# # Create a bar chart using Plotly Express
# fig = px.bar(shift_counts_df, 
#              x='Shift', 
#              y='Number_of_Incidents', 
#              title='Number of Incidents by Shift',
#              labels={'Number_of_Incidents': 'Number of Incidents', 'Shift': 'Shift'},
#              color='Shift',  # This uses the shift column to color the bars differently
#              color_continuous_scale=px.colors.sequential.Viridis,  # Optional: use a color scale
#              template='plotly_white')  # Use a white background for a clean look

# # Update layout for better readability
# fig.update_layout(
#     xaxis_title='Shift',
#     yaxis_title='Number of Incidents',
#     title_x=0.5,  # Center the title
#     plot_bgcolor='white'  # Ensure the background color is white
# )

# # Show the plot
# fig.show()


# In[97]:


monthly_shift_counts = df.groupby(['Month', 'Shift']).size().unstack(fill_value=0)
monthly_shift_counts = monthly_shift_counts.reset_index()
monthly_shift_counts_melted = monthly_shift_counts.melt(id_vars='Month', var_name='Shift', value_name='Number of Incidents')


# In[119]:


# fig = px.bar(monthly_shift_counts_melted, x='Month', y='Number of Incidents', color='Shift',
#              barmode='stack', labels={'Date': 'Month', 'Number of Incidents': 'Number of Incidents'},
#              title='Stacked Number of Incidents by Shift and Month')

# # fig.update_layout(
#     title={'text': 'Stacked Number of Incidents by Shift and Month', 'font': {'size': 20}, 'x': 0.5},
#     xaxis_title='Month',
#     yaxis_title='Total Number of Incidents',
#     xaxis=dict(
#         tickmode='linear', 
#         tick0=0,  
#         dtick=1,  
#         tickangle=-45, 
#         type='category' 
#     ),
#     legend_title='Shift',
#     legend=dict(
#         orientation='v', 
#         x=0, 
#         y=1,
#         xanchor='left', 
#         bgcolor='rgba(255,255,255,0.9)'  
#     ),
#     plot_bgcolor='rgba(255, 255, 255, 0.8)',  
#     bargap=0.2,  
#     font=dict(family='Arial', size=14, color='black'),
#     width=1200,  
#     # height=650 
#)


# fig.show()


# In[99]:


# Group by 'Month' and 'Shift' and sum the incidents
incidents_by_month_shift = df.groupby(['Month', 'Shift'])['Incident'].sum().unstack().fillna(0)

#plt.figure(figsize=(12, 8))
#sns.heatmap(incidents_by_month_shift, cmap='YlOrRd', annot=True, fmt='g', linewidths=.5, linecolor='lightgrey')
#plt.xlabel('Shift')
#plt.ylabel('Month')
#plt.title('Incidents by Month and Shift')
#plt.xticks(rotation=45)
#plt.tight_layout()
#plt.show()


# In[102]:


incidents_by_day_shift = df.groupby(['Day_of_Week', 'Shift'])['Incident'].sum().unstack().fillna(0)


# In[103]:


shift1_total_incidents = incidents_by_day_shift['Shift 1 (6AM-2PM)'].sum()

print("Total Incidents for Shift 1:", shift1_total_incidents)



#plt.figure(figsize=(12, 8))
#sns.heatmap(incidents_by_day_shift, cmap='YlOrRd', annot=True, fmt='g', linewidths=.5, linecolor='lightgrey')
#plt.xlabel('Shift')
#plt.ylabel('Day of the Week')
#plt.title('Incidents by Day of the Week and Shift')
#plt.xticks(rotation=45)
#plt.tight_layout()
#plt.show()


# In[110]:


total_incidents_monday = incidents_by_weekday['Monday'].sum()
print("Total incidents on Monday:", total_incidents_monday)


# In[111]:


total_incidents_tuesday = incidents_by_weekday['Tuesday'].sum()
print("Total incidents on Tuesday:", total_incidents_tuesday)


# In[112]:


total_incidents_wed = incidents_by_weekday['Wednesday'].sum()
print("Total incidents on Wednesday:", total_incidents_wed)


# In[114]:


total_incidents_Thursday= incidents_by_weekday['Thursday'].sum()
print("Total incidents on Thursday:", total_incidents_Thursday)


# In[115]:


total_incidents_Friday= incidents_by_weekday['Friday'].sum()
print("Total incidents on Friday:", total_incidents_Friday)


# In[116]:


total_incidents_Saturday= incidents_by_weekday['Saturday'].sum()
print("Total incidents on Saturday:", total_incidents_Saturday)


# In[118]:


total_incidents_Sunday= incidents_by_weekday['Sunday'].sum()
print("Total incidents on Sunday:", total_incidents_Sunday)


# In[121]:


incidents_by_sub_area = df.groupby('Sub Area')['Incident'].sum()
sorted_incidents_by_sub_area = incidents_by_sub_area.sort_values(ascending=False)
top_30_sub_areas = sorted_incidents_by_sub_area.head(30)


# In[122]:


# Convert the top_30_sub_areas Series to a DataFrame for Plotly
top_30_sub_areas_df = top_30_sub_areas.reset_index()
top_30_sub_areas_df.columns = ['Sub_Area', 'Number_of_Incidents']

# Create an interactive bar chart using Plotly Express
# fig = px.bar(top_30_sub_areas_df, 
#              x='Sub_Area', 
#              y='Number_of_Incidents', 
#              title='Top 30 Sub-Areas with Highest Number of Incidents',
#              labels={'Sub_Area': 'Sub-Area', 'Number_of_Incidents': 'Number of Incidents'},
#              color='Sub_Area',  # Color bars based on Sub Area
#              color_continuous_scale=px.colors.sequential.Teal)  # Use a teal color scale

# # Enhance the layout and aesthetics of the chart
# fig.update_layout(
#     xaxis_title='Sub-Area',
#     yaxis_title='Number of Incidents',
#     title_x=0.5,  # Center the title
#     plot_bgcolor='white',  # Set the background color to white for a clean look
#     xaxis_tickangle=-45,  # Rotate the x-axis labels for better readability
#     width=1200,  # Width of the plot in pixels
#     height=800   # Height of the plot in pixels
# )

# # Show the plot
# fig.show()


# In[126]:


incidents_by_sub_area = df.groupby('Sub Area')['Incident'].sum()
sorted_incidents_by_sub_area = incidents_by_sub_area.sort_values(ascending=False)

last_30_sub_areas = sorted_incidents_by_sub_area.tail(30)


# In[127]:


last_30_sub_areas_df = last_30_sub_areas.reset_index()
last_30_sub_areas_df.columns = ['Sub_Area', 'Number_of_Incidents']
last_30_sub_areas_df = last_30_sub_areas_df.sort_values(by='Number_of_Incidents', ascending=False)

# # Create an interactive bar chart using Plotly Express
# fig = px.bar(last_30_sub_areas_df, 
#              x='Sub_Area', 
#              y='Number_of_Incidents', 
#              title='Last 30 Sub-Areas with Highest Number of Incidents',
#              labels={'Sub_Area': 'Sub-Area', 'Number_of_Incidents': 'Number of Incidents'},
#              color='Sub_Area',  # Color bars based on Sub Area
#              color_continuous_scale=px.colors.sequential.Blues)  # Use a blue color scale

# # Enhance the layout and aesthetics of the chart
# fig.update_layout(
#     xaxis_title='Sub-Area',
#     yaxis_title='Number of Incidents',
#     title_x=0.5,  # Center the title
#     plot_bgcolor='white',  # Set the background color to white for a clean look
#     xaxis_tickangle=-45,  # Rotate the x-axis labels for better readability
#     width=1200,  # Width of the plot in pixels
#     height=800   # Height of the plot in pixels
# )

# # Show the plot
# fig.show()


# In[129]:


incidents_by_category = df.groupby('CS \ Risk Categories')['Incident'].sum()
sorted_incidents_by_category = incidents_by_category.sort_values(ascending=False)
top_20_categories = sorted_incidents_by_category.head(20)


# In[130]:


incidents_by_category = df.groupby('CS \ Risk Categories')['Incident'].sum()
sorted_incidents_by_category = incidents_by_category.sort_values(ascending=False)
top_20_categories = sorted_incidents_by_category.head(20)
# Convert the top_20_categories Series to a DataFrame for Plotly
top_20_categories_df = top_20_categories.reset_index()
top_20_categories_df.columns = ['CS_Risk_Categories', 'Number_of_Incidents']

# Create an interactive bar chart using Plotly Express
# fig = px.bar(top_20_categories_df, 
#              x='CS_Risk_Categories', 
#              y='Number_of_Incidents', 
#              title='Top 20 CS/Risk Categories with Highest Number of Incidents',
#              labels={'CS_Risk_Categories': 'CS / Risk Categories', 'Number_of_Incidents': 'Number of Incidents'},
#              color='Number_of_Incidents',  # Color bars based on the number of incidents
#              color_continuous_scale=px.colors.sequential.Viridis)  # Use a viridis color scale

# # Enhance the layout and aesthetics of the chart
# fig.update_layout(
#     xaxis_title='CS / Risk Categories',
#     yaxis_title='Number of Incidents',
#     title_x=0.5,  # Center the title
#     plot_bgcolor='white',  # Set the background color to white for a clean look
#     xaxis_tickangle=-45,  # Rotate the x-axis labels for better readability
#     width=1000,  # Width of the plot in pixels
#     height=800   # Height of the plot in pixels
# )

# # Show the plot
# fig.show()


# In[132]:


incidents_by_likelihood = df.groupby('Likelihood')['Incident'].sum()

incidents_by_likelihood_df = incidents_by_likelihood.reset_index()
incidents_by_likelihood_df.columns = ['Likelihood', 'Number_of_Incidents']

# Create an interactive pie chart using Plotly Express with added aesthetics
# fig = px.pie(incidents_by_likelihood_df, 
#              values='Number_of_Incidents', 
#              names='Likelihood', 
#              title='Incidents by Likelihood', 
#              color_discrete_sequence=px.colors.qualitative.Pastel,  # Using a more vibrant color sequence
#              hole=0.3)  # Creates a donut chart

# # Enhance the layout and aesthetics of the chart
# fig.update_traces(textposition='inside', textinfo='percent+label', hoverinfo='label+percent', marker=dict(line=dict(color='white', width=2)))
# fig.update_layout(
#     title_x=0.5,  # Center the title for consistency
#     legend_title_text='Likelihood',  # Provide a title for the legend for better understanding
#     legend=dict(orientation="h", yanchor="bottom", y=0.01, xanchor="right", x=1),  # Positioning the legend horizontally at the bottom
#     width=800,  # Increase width of the plot
#     height=800   # Increase height of the plot
# )

# # Show the plot
# fig.show()


# In[133]:


# Get the value counts of incidents
incident_counts = df['Incident'].value_counts()

# Create a DataFrame for Plotly
incident_counts_df = incident_counts.reset_index()
incident_counts_df.columns = ['Incident', 'Count']

# Create an interactive bar chart using Plotly Express
# fig = px.bar(incident_counts_df, 
#              x='Incident', 
#              y='Count', 
#              title='Distribution of Incidents',
#              labels={'Incident': 'Incident Type', 'Count': 'Number of Incidents'},
#              color='Incident',  # Color bars based on incident type
#              color_discrete_sequence=px.colors.qualitative.Pastel)  # Using a pastel color palette

# # Enhance the layout and aesthetics of the chart
# fig.update_layout(
#     xaxis_title='Incident Type',
#     yaxis_title='Number of Incidents',
#     title_x=0.5,  # Center the title
#     plot_bgcolor='white',  # Set the background color to white for a clean look
#     xaxis_tickangle=-45,  # Rotate the x-axis labels for better readability
#     width=1000,  # Width of the plot in pixels
#     height=600   # Height of the plot in pixels
# )

# # Show the plot
# fig.show()


import streamlit as st
import pandas as pd
import plotly.express as px

# Get the value counts of incidents for the "Near Miss" type
near_miss_counts = df['Near Miss'].value_counts()

# Create a DataFrame for Plotly
near_miss_counts_df = near_miss_counts.reset_index()
near_miss_counts_df.columns = ['Near Miss', 'Count']

# Create an interactive bar chart using Plotly Express
# fig = px.bar(near_miss_counts_df, 
#              x='Near Miss', 
#              y='Count', 
#              title='Distribution of Near Miss Incidents',
#              labels={'Near Miss': 'Near Miss Type', 'Count': 'Number of Incidents'},
#              color='Near Miss',  # Color bars based on incident type
#              color_discrete_sequence=px.colors.qualitative.Pastel)  # Using a pastel color palette

# # Enhance the layout and aesthetics of the chart
# fig.update_layout(
#     xaxis_title='Near Miss Type',
#     yaxis_title='Number of Incidents',
#     title_x=0.5,  # Center the title
#     plot_bgcolor='white',  # Set the background color to white for a clean look
#     width=800,  # Width of the plot in pixels
#     height=600   # Height of the plot in pixels
# )

# # Show the plot
# fig.show()
import streamlit as st
st.set_option('deprecation.showPyplotGlobalUse', False)

def monthly_analysis():
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.strftime('%Y-%m')
    df['Day_of_Week'] = df['Date'].dt.day_name()

    day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Create heatmaps and bar charts in Streamlit
    incidents_by_weekday = df.groupby(['Month', 'Day_of_Week'])['Incident'].sum().unstack().fillna(0)
    incidents_by_weekday = incidents_by_weekday[day_order]

    # Sorting DataFrame by 'Month'
    df_sorted = df.sort_values(by='Month')

    # First row
    with st.container():
        col1, col2 = st.columns(2)

        # First column in first row
        with col1:
            # Heatmap for incidents by weekday
            plt.figure(figsize=(12, 8))
            sns.heatmap(incidents_by_weekday, cmap='YlOrRd', annot=True, fmt='g', linewidths=.5, linecolor='lightgrey')
            plt.xlabel('Day of the Week')
            plt.ylabel('Month')
            plt.title('Incidents by Month and Weekday')
            plt.xticks(rotation=45)
            plt.tight_layout()
            st.pyplot()

        # Second column in first row
        with col2:
            # Heatmap for incidents by month and shift
            incidents_by_month_shift = df.groupby(['Month', 'Shift'])['Incident'].sum().unstack().fillna(0)

            plt.figure(figsize=(12, 8))
            sns.heatmap(incidents_by_month_shift, cmap='Wistia', annot=True, fmt='g', linewidths=.5, linecolor='lightgrey')
            plt.xlabel('Shift')
            plt.ylabel('Month')
            plt.title('Incidents by Month and Shift')
            plt.xticks(rotation=45)
            plt.tight_layout()
            st.pyplot()

    # Second row
    with st.container():
        # Additional Plot 2: 3D pie chart
        total_incidents_by_month = df.groupby('Month')['Incident'].sum()
        fig = go.Figure(data=[go.Pie(labels=total_incidents_by_month.index,
                                     values=total_incidents_by_month.values,
                                     title='Total Incidents by Month',
                                     hoverinfo='label+percent',
                                     textinfo='value+percent',
                                     hole=0.3,
                                     pull=[0.1] * len(total_incidents_by_month))])
        fig.update_layout(
            title_text='Total Incidents by Month',
            title_x=0.5,
            legend_title='Month',
            legend=dict(orientation='h', x=0, y=-0.1),
            width=800,
            height=600
        )
        st.plotly_chart(fig)

    # Third row
    with st.container():
        # Additional Plot 1: Line chart using Plotly
        incidents_by_weekday.reset_index(inplace=True)
        incidents_by_weekday_melted = pd.melt(incidents_by_weekday, id_vars='Month', var_name='Day_of_Week', value_name='Incidents')
        fig = px.line(incidents_by_weekday_melted, x='Month', y='Incidents', color='Day_of_Week', 
                      title='Incidents by Month and Weekday', labels={'Incidents': 'Number of Incidents', 'Month': 'Month'})
        fig.update_layout(
            xaxis={'type': 'category', 'categoryorder': 'category ascending'}, 
            xaxis_title='Month',
            yaxis_title='Number of Incidents',
            legend_title='Day of the Week',
            plot_bgcolor='white',
            title_font_size=24,
            legend_font_size=14,
            font_family='Arial',
            font_size=12,
            width=1200,  # Adjust the width as needed
            height=650   # Adjust the height as needed
        )
        fig.update_traces(line=dict(width=2), mode='lines+markers')
        st.plotly_chart(fig)

    # Fourth row
    with st.container():
        # Stacked bar chart using Plotly
        fig = px.bar(x=df_sorted['Month'], y=df_sorted['Incident'], color=df_sorted['Shift'], barmode='stack',
                     labels={'Date': 'Month', 'Number of Incidents': 'Number of Incidents'},
                     title='Stacked Number of Incidents by Shift and Month')
        fig.update_layout(
            title={'text': 'Stacked Number of Incidents by Shift and Month', 'font': {'size': 20}, 'x': 0.5},
            xaxis_title='Month',
            yaxis_title='Total Number of Incidents',
            xaxis=dict(
                tickmode='linear',
                tick0=0,
                dtick=1,
                tickangle=-45,
                type='category'
            ),
            legend_title='Shift',
            legend=dict(
                orientation='v',
                x=0,
                y=1,
                xanchor='left',
                bgcolor='rgba(255,255,255,0.9)'
            ),
            plot_bgcolor='rgba(255, 255, 255, 0.8)',
            bargap=0.2,
            font=dict(family='Arial', size=14, color='black'),
            width=1200,
            height=650
        )
        st.plotly_chart(fig)

def weekly_analysis():
    df['Date'] = pd.to_datetime(df['Date'])
    df['Week_of_Year'] = df['Date'].dt.strftime('%Y-%U')
    df['Day_of_Week'] = df['Date'].dt.day_name()
    day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    incidents_by_weekday = df.groupby(['Week_of_Year', 'Day_of_Week']).size().unstack().reindex(columns=day_order).fillna(0)
    
    plt.figure(figsize=(12, 8))  # Decrease the figure size for a smaller heatmap

    # Create a heatmap with custom styling
    sns.heatmap(incidents_by_weekday, cmap='Blues', annot=True, fmt='g', linewidths=.5, linecolor='lightgrey',
                cbar_kws={'label': 'Number of Incidents'})  # Add color bar label

    plt.xlabel('Day of the Week', fontsize=14)  # Adjust x-axis label font size
    plt.ylabel('Week of the Year', fontsize=14)  # Adjust y-axis label font size
    plt.title('Incidents by Week and Weekday', fontsize=16)  # Adjust title font size
    plt.xticks(rotation=45, fontsize=12)  # Adjust x-axis tick font size and rotation
    plt.yticks(fontsize=12)  # Adjust y-axis tick font size
    plt.tight_layout()

    # Display the heatmap
    st.pyplot()


def daywise_analysis():
    df['Date'] = pd.to_datetime(df['Date'])
    df['Day_of_Week'] = df['Date'].dt.day_name()
    incidents_by_day = df.groupby('Day_of_Week')['Incident'].sum()

    days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    incidents_by_day = incidents_by_day.reindex(days_order)

    # Create a DataFrame for Plotly
    incidents_by_day_df = pd.DataFrame({'Day_of_Week': incidents_by_day.index, 'Number_of_Incidents': incidents_by_day.values})

    # Create a bar chart using Plotly Express for incidents by day of the week
    fig = px.bar(incidents_by_day_df, 
                 x='Day_of_Week', 
                 y='Number_of_Incidents', 
                 title='Incidents by Day of the Week',
                 labels={'Day_of_Week': 'Day of the Week', 'Number_of_Incidents': 'Number of Incidents'},
                 color='Day_of_Week',  # Color the bars by day of the week
                 color_discrete_sequence=px.colors.qualitative.Vivid)  # Choose a vivid color palette

    # Update layout for better readability and larger bar chart
    fig.update_layout(
        xaxis_title='Day of the Week',
        yaxis_title='Number of Incidents',
        title_x=0.5,  # Center the title
        plot_bgcolor='white',  # Set the background to white for a cleaner look
        xaxis_tickangle=-45,  # Angle the x-axis labels for better visibility
        width=1300,  # Set the width of the plot
        height=850    # Set the height of the plot
    )

    # Show the bar chart
    st.plotly_chart(fig)

    # Additional plots
    # Plot 1: Incidents by Day of the Week and Shift
    col1, col2 = st.columns(2)  # Split the screen into two columns

    with col1:
        plt.figure(figsize=(10, 8))  # Larger figure size
        sns.heatmap(incidents_by_day_shift, cmap='bone', annot=True, fmt='g', linewidths=.5, linecolor='lightgrey')
        plt.xlabel('Shift')
        plt.ylabel('Day of the Week')
        plt.title('Incidents by Day of the Week and Shift')
        plt.xticks(rotation=45)
        plt.tight_layout()
        st.pyplot()

    with col2:
        # Plot 2: Incidents by Month and Weekday
        df['Month'] = df['Date'].dt.strftime('%Y-%m')
        df['Day_of_Week'] = df['Date'].dt.day_name()

        day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        incidents_by_weekday = df.groupby(['Month', 'Day_of_Week'])['Incident'].sum().unstack().fillna(0)
        incidents_by_weekday = incidents_by_weekday[day_order]

        plt.figure(figsize=(10, 8))  # Larger figure size
        sns.heatmap(incidents_by_weekday, cmap='YlOrRd', annot=True, fmt='g', linewidths=.5, linecolor='lightgrey')
        plt.xlabel('Day of the Week')
        plt.ylabel('Month')
        plt.title('Incidents by Month and Weekday')
        plt.xticks(rotation=45)
        plt.tight_layout()
        st.pyplot()

    # Plot 3: Line chart
    fig_line = go.Figure(data=go.Scatter(
        x=incidents_by_day_df['Day_of_Week'],
        y=incidents_by_day_df['Number_of_Incidents'],
        mode='lines+markers',  # Connect points with lines and add markers
        line=dict(color='royalblue', width=3),  # Set line color and width
        marker=dict(color='red', size=10, line=dict(color='white', width=2))  # Set marker color, size, and outline
    ))

    # Update layout for better readability
    fig_line.update_layout(
        title='Incidents by Day of the Week',
        xaxis=dict(title='Day of the Week', tickangle=-45, showgrid=False),  # Rotate x-axis labels and remove gridlines
        yaxis=dict(title='Number of Incidents', showgrid=False),  # Remove gridlines on y-axis
        plot_bgcolor='rgba(255, 255, 255, 0.9)',  # Set plot background color with transparency
        title_x=0.5,  # Center the title
        font=dict(family='Arial', size=14, color='black'),  # Set font style and size
        margin=dict(l=50, r=50, t=80, b=50),  # Adjust margins
    )

    # Show the line chart
    st.plotly_chart(fig_line)



def shiftwise_analysis():
    if isinstance(shift_counts, pd.Series):
        shift_counts_df = shift_counts.reset_index()
        shift_counts_df.columns = ['Shift', 'Number_of_Incidents']
    else:
        shift_counts_df = shift_counts

    # Create a bar chart using Plotly Express for number of incidents by shift
    fig = px.bar(shift_counts_df, 
                 x='Shift', 
                 y='Number_of_Incidents', 
                 title='Number of Incidents by Shift',
                 labels={'Number_of_Incidents': 'Number of Incidents', 'Shift': 'Shift'},
                 color='Shift',  # This uses the shift column to color the bars differently
                 color_continuous_scale=px.colors.sequential.Viridis,  # Optional: use a color scale
                 template='plotly_white')  # Use a white background for a clean look

    # Update layout for better readability
    fig.update_layout(
        xaxis_title='Shift',
        yaxis_title='Number of Incidents',
        title_x=0.5,  # Center the title
        plot_bgcolor='white',  # Ensure the background color is white
        height=600,
        width=1000
    )

    # Show the first plot using Streamlit
    st.plotly_chart(fig)

    # Additional plots
    # Plot 1: Stacked Number of Incidents by Shift and Month
    fig = px.bar(monthly_shift_counts_melted, x='Month', y='Number of Incidents', color='Shift',
                 barmode='stack', labels={'Date': 'Month', 'Number of Incidents': 'Number of Incidents'},
                 title='Stacked Number of Incidents by Shift and Month')

    fig.update_layout(
        title={'text': 'Stacked Number of Incidents by Shift and Month', 'font': {'size': 20}, 'x': 0.5},
        xaxis_title='Month',
        yaxis_title='Total Number of Incidents',
        xaxis=dict(
            tickmode='linear', 
            tick0=0,  
            dtick=1,  
            tickangle=-45, 
            type='category' 
        ),
        legend_title='Shift',
        legend=dict(
            orientation='v', 
            x=0, 
            y=1,
            xanchor='left', 
            bgcolor='rgba(255,255,255,0.9)'  
        ),
        plot_bgcolor='rgba(255, 255, 255, 0.8)',  
        bargap=0.2,  
        font=dict(family='Arial', size=14, color='black'),
        width=1200,  
        height=650 
    )

    # Show the second plot using Streamlit column
    st.plotly_chart(fig)

    # Plot 2: Incidents by Month and Shift
    incidents_by_month_shift = df.groupby(['Month', 'Shift'])['Incident'].sum().unstack().fillna(0)

    # Plot 3: Incidents by Day of the Week and Shift
    incidents_by_day_shift = df.groupby(['Day_of_Week', 'Shift'])['Incident'].sum().unstack().fillna(0)

    # Arrange the last two plots into the third row
    col1, col2 = st.columns(2)

    with col1:
        plt.figure(figsize=(10,8))
        sns.heatmap(incidents_by_month_shift, cmap='bone', annot=True, fmt='g', linewidths=.5, linecolor='lightgrey')
        plt.xlabel('Shift')
        plt.ylabel('Month')
        plt.title('Incidents by Month and Shift')
        plt.xticks(rotation=45)
        plt.tight_layout()
        st.pyplot()

    with col2:
        plt.figure(figsize=(10,8))
        sns.heatmap(incidents_by_day_shift, cmap='cool', annot=True, fmt='g', linewidths=.5, linecolor='lightgrey')
        plt.xlabel('Shift')
        plt.ylabel('Day of the Week')
        plt.title('Incidents by Day of the Week and Shift')
        plt.xticks(rotation=45)
        plt.tight_layout()
        st.pyplot()


def top_areas_analysis():
    # Convert the top_30_sub_areas Series to a DataFrame for Plotly
    top_30_sub_areas_df = top_30_sub_areas.reset_index()
    top_30_sub_areas_df.columns = ['Sub_Area', 'Number_of_Incidents']

    # Create an interactive bar chart using Plotly Express
    fig = px.bar(top_30_sub_areas_df, 
                 x='Sub_Area', 
                 y='Number_of_Incidents', 
                 title='Top 30 Sub-Areas with Highest Number of Incidents',
                 labels={'Sub_Area': 'Sub-Area', 'Number_of_Incidents': 'Number of Incidents'},
                 color='Sub_Area',  # Color bars based on Sub Area
                 color_continuous_scale=px.colors.sequential.Teal)  # Use a teal color scale

    # Enhance the layout and aesthetics of the chart
    fig.update_layout(
        xaxis_title='Sub-Area',
        yaxis_title='Number of Incidents',
        title_x=0.375,  # Center the title
        plot_bgcolor='white',  # Set the background color to white for a clean look
        xaxis_tickangle=-45,  # Rotate the x-axis labels for better readability
        width=1400,  # Width of the plot in pixels
        height=1200   # Height of the plot in pixels
    )

    # Show the plot
    st.plotly_chart(fig)

def bottom_areas_analysis():
    last_30_sub_areas_df = last_30_sub_areas.reset_index()
    last_30_sub_areas_df.columns = ['Sub_Area', 'Number_of_Incidents']
    last_30_sub_areas_df = last_30_sub_areas_df.sort_values(by='Number_of_Incidents', ascending=False)

    # Create an interactive bar chart using Plotly Express
    fig = px.bar(last_30_sub_areas_df, 
                 x='Sub_Area', 
                 y='Number_of_Incidents', 
                 title='Last 30 Sub-Areas with Highest Number of Incidents',
                 labels={'Sub_Area': 'Sub-Area', 'Number_of_Incidents': 'Number of Incidents'},
                 color='Sub_Area',  # Color bars based on Sub Area
                 color_continuous_scale=px.colors.sequential.Blues)  # Use a blue color scale

    # Enhance the layout and aesthetics of the chart
    fig.update_layout(
        xaxis_title='Sub-Area',
        yaxis_title='Number of Incidents',
        title_x=0.375,  # Center the title
        plot_bgcolor='white',  # Set the background color to white for a clean look
        xaxis_tickangle=-45,  # Rotate the x-axis labels for better readability
        width=1400,  # Width of the plot in pixels
        height=1200   # Height of the plot in pixels
    )

    # Show the plot
    st.plotly_chart(fig)


def risk_categories_analysis():
    incidents_by_category = df.groupby('CS \ Risk Categories')['Incident'].sum()
    sorted_incidents_by_category = incidents_by_category.sort_values(ascending=False)
    top_20_categories = sorted_incidents_by_category.head(20)
    # Convert the top_20_categories Series to a DataFrame for Plotly
    top_20_categories_df = top_20_categories.reset_index()
    top_20_categories_df.columns = ['CS_Risk_Categories', 'Number_of_Incidents']

    # Create an interactive bar chart using Plotly Express
    fig = px.bar(top_20_categories_df, 
                 x='CS_Risk_Categories', 
                 y='Number_of_Incidents', 
                 title='Top 20 CS/Risk Categories with Highest Number of Incidents',
                 labels={'CS_Risk_Categories': 'CS / Risk Categories', 'Number_of_Incidents': 'Number of Incidents'},
                 color='Number_of_Incidents',  # Color bars based on the number of incidents
                 color_continuous_scale=px.colors.sequential.Viridis)  # Use a viridis color scale

    # Enhance the layout and aesthetics of the chart
    fig.update_layout(
        xaxis_title='CS / Risk Categories',
        yaxis_title='Number of Incidents',
        title_x=0.375,  # Center the title
        plot_bgcolor='white',  # Set the background color to white for a clean look
        xaxis_tickangle=-45,  # Rotate the x-axis labels for better readability
        width=1200,  # Width of the plot in pixels
        height=800   # Height of the plot in pixels
    )

    # Show the plot
    st.plotly_chart(fig)

    # Assuming you have a datetime column named 'Date' in your DataFrame 'df'
    df['Date'] = pd.to_datetime(df['Date'])

    # Group incidents by CS / Risk Categories and Date
    incidents_by_category_date = df.groupby(['CS \ Risk Categories', pd.Grouper(key='Date', freq='M')])['Incident'].sum().reset_index()

    # Create a line plot using Plotly Express
    fig_line = px.line(incidents_by_category_date, 
                       x='Date', 
                       y='Incident', 
                       color='CS \ Risk Categories',
                       title='Trend of Incidents by CS / Risk Categories',
                       labels={'Date': 'Date', 'Incident': 'Number of Incidents', 'CS \ Risk Categories': 'CS / Risk Categories'},
                       line_shape='spline',  # Use spline interpolation for smoother lines
                       template='plotly_dark')  # Use a dark template for an attractive look

    # Enhance the layout and aesthetics of the line plot
    fig_line.update_layout(
        xaxis_title='Date',
        yaxis_title='Number of Incidents',
        title_x=0.5,  # Center the title
        font=dict(family='Arial', size=12, color='white'),  # Set font style and size
        width=1200,  # Width of the plot
        height=600   # Height of the plot
    )

    # Show the line plot
    st.plotly_chart(fig_line)
    
def likelihood_analysis():
    incidents_by_likelihood = df.groupby('Likelihood')['Incident'].sum()

    incidents_by_likelihood_df = incidents_by_likelihood.reset_index()
    incidents_by_likelihood_df.columns = ['Likelihood', 'Number_of_Incidents']

    # Create an interactive pie chart using Plotly Express with added aesthetics
    fig = px.pie(incidents_by_likelihood_df, 
                 values='Number_of_Incidents', 
                 names='Likelihood', 
                 title='Incidents by Likelihood', 
                 color_discrete_sequence=px.colors.qualitative.Pastel,  # Using a more vibrant color sequence
                 hole=0.3)  # Creates a donut chart

    # Enhance the layout and aesthetics of the chart
    fig.update_traces(textposition='inside', textinfo='percent+label', hoverinfo='label+percent', marker=dict(line=dict(color='white', width=2)))
    fig.update_layout(
        title_x=0.5,  # Center the title for consistency
        legend_title_text='Likelihood',  # Provide a title for the legend for better understanding
        legend=dict(orientation="h", yanchor="bottom", y=0.01, xanchor="right", x=1),  # Positioning the legend horizontally at the bottom
        width=800,  # Increase width of the plot
        height=800   # Increase height of the plot
    )

    # Assuming you have a datetime column named 'Date' in your DataFrame 'df'
    df['Date'] = pd.to_datetime(df['Date'])

    # Group incidents by Likelihood and Date
    incidents_by_likelihood_date = df.groupby(['Likelihood', pd.Grouper(key='Date', freq='M')])['Incident'].sum().reset_index()

    # Create a line plot using Plotly Express
    fig_line = px.line(incidents_by_likelihood_date, 
                       x='Date', 
                       y='Incident', 
                       color='Likelihood',
                       title='Trend of Incidents by Likelihood',
                       labels={'Date': 'Date', 'Incident': 'Number of Incidents', 'Likelihood': 'Likelihood'},
                       line_shape='spline',  # Use spline interpolation for smoother lines
                       template='plotly_white')  # Use a white background for a clean look

    # Enhance the layout and aesthetics of the line plot
    fig_line.update_layout(
        xaxis_title='Date',
        yaxis_title='Number of Incidents',
        title_x=0.5,  # Center the title
        legend_title='Likelihood',  # Provide a title for the legend
        plot_bgcolor='white',  # Set the background to white for a cleaner look
        font=dict(family='Arial', size=12, color='black'),  # Set font style and size
        width=1300,  # Set the width of the plot
        height=800   # Set the height of the plot
    )
    # Show the plot
    st.plotly_chart(fig_line)
    st.plotly_chart(fig)

    

def miscellaneous_analysis():
    # Get the value counts of incidents
    incident_counts = df['Incident'].value_counts()

    # Create a DataFrame for Plotly
    incident_counts_df = incident_counts.reset_index()
    incident_counts_df.columns = ['Incident', 'Count']

    # Sort the DataFrame by incident count in descending order
    incident_counts_df = incident_counts_df.sort_values(by='Count', ascending=False)

    # Create an interactive bar chart using Plotly Express
    fig_bar = px.bar(incident_counts_df, 
                     x='Incident', 
                     y='Count', 
                     title='Distribution of Incidents',
                     labels={'Incident': 'Incident Type', 'Count': 'Number of Incidents'},
                     color='Incident',  # Color bars based on incident type
                     color_discrete_sequence=px.colors.qualitative.Pastel)  # Using a pastel color palette

    # Enhance the layout and aesthetics of the bar chart
    fig_bar.update_layout(
        xaxis_title='Incident Type',
        yaxis_title='Number of Incidents',
        title_x=0.375,  # Center the title
        plot_bgcolor='white',  # Set the background color to white for a clean look
        xaxis_tickangle=-45,  # Rotate the x-axis labels for better readability
        width=1300,  # Width of the plot in pixels
        height=800   # Height of the plot in pixels
    )

    # Show the bar chart
    st.plotly_chart(fig_bar)

    # Create a line plot using Plotly Express
    fig_line = px.line(incident_counts_df, 
                       x='Incident', 
                       y='Count', 
                       title='Distribution of Incidents',
                       labels={'Incident': 'Incident Type', 'Count': 'Number of Incidents'},
                       line_shape='spline',  # Use spline interpolation for smoother lines
                       template='plotly_dark')  # Use a dark template for an attractive look

    # Enhance the layout and aesthetics of the line plot
    fig_line.update_layout(
        xaxis_title='Incident Type',
        yaxis_title='Number of Incidents',
        title_x=0.5,  # Center the title
        plot_bgcolor='black',  # Set the background color to black for a sleek look
        font=dict(family='Arial', size=12, color='white'),  # Set font style and size
        width=1200,  # Width of the plot
        height=600,  # Height of the plot
        showlegend=False  # Hide the legend as it's not necessary for a single line plot
    )

    # Show the line plot
    st.plotly_chart(fig_line)

    # Create a pie plot using Plotly
    fig_pie = go.Figure(data=[go.Pie(labels=incident_counts_df['Incident'], 
                                     values=incident_counts_df['Count'],
                                     hole=0.3)])  # Creates a donut chart

    # Enhance the layout and aesthetics of the pie plot
    fig_pie.update_layout(
        title='Distribution of Incidents',
        title_x=0.5,  # Center the title
        template='plotly_white',  # Use a white template for a clean look
        width=800,  # Width of the plot
        height=600,  # Height of the plot
        showlegend=True  # Show legend for better readability
    )

    # Show the pie plot
    st.plotly_chart(fig_pie)

    # Get the value counts of incidents for the "Near Miss" type
    near_miss_counts = df['Near Miss'].value_counts()

    # Create a DataFrame for Plotly
    near_miss_counts_df = near_miss_counts.reset_index()
    near_miss_counts_df.columns = ['Near Miss', 'Count']

    # Create an interactive bar chart using Plotly Express
    fig = px.bar(near_miss_counts_df, 
                 x='Near Miss', 
                 y='Count', 
                 title='Distribution of Near Miss Incidents',
                 labels={'Near Miss': 'Near Miss Type', 'Count': 'Number of Incidents'},
                 color='Near Miss',  # Color bars based on incident type
                 color_discrete_sequence=px.colors.qualitative.Safe)  # Using a pastel color palette

    # Enhance the layout and aesthetics of the chart
    fig.update_layout(
        xaxis_title='Near Miss',
        yaxis_title='Number of Incidents',
        title_x=0.375,  # Center the title
        plot_bgcolor='White',  # Set the background color to white for a clean look
        width=1600,  # Width of the plot in pixels
        height=800   # Height of the plot in pixels
    )

    # Show the plot
    st.plotly_chart(fig)
# Set wide mode to True to remove spacing between sidebar and plot
st.set_page_config(layout="wide")

# Define the title and sidebar layout
st.sidebar.title('Safety Event Analysis Dashboard')

# Add a selectbox for analysis category in the sidebar
analysis_category = st.sidebar.selectbox('Select Analysis Category', ['Monthly Analysis', 'Weekly Analysis', 'Day wise Analysis', 'Shift Analysis', 'Top Areas Analysis', 'Bottom Areas Analysis', 'Risk Categories Analysis', 'Likelihood Analysis', 'Miscellaneous Analysis'])


if analysis_category == 'Monthly Analysis':
    monthly_analysis()
elif analysis_category == 'Weekly Analysis':
    weekly_analysis()
elif analysis_category == 'Day wise Analysis':
    daywise_analysis()
elif analysis_category == 'Shift Analysis':
    shiftwise_analysis()
elif analysis_category == 'Top Areas Analysis':
    top_areas_analysis()
elif analysis_category == 'Bottom Areas Analysis':
    bottom_areas_analysis()
elif analysis_category == 'Risk Categories Analysis':
    risk_categories_analysis()
elif analysis_category == 'Likelihood Analysis':
    likelihood_analysis()
elif analysis_category == 'Miscellaneous Analysis':
    miscellaneous_analysis()
