<template>
    <div :id="id" class="myUsage"></div>
</template>

<script>
export default {
  props: {
    cpu_usage: {
      type: Number,
      // eslint-disable-next-line vue/require-valid-default-prop
      default: 0
    },
    id: {
      type: Number
    }
  },
  mounted () {
    this.drawECharts()
  },
  watch: {
    cpu_usage: {
      handler (newVal, oldVal) {
        console.log('hello')
        if (this.cpu_usage) {
          if (newVal) {
            this.cpu_usage = newVal
            var newInfo = [{value: newVal, name: 'cpu_usage'}]
            this.option.series[0].data = newInfo
            console.log(this.cpu_info)
            console.log(newVal + '>>')
            console.log(this.cpu_usage)
            // this.option.legend.data = newVal.name
            this.chart.setOption(this.option, true)
          } else {
            this.option.series[0].data = this.oldVal
            // this.option.legend.data = this.oldVal.name
            this.chart.setOption(oldVal, true)
          }
        }
      },
      deep: true // 对象内部属性的监听，关键。
    }
  },
  data () {
    return {
      chart: null,
      option: null,
      cpu_info: [{value: this.cpu_usage, name: 'cpu_usage'}]
    }
  },
  name: 'usage',
  methods: {
    drawECharts () {
      let myChart = this.$echarts.init(
        document.getElementById(this.id)
      )
      this.chart = myChart
      this.chart.showLoading()
      this.option = {
        tooltip: {
          formatter: '{a} <br/>{b} : {c}%'
        },
        series: [
          {
            name: 'CPU Usage',
            type: 'gauge',
            detail: {formatter: '{value}%'},
            data: this.cpu_info,
            textStyle: {
              color: 'white'
            }
          }
        ]
      }

      this.chart.setOption(this.option, true)
      this.chart.hideLoading()
      window.onresize = function () {
        console.log('resizing now ')
        myChart.resize()
      }
    }
  }
}

</script>

<style scoped>
.myUsage{
    width:100%;
    height: 400px;
}
</style>
