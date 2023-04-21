from bs4 import BeautifulSoup
import pandas as pd
import copy

## WARNING: 
# You need to play with the margin to print everything correctly.

# Path to template
path_template_document = "data/template/page.html"
path_template_idcard = "data/template/id_card_volunteer.html"

# Columns taking from the dataset to replace inside the idcard template
path_dataset = "data/dataset/Foiegraph 2022 Registration (Responses) - Form Responses 1.csv"
path_html_output = "data/out_volunteer.html"
# script
df = pd.read_csv(path_dataset, encoding='utf-8')

## Manipulation goes here
df = df[-df['Volunteer'].isna()]

## Output the badge
with open(path_template_document, encoding="utf-8") as fp, open(path_template_idcard, encoding="utf-8") as fid:
    document = BeautifulSoup(fp, 'html.parser')
    template_idcard = BeautifulSoup(fid, 'html.parser')

body = document.find("body")

for i in range(len(df)):
    idcard = copy.copy(template_idcard)
    if df.iloc[i].loc["Attending in person or remotely?"] != "Remotely":
        for id in df.columns:
            tag = idcard.find('text',id=id)
            if tag:
                tag["id"] = id + str(i)

                if pd.notna(df.iloc[i].loc[id]):
                    tag.string = df.iloc[i].loc[id]
 
        body.append(idcard)

with open(path_html_output,"w", encoding='utf-8-sig') as f:
    f.write(str(document))