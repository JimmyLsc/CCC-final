<template>
  <div id="piecharts" class="myecharts"></div>
</template>

<script>
export default {
  props: {
    election: {
      type: Array,
      // eslint-disable-next-line vue/require-valid-default-prop
      default: [
        {value: 80, name: '云南'},
        {value: 5, name: '北京'},
        {value: 15, name: '山东'},
        {value: 25, name: '河北'},
        {value: 20, name: '江苏'},
        {value: 35, name: '浙江'},
        {value: 30, name: '四川'},
        {value: 40, name: '湖北'}
      ]
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
    election: {
      handler (newVal, oldVal) {
        console.log('hello')
        if (this.election) {
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
  name: 'piechart',
  methods: {
    // 调用后段借口获取最新的信息
    // applyData () {
    //   this.axios.get('http://127.0.0.1:8000/api/get_geodata').then(response => {
    //     var res = response.data
    //     if (res.error_num === 0) {
    //       this.pieChartData = res['pieChartData']
    //       this.option.series[0].data = this.pieChartData
    //       this.option.legend.data = this.pieChartData.name
    //       this.chart.setOption(this.option, true)
    //     } else {
    //       this.$message.error('failed')
    //     }
    //   })
    // },

    drawECharts () {
      let myChart = this.$echarts.init(
        document.getElementById('piecharts'),
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
          data: this.election.name,
          textStyle: {
            color: 'white'
          }
        },
        series: [
          {
            name: 'Political Party Voting Distribution',
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
            data: this.election
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
.myecharts {
  width: 100%;
  height: 50vh;
}
</style>
