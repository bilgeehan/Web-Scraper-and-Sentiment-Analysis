import csv
from textblob import TextBlob
from mtranslate import translate

old_data = []  # Datas until 2013(page 1 to 10)
old_data_positive = []
old_data_negative = []
old_data_neutral = []
new_data = []  # Datas in 2023 (page 580 to 590)
new_data_positive = []
new_data_negative = []
new_data_neutral = []


def read_from_csv(filename):
    data = []
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data


csv_datas = read_from_csv('surian.csv')

for row in csv_datas:
    old_data.append(row['Old Data'].strip())
    new_data.append(row['New Data'].strip())

for data in old_data:
    if data:
        english_translation = translate(data, 'en')
        blob = TextBlob(english_translation)
        sentiment = blob.sentiment
        if sentiment.polarity > 0:
            old_data_positive.append(data)
        elif sentiment.polarity < 0:
            old_data_negative.append(data)
        else:
            old_data_neutral.append(data)

for data in new_data:
    if data:
        english_translation = translate(data, 'en')
        blob = TextBlob(english_translation)
        sentiment = blob.sentiment
        if sentiment.polarity > 0:
            new_data_positive.append(data)
        elif sentiment.polarity < 0:
            new_data_negative.append(data)
        else:
            new_data_neutral.append(data)

docName = "sentiments.csv"

csv_datas = zip(old_data_positive, old_data_negative, old_data_neutral,
                new_data_positive, new_data_negative, new_data_neutral)

with open(docName, "w", newline="", encoding="utf-8") as docc:
    writerr = csv.writer(docc)

    writerr.writerow(["Old Data Positive", "Old Data Negative", "Old Data Neutral",
                     "New Data Positive", "New Data Negative", "New Data Neutral"])

    for veri in csv_datas:
        writerr.writerow(veri)

print("Datas written to CSV ")

