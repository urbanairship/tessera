module ts {
  export module models {
    export class SimpleTimeSeries extends Chart {
      static meta: DashboardItemMetadata = {
        item_type: 'simple_time_series',
        display_name: 'Simple Time Series',
        icon: 'fa fa-line-chart',
        category: 'chart',
        template: ds.templates.models.simple_time_series
      }

      filled: boolean = false
      show_max_value: boolean = false
      show_min_value: boolean = false
      show_last_value: boolean = false

      constructor(data?: any) {
        super(data)
        if (data) {
          this.legend = data.legend
          this.filled = Boolean(data.filled)
          this.show_max_value = Boolean(data.show_max_value)
          this.show_min_value = Boolean(data.show_min_value)
          this.show_last_value = Boolean(data.show_last_value)
          this.height = 1
        }
      }

      toJSON() : any {
        return $.extend(super.toJSON(), {
          filled: this.filled,
          show_max_value: this.show_max_value,
          show_min_value: this.show_min_value,
          show_last_value: this.show_last_value
        })
      }

      data_handler(query: ts.models.data.Query) : void {
        if (item.filled) {
          ds.charts.simple_area_chart($('#' + this.item_id + ' .ds-graph-holder'), this, query)
        } else {
          ds.charts.simple_line_chart($('#' + this.item_id + ' .ds-graph-holder'), this, query)
        }
      }

      interactive_properties() : PropertyListEntry[] {
        return super.interactive_properties().concat([
          { name: 'filled', type: 'boolean' },
          { name: 'show_max_value', type: 'boolean' },
          { name: 'show_min_value', type: 'boolean' },
          { name: 'show_last_value', type: 'boolean' }
        ])
      }
    }
    ts.models.register_dashboard_item(SimpleTimeSeries)
  }
}