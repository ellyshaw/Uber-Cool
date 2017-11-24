import csv
import plotly.graph_objs as go
import numpy as np
from sklearn.svm import SVR
import plotly as py
py.tools.set_credentials_file(username='xx', api_key='xx')
import plotly.plotly as py


py.sign_in("xx", "xx")
dates = []
share = []


def get_data(filename):
    with open(filename, 'r') as csvfile:
        csvFileReader = csv.reader(csvfile)
        next(csvFileReader)
        for row in csvFileReader:
            dates.append(float(row[0]))
            share.append(float(row[1]))
    return


def predict_share(dates, share, x):
    dates = np.array(dates)[np.newaxis]
    dates = dates.T
    svr_poly = SVR(kernel='poly', C=1e3, degree=2)
    svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.001)
    svr_poly.fit(dates, share)
    lw = 2
    p1 = go.Scatter(x=dates, y=share,
                    mode='markers',
                    marker=dict(color='black'),
                    name='data')
    p2 = go.Scatter(x=dates, y=svr_rbf.predict(dates),
                    mode='lines',
                    line=dict(color='turquoise', width=lw))
    p3 = go.Scatter(x=futureDates, y=svr_rbf.predict(futureDates),
                    mode='lines',
                    line=dict(color='turquoise', width=lw))
    data = [p1, p2, p3]
    layout = go.Layout(title='Model S',
                       hovermode='closest',
                       xaxis=dict(title='Date'),
                       yaxis=dict(title='Sales', range=[0, 5])
                       )
    fig = go.Figure(data=data, layout=layout)
    py.iplot(fig)


get_data('data.csv')
futureDates = []
for i in range(30):
    futureDates.append(i+43)

futureDates = np.array(futureDates)[np.newaxis]
futureDates = futureDates.T
predicted_result = predict_share(dates, share, futureDates)
