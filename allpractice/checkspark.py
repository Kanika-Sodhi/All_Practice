import re
import string
import pandas as pd

a_string = '!hi. wh?at is the weat[h]er lik?e.'
new_string = re.sub(r'[^\w\s]', '', a_string)
print(new_string)

data = [['Alex$!*%', 10], ['Bob_)&', 12], ['Clarke', 13]]
df = pd.DataFrame(data, columns=['Name', 'Age'])


def remove_punctuations(text):
    for punctuation in string.punctuation:
        text = text.replace(punctuation, '')
    return text


# Apply to the DF series
df['Name'] = df['Name'].apply(remove_punctuations)
print(df)
