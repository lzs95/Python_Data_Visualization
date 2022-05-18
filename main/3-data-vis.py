import justpy as jp
import pandas 
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt
data = pandas.read_csv("./data/CC26Slack.csv" , parse_dates=["Date"])
daily_members_average = data[["Date","Total enabled membership","Daily active members","Daily members posting messages","Messages posted"]]

chart = """
{
  chart: {
    type: 'bar'
  },
  title: {
    text: 'Historic World Population by Region'
  },
  subtitle: {
    text: 'Source: <a href="https://en.wikipedia.org/wiki/World_population">Wikipedia.org</a>'
  },
  xAxis: {
    categories: ['Africa', 'America', 'Asia', 'Europe', 'Oceania'],
    title: {
      text: null
    }
  },
  yAxis: {
    min: 0,
    title: {
      text: 'Population (millions)',
      align: 'high'
    },
    labels: {
      overflow: 'justify'
    }
  },
  tooltip: {
    valueSuffix: ' millions'
  },
  plotOptions: {
    bar: {
      dataLabels: {
        enabled: true
      }
    }
  },
  legend: {
    layout: 'vertical',
    align: 'right',
    verticalAlign: 'top',
    x: -40,
    y: 80,
    floating: true,
    borderWidth: 1,
    backgroundColor:
      Highcharts.defaultOptions.legend.backgroundColor || '#FFFFFF',
    shadow: true
  },
  credits: {
    enabled: false
  },
  series: [{
    name: 'Year 1800',
    data: [107, 31, 635, 203, 2]
  }, {
    name: 'Year 1900',
    data: [133, 156, 947, 408, 6]
  }, {
    name: 'Year 2000',
    data: [814, 841, 3714, 727, 31]
  }, {
    name: 'Year 2016',
    data: [1216, 1001, 4436, 738, 40]
  }]
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