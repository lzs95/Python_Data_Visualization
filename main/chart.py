import justpy as jp
import pandas 
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt
data = pandas.read_csv("./data/CC26Slack.csv" , parse_dates=["Date"])
daily_members_average = data[["Date","Total enabled membership","Daily active members","Daily members posting messages","Messages posted"]]

chart = """{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Slack Chat'
    },
    subtitle: {
        text: ''
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Date'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 30 users.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Users'
        },
        labels: {
            format: '{value}°'
        },
        accessibility: {
            rangeDescription: ''
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: ' {point.y} active users'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Users',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}
"""

def app():
    web_page = jp.QuasarPage()
    #Quasar Division
    h2 = jp.QDiv(a=web_page,text ="CC26 SlackChat Analysis", classes = "text-h2 text-center q-pa-md")
    p1 = jp.QDiv(a=web_page,text = "Active members")
    hc = jp.HighCharts(a=web_page, options=chart)
    #Changing data from HighCHarts pythn data structures 
    hc.options.xAxis.categories = list(daily_members_average["Date"])
    # hc.options.yAxis.categories = list(daily_members_average.index)
    hc.options.series[0].data = list(zip(daily_members_average["Date"].dt.date,daily_members_average["Daily active members"]))
    
    return web_page



#Deploys webapp 
jp.justpy(app)