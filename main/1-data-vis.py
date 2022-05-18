import justpy as jp
import pandas 
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt
data = pandas.read_csv("./data/CC26Slack.csv" , parse_dates=["Date"])
daily_members_average = data[["Date","Total enabled membership","Daily active members","Daily members posting messages","Messages posted"]]
data["Weekday"] = data["Date"].dt.strftime("%A")
data["Daynumber"] = data["Date"].dt.strftime("%w")
weekday_avrg = data.groupby(["Weekday","Daynumber"]).mean()
weekday_avrg = weekday_avrg.sort_values("Daynumber")

chart = """
{
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
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Users'
        },
        labels: {
        format: '{value}'
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

chart_Users = """
{
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
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Users'
        },
        labels: {
        format: '{value}'
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
        color: '#70ffb3',
        data: [],
    }],   
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
    #Changing data from HighCHarts python data structures 
    hc.options.xAxis.categories = list(daily_members_average["Date"].dt.strftime("%Y-%m-%d"))
    hc.options.yAxis.categories = list(daily_members_average["Total enabled membership"])
    hc.options.series[0].data = list(daily_members_average["Daily active members"])
    hc.options.series[1].data = list(daily_members_average["Daily members posting messages"])
    
    #Average Users per Week
    h2 = jp.QDiv(a=web_page,text ="Average Users Weekly", classes = "text-h3 text-center q-pa-md")
    hc2 = jp.HighCharts(a=web_page, options=chart_Users)
    hc2.options.xAxis.categories = list(weekday_avrg.index.get_level_values(0))
    hc2.options.yAxis.categories = list(daily_members_average["Total enabled membership"])
    hc2.options.series[0].data = list(weekday_avrg["Daily active members"])
    
    return web_page



#Deploys webapp 
jp.justpy(app)

