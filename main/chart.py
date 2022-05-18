import justpy as jp
import pandas 
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt
data = pandas.read_csv("./data/CC26Slack.csv" , parse_dates=["Date"])
daily_members_average = data[["Date","Total enabled membership","Daily active members","Daily members posting messages","Messages posted"]]

chart = """{
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
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Users'
        },
        lineWidth: 2
    },
    legend: {
    layout: 'vertical',
    align: 'right',
    verticalAlign: 'middle'
    },
    
     xAxis: {
        title: {
            text: 'Date'
        },
        lineWidth: 2
    },
    legend: {
    layout: 'vertical',
    align: 'right',
    verticalAlign: 'middle'
    },
    
 
  
    series: [{
        name: 'Users',
        data: []
    },
    {
        name: 'Users Posting Messages',
        data: [],
        color: '#ff9496',
    }
    ],   
    responsive: {
    rules: [{
      condition: {
        maxWidth: 500
      },
      chartOptions: {
        legend: {
          layout: 'horizontal',
          align: 'center',
          verticalAlign: 'bottom'
        }
      }
    }]
  }
}
"""

def app():
    web_page = jp.QuasarPage()
    #Quasar Division
    h2 = jp.QDiv(a=web_page,text ="CC26 SlackChat Analysis", classes = "text-h2 text-center q-pa-md")
    #HighCharts
    hc = jp.HighCharts(a=web_page, options=chart)
    #Changing data from HighCHarts pythn data structures 
    hc.options.xAxis.categories = list(daily_members_average["Date"].dt.strftime("%Y-%m-%d"))
    hc.options.yAxis.categories = list(daily_members_average["Total enabled membership"])
    hc.options.series[0].data = list(daily_members_average["Daily active members"])
    hc.options.series[1].data = list(daily_members_average["Daily members posting messages"])
    
    return web_page



#Deploys webapp 
jp.justpy(app)

#  plotOptions: {
#     series: {
#       label: {
#         connectorAllowed: false
#       },
#       pointStart: 2010
#       }
#     },