import pandas as pd
import matplotlib.pyplot as plt

data = [[1,'M',18,'Student','Banglore'],
        [2,'F',19,'Student','Chennai'],
        [3,'M',19,'Student','Delhi'],
        [4,'F',26,'Working professional','Chandigarh']
        ]

df = pd.DataFrame(data, columns = ['serial', 'Gender','Age','Occupation','Place'])
df.hist()
plt.show()