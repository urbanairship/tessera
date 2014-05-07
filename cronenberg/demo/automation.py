import json
import sys
from ..model import *
from ..model.database import *



def demo_automation_overview():
    return database.Dashboard(
        title='Overview',
        category='Automation',
        summary='A high level summary of automation',
        tags=[ Tag('automation'), Tag('summary'), Tag('executive'), Tag('featured') ],
        definition = DashboardDef(
            definition=dumps(
                DashboardDefinition(
                    queries = {
                        'total_events_processed': 'alias(sumSeries(nonNegativeDerivative(servers.{s0306,s0307}.rash.triggers-gorram-consumer.argonmutationconsumer_timer.device_open_processed.Count),nonNegativeDerivative(servers.{s0306,s0307}.rash.triggers-gorram-consumer.argonmutationconsumer_meter.totalmutationsreceived.Count),nonNegativeDerivative(servers.{s0306,s0307}.rash.triggers-state-ingress.immediatetriggerauditlog.observation_latency.Count)),"Total Event Count")',

                                    'total_triggers_satisfied': 'alias(sumSeries(nonNegativeDerivative(sumSeries(servers.{s0306,s0307}.rash.triggers-state-ingress.observationstreamconsumer.historical_triggers_satisfied.Count)),nonNegativeDerivative(sumSeries(servers.{s0306,s0307}.rash.triggers-state-ingress.observationstreamconsumer.immediate_triggers_satisfied.Count))),"Total Triggers Satisfied Count")',

        'api_rate': 'group(alias(sumSeries(scaleToSeconds(nonNegativeDerivative(servers.{s0189,s0188}.rash.push-api.pipelineendpointmetrics.total_request_count.Count), 1)),"API Total Request Rate"),alias(sumSeries(nonNegativeDerivative(servers.{s0189,s0188}.rash.push-api.pipelineendpointmetrics.total_request_count.Count)),"API Total Request Count"))',
                        'historical_triggers': 'group(alias(scaleToSeconds(nonNegativeDerivative(sumSeries(servers.{s0306,s0307}.rash.triggers-state-ingress.observationstreamconsumer.historical_triggers_processed.Count)), 1),"Historical Triggers Processed Rate"),alias(nonNegativeDerivative(sumSeries(servers.{s0306,s0307}.rash.triggers-state-ingress.observationstreamconsumer.historical_triggers_processed.Count)),"Historical Triggers Processed Count"),alias(scaleToSeconds(nonNegativeDerivative(sumSeries(servers.{s0306,s0307}.rash.triggers-state-ingress.observationstreamconsumer.historical_triggers_satisfied.Count)), 1),"Historical Triggers Satisfied Rate"),alias(nonNegativeDerivative(sumSeries(servers.{s0306,s0307}.rash.triggers-state-ingress.observationstreamconsumer.historical_triggers_satisfied.Count)),"Historical Triggers Satisfied Count"))',
                        'device_event_rate': 'alias(sumSeries(scaleToSeconds(nonNegativeDerivative(servers.{s0306,s0307}.rash.triggers-gorram-consumer.argonmutationconsumer_timer.device_open_processed.Count), 1)),"Device Open Rate")',
                        'api_latency': 'alias(averageSeries(maxSeries(servers.{s0189,s0188}.rash.push-api.pipelineendpointmetrics.postpipelinetimer.Mean),maxSeries(servers.{s0189,s0188}.rash.push-api.pipelineendpointmetrics.postvalidatetimer.Mean),maxSeries(servers.{s0189,s0188}.rash.push-api.pipelineendpointmetrics.putpipelinetimer.Mean),maxSeries(servers.{s0189,s0188}.rash.push-api.pipelineendpointmetrics.deletepipelinetimer.Mean),maxSeries(servers.{s0189,s0188}.rash.push-api.pipelineendpointmetrics.getpipelinetimer.Mean),maxSeries(servers.{s0189,s0188}.rash.push-api.pipelineendpointmetrics.getlimitstimer.Mean),maxSeries(servers.{s0189,s0188}.rash.push-api.pipelineendpointmetrics.listpipelinetimer.Mean),maxSeries(servers.{s0189,s0188}.rash.push-api.pipelineendpointmetrics.listdeletedpipelinetimer.Mean)),"/api/pipelines, Average Latency")',
                        'total_triggers_processed': 'alias(sumSeries(nonNegativeDerivative(sumSeries(servers.{s0306,s0307}.rash.triggers-state-ingress.observationstreamconsumer.historical_triggers_processed.Count)),nonNegativeDerivative(sumSeries(servers.{s0306,s0307}.rash.triggers-state-ingress.observationstreamconsumer.immediate_triggers_processed.Count))),"Total Triggers Processed Count")',
                        'total_push_rate': 'group(alias(sumSeries(scaleToSeconds(nonNegativeDerivative(servers.{s0306,s0307}.rash.triggers-fulfillment.pushfulfillmenthandler.total_push_count.Count), 1),scaleToSeconds(nonNegativeDerivative(servers.{s0306,s0307}.rash.triggers-fulfillment.delayedpushfulfillmenthandler.total_delayed_push_count.Count), 1)),"Total Push Rate"),alias(sumSeries(scaleToSeconds(nonNegativeDerivative(servers.{s0306,s0307}.rash.triggers-fulfillment.pushfulfillmenthandler.total_push_count.Count), 1)),"Push Rate"),alias(sumSeries(scaleToSeconds(nonNegativeDerivative(servers.{s0306,s0307}.rash.triggers-fulfillment.delayedpushfulfillmenthandler.total_delayed_push_count.Count), 1)),"Delayed Push Rate"))',
                        'immediate_triggers': 'group(alias(scaleToSeconds(nonNegativeDerivative(sumSeries(servers.{s0306,s0307}.rash.triggers-state-ingress.observationstreamconsumer.immediate_triggers_processed.Count)), 1),"Immediate Triggers Processed Rate"),alias(nonNegativeDerivative(sumSeries(servers.{s0306,s0307}.rash.triggers-state-ingress.observationstreamconsumer.immediate_triggers_processed.Count)),"Immediate Triggers Processed Count"),alias(scaleToSeconds(nonNegativeDerivative(sumSeries(servers.{s0306,s0307}.rash.triggers-state-ingress.observationstreamconsumer.immediate_triggers_satisfied.Count)), 1),"Immediate Triggers Satisfied Rate"),alias(nonNegativeDerivative(sumSeries(servers.{s0306,s0307}.rash.triggers-state-ingress.observationstreamconsumer.immediate_triggers_satisfied.Count)),"Immediate Triggers Satisfied Count"))',
                        'end_to_end': 'group(alias(maxSeries(servers.{s0306,s0307}.rash.triggers-fulfillment.controller.pipeline_end_to_end_delivery_time.Mean),"End to End Delivery, Mean Latency"),alias(maxSeries(servers.{s0306,s0307}.rash.triggers-fulfillment.controller.pipeline_end_to_end_delivery_time.99thPercentile),"End to End Delivery, 99th% Latency"))',
                        'stacked_test': 'group(alias(sumSeries(servers.{s0306,s0307}.rash.triggers-fulfillment.pushpayloadmetrics.pushcount.all.Count),"All Push Count"),alias(diffSeries(sumSeries(servers.{s0306,s0307}.rash.triggers-fulfillment.pushpayloadmetrics.pushcount.all.Count),sumSeries(servers.{s0306,s0307}.rash.triggers-fulfillment.pushpayloadmetrics.pushfeaturetype_richpush.payload.Count)),"Regular Push Count"),alias(sumSeries(servers.{s0306,s0307}.rash.triggers-fulfillment.pushpayloadmetrics.pushfeaturetype_richpush.payload.Count),"Rich Push Count"))',
                        'total_pushes_sent': 'alias(sumSeries(nonNegativeDerivative(servers.{s0306,s0307}.rash.triggers-fulfillment.pushfulfillmenthandler.total_push_count.Count),nonNegativeDerivative(servers.{s0306,s0307}.rash.triggers-fulfillment.delayedpushfulfillmenthandler.total_delayed_push_count.Count)),"Push Count")'
                    },
                    items=[
                        Section(layout=Section.Layout.FIXED,
                                  items=[
                                      Row(items=[
                                          Cell(span=3, style=DashboardItem.Style.WELL, align='center',
                                               items=SingleStat(title='Raw Events Processed',
                                                                query='total_events_processed',
                                                                format=',.0f',
                                                                transform='sum')),
                                          Cell(span=3, style=DashboardItem.Style.WELL, align='center',
                                               items=SingleStat(title='Triggers Processed',
                                                                query='total_triggers_processed',
                                                                format=',.0f',
                                                                transform='sum')),
                                          Cell(span=3, style=DashboardItem.Style.WELL, align='center',
                                               items=SingleStat(title='Triggers Satisifed',
                                                                query='total_triggers_satisfied',
                                                                format=',.0f',
                                                                transform='sum')),
                                          Cell(span=3, style=DashboardItem.Style.WELL, align='center',
                                               items=SingleStat(title='Pushes Sent',
                                                                query='total_pushes_sent',
                                                                format=',.0f',
                                                                transform='sum'))
                                      ])
                                  ]),
                        Section(layout=Section.Layout.NONE,
                                items=[
                                    StackedAreaChart(height=4,
                                                     query='total_push_rate')
                                ]),
                        Section(layout=Section.Layout.FIXED,
                                items=[
                                      Separator()
                                      ,Row(items=[
                                          Cell(span=4,
                                               items=JumbotronSingleStat(height=4,
                                                                         title='Average Push Rate',
                                                                         query='total_push_rate',
                                                                         transform='mean',
                                                                         units=' /sec'
                                                                     )),
                                          Cell(span=8,
                                               items=StandardTimeSeries(height=4,
                                                                        query='total_push_rate'))
                                      ])
                                      ,Row(items=[
                                          Cell(span=2, offset=2,
                                               items=SingleStat(title='Mean End to End Delivery Time',
                                                                query='end_to_end',
                                                                units=' ms',
                                                                format=',.0f',
                                                                transform='mean')),
                                          Cell(span=8, items=SimpleTimeSeries(query='end_to_end'))
                                      ])
                                      ,Heading('Trigger Details', description='Breakdown between immediate and historical')
                                      ,Separator()
                                      ,Row(items=[
                                          Cell(span=2,
                                               items=SingleStat(title='Immediate Triggers Processed',
                                                                query='immediate_triggers',
                                                                units='/sec',
                                                                format=',.2f')),
                                          Cell(span=2,
                                               items=SingleStat(title='Immediate Triggers Satisfied',
                                                                query='immediate_triggers',
                                                                units='/sec',
                                                                index=3,
                                                                format=',.2f')),
                                          Cell(span=8,
                                               items=SimpleTimeSeries(query='immediate_triggers'))
                                      ])
                                      ,Row(items=[
                                          Cell(span=2,
                                               items=SingleStat(title='Historical Triggers Processed',
                                                                query='historical_triggers',
                                                                units='/sec',
                                                                format=',.2f')),
                                          Cell(span=2,
                                               items=SingleStat(title='Historical Triggers Satisfied',
                                                                query='historical_triggers',
                                                                units='/sec',
                                                                index=3,
                                                                format=',.2f')),
                                          Cell(span=8,
                                               items=SimpleTimeSeries(query='historical_triggers'))
                                      ])
                                      ,Row(items=[
                                          Cell(span=2, offset=2,
                                               items=SingleStat(title='Mean Device Opens Rate',
                                                                query='device_event_rate',
                                                                units='/sec',
                                                                format=',.0f')),
                                          Cell(span=8,
                                               items=SimpleTimeSeries(query='device_event_rate'))
                                      ])
                                      ,Heading('API')
                                      ,Separator()
                                      ,Row(items=[
                                          Cell(span=2,
                                               items=SingleStat(title='Mean API Response Time',
                                                                query='api_latency',
                                                                units=' ms',
                                                                format=',.2f')),
                                          Cell(span=2,
                                               items=SingleStat(title='API Requests',
                                                                query='api_rate',
                                                                index=1,
                                                                format=',.0f',
                                                                transform='sum')),
                                          Cell(span=8,
                                               items=SimpleTimeSeries(query='api_rate'))
                                      ])
                                ])
                    ]))))
