import pandas as pd
import plotly.express as px

F= pd.read_csv('data/data.csv') 
mean1= F.groupby(['student_id','level'],as_index = False)['attempt'].mean()
# print(mean1)
figure = px.scatter(mean1,x="student_id",y="level",size="attempt",color="attempt",title="Student’s performances in each level.")
figure.show()