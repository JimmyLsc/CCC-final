<template>
  <div id="piecharts2" class="educhart"></div>
</template>

<script>
export default {
  props: {
    education: {
      type: Array,
      // eslint-disable-next-line vue/require-valid-default-prop
      default: []
    },
    loaded: {
      type: Boolean,
      default: false
    }
  },

  data () {
    return {
      chart: null,
      option: null
    }
  },
  // 如果pieChartData 更新了值则需要刷新数据
  watch: {
    education: {
      handler (newVal, oldVal) {
        console.log('hello')
        if (this.education) {
          if (newVal) {
            this.option.series[0].data = newVal
            // this.option.legend.data = newVal.name
            this.chart.setOption(this.option, true)
          } else {
            this.option.series[0].data = this.oldVal
            // this.option.legend.data = this.oldVal.name
            this.chart.setOption(oldVal, true)
          }
        } else {
          this.init()
        }
      },
      deep: true // 对象内部属性的监听，关键。
    },
    loaded: {
      handler (newVal, oldVal) {
        if (newVal === false) {
          this.chart.showLoading()
        } else {
          this.chart.hideLoading()
        }
      },
      deep: true // 对象内部属性的监听，关键。
    }
  },

  mounted () {
    this.drawECharts()
  },
  name: 'piechart2',
  methods: {
    drawECharts () {
      let myChart = this.$echarts.init(
        document.getElementById('piecharts2'),
        'temp'
      )
      this.chart = myChart
      this.chart.showLoading()
      this.option = {
        tooltip: {
          trigger: 'item',
          formatter: '{a} <br/>{b}: {c} ({d}%)'
        },
        legend: {
          orient: 'vertical',
          left: 10,
          // eslint-disable-next-line no-undef
          data: this.education.name,
          textStyle: {
            color: 'white'
          }
        },
        series: [
          {
            name: 'Education Distribution',
            type: 'pie',
            radius: ['50%', '70%'],
            avoidLabelOverlap: false,
            label: {
              show: false,
              position: 'center'
            },
            emphasis: {
              label: {
                show: true,
                fontSize: '30',
                fontWeight: 'bold'
              }
            },
            labelLine: {
              show: false
            },
            // eslint-disable-next-line no-undef
            data: this.education
          }
        ]
      }

      if (this.option && typeof this.option === 'object') {
        this.chart.setOption(this.option, true)
        window.onresize = function () {
          console.log('resizing now ')
          myChart.resize()
        }
      }
    }
  }
}
</script>

<style scoped>
.educhart {
  width: 100%;
  height: 400px;
}
</style>
