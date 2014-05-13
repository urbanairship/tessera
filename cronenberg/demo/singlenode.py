import json
import sys
from ..model import *
from ..model.database import *

def demo_node_dashboard():
    return database.Dashboard(
        title='System Overview',
        summary='Summary of {{#if title}}{{title}}{{else}}{{ role }}{{/if}}',
        category='Demo',
        tags=[ Tag('template', bgcolor='lightblue', fgcolor='black') ],
        definition = DashboardDef(
            definition=dumps(
                DashboardDefinition(
                     queries = {
                         'cpu_usage' : 'aliasByNode(group(servers.{{clusto-query "role"}}.sysstat.cpu.all.system,servers.{{clusto-query "role"}}.sysstat.cpu.all.user,servers.{{clusto-query "role"}}.sysstat.cpu.all.io_wait), 1, 5)',
                         'loadavg' : 'aliasByNode(servers.{{clusto-query "role"}}.sysstat.loadavg.01, 1)',
                         'context' : 'aliasByNode(servers.{{clusto-query "role"}}.sysstat.context_switches.context_switches, 1)',
                         'processes' : 'aliasByNode(servers.{{clusto-query "role"}}.sysstat.loadavg.process_list_size, 1)',
                         'bytes_received' : 'aliasByNode(servers.{{clusto-query "role"}}.sysstat.network.*.bytes_rx,1,4)',
                         'tcp_establised' : 'aliasByNode(servers.{{clusto-query "role"}}.tcp.CurrEstab,1)',
                         'memory_usage' : 'asPercent(sumSeries(servers.{{clusto-query "role"}}.memory.Active),sumSeries(servers.{{clusto-query "role"}}.memory.MemTotal))',
                         'chef' : 'drawAsInfinite(servers.{{clusto-query "role"}}.chef.elapsed)'
                     },
                     items=Section(layout=Section.Layout.FIXED,
                                   items=[
                                       Row(items=[
                                           Cell(span=4, style=DashboardItem.Style.WELL,
                                                items=StandardTimeSeries(height=2, title='Load Average', query='loadavg'))
                                           ,Cell(span=4, style=DashboardItem.Style.WELL,
                                                 items=StandardTimeSeries(height=2, title='TCP Connections', query='tcp_establised'))
                                           ,Cell(span=4, style=DashboardItem.Style.WELL,
                                                 items=StandardTimeSeries(height=2, title='% Memory In Use', query='memory_usage'))
                                       ])
                                       #                        ,Row(Cell(span=2, offset=2, align='right', items=SingleStat(title='Cheffed', query='chef', transform='sum', units='times', format=',.0f'))
                                       #                             ,Cell(span=8, items=SimpleTimeSeries(query='chef')))
                                       ,Heading('CPU')
                                       ,Separator()
                                       ,Row(items=[
                                           Cell(span=2, align='center', items=SingleStat(query='cpu_usage', title='Max Usage', transform='max'))
                                           ,Cell(span=2, align='center', items=SingleStat(query='cpu_usage', title='Mean Usage', transform='mean'))
                                           ,Cell(span=8,
                                                 items=StackedAreaChart(title='CPU Usage',query='cpu_usage', options={
                                                     'yAxisFormat': ',.0f',
                                                     'palette' : 'd3category10'
                                                 }))
                                       ])
                                       ,Row(items=[
                                           Cell(span=2, align='center', items=SingleStat(query='loadavg', title='Max Load Average', transform='max'))
                                           ,Cell(span=2, align='center', items=SingleStat(query='loadavg', title='Mean Load Average', transform='mean'))
                                           ,Cell(span=8,
                                                 items=StandardTimeSeries(title='1 Minute Load Average',query='loadavg'))
                                       ])
                                       ,Row(items=[
                                           Cell(span=2, align='center', items=SingleStat(query='context', title='Max Context Switches',
                                                                                         transform='max', units='/sec',
                                                                                         format=',.2s'))
                                           ,Cell(span=2, align='center', items=SingleStat(query='context', title='Mean Context Switches',
                                                                                          transform='mean', units='/sec',
                                                                                          format=',.2s'))
                                           ,Cell(span=8,
                                                 items=StandardTimeSeries(title='Context Switches per Second',query='context', options={
                                                     'yAxisLabel' : 'Context Switches per Second',
                                                     'yAxisFormat' : ',.2s'
                                                 }))
                                       ])
                                       ,Row(items=[
                                           Cell(span=2, align='center', items=SingleStat(query='processes', title='Max Processes',
                                                                                         transform='max',
                                                                                        format=',.0f'))
                                           ,Cell(span=2, align='center', items=SingleStat(query='processes', title='Mean Processes',
                                                                                          transform='mean',
                                                                                          format=',.0f'))
                                           ,Cell(span=8,
                                                 items=StandardTimeSeries(title='Active Processes',query='processes', options={
                                                     'yAxisLabel' : 'Total # of Processes',
                                                     'yAxisFormat' : ',.0f'
                                                 }))
                                           ])
                                       ,Heading('Network')
                                       ,Separator()
                                       ,Row(items=[
                                           Cell(span=2, align='center', items=SingleStat(query='tcp_establised', title='Max Connections',
                                                                                         transform='max',
                                                                                         thresholds=Thresholds(warning=28000, danger=30000),
                                                                                         format=',.2s'))
                                           ,Cell(span=2, align='center', items=SingleStat(query='tcp_establised', title='Mean Connections',
                                                                                          transform='mean',
                                                                                          format=',.2s'))
                                           ,Cell(span=8, height=3,
                                                 items=StandardTimeSeries(title='TCP Connections Established',query='tcp_establised', options={
                                                     # 'yAxisLabel' : '# of Bytes/Second',
                                                     'yAxisFormat' : ',.2s'
                                                 }))
                                       ])
                                       ,Row(items=[
                                           Cell(span=2, align='center', items=SingleStat(query='bytes_received', title='Max',
                                                                                         transform='max',
                                                                                         units='/sec',
                                                                                         format=',.1s'))
                                           ,Cell(span=2, align='center', items=SingleStat(query='bytes_received', title='Sum',
                                                                                          transform='sum',
                                                                                          units='bytes',
                                                                                          format=',.1s'))
                                           ,Cell(span=8,
                                                 items=StackedAreaChart(title='Bytes Received',query='bytes_received', height=5,
                                                                        options={
                                                                            'yAxisLabel' : '# of Bytes/Second',
                                                                            'yAxisFormat' : ',.1s',
                                                                            'style' : 'stream'
                                                                  }))
                                       ])
                                   ])))))
