<template>
    <div id="barChart" class="myBar"></div>
</template>

<script>
export default {
  name: 'combine',
  props: {
    loaded: false,
    combineInfo: {
      type: Array,
      // eslint-disable-next-line vue/require-valid-default-prop
      default:
      {
        education: {
          name: 'High Education Proportion',
          type: 'bar',
          data: [
            0.186092,
            0.180997,
            0.148639,
            0.159013,
            0.129748,
            0.140365
          ]
        },
        election: {
          name: 'Liberal National Coalition Proportion',
          type: 'bar',
          'data': [
            0.186092,
            0.180997,
            0.148639,
            0.159013,
            0.129748,
            0.140365
          ]
        },
        pos: {
          name: 'Overall Positive Tweet Proportion',
          type: 'line',
          data: [
            0.7184466019417476,
            0.7044025157232704,
            0.7924528301886793,
            0.8125,
            0,
            0.7746478873239436
          ]
        },
        china_pos: {
          name: 'Positive Tweet About China Proportion',
          type: 'line',
          data: [
            0,
            0,
            1.0,
            0,
            0,
            0
          ]
        }
      }
    }
  },
  mounted () {
    this.drawEcharts()
    console.log('hi')
  },
  data () {
    return {
      chart: null,
      option: null
    }
  },
  watch: {
    combineInfo: {
      handler (newVal, oldVal) {
        console.log('hello')
        if (this.combineInfo) {
          if (newVal) {
            this.option.series[0] = newVal.education
            this.option.series[1] = newVal.election
            this.option.series[2] = newVal.pos
            this.option.series[3] = newVal.china_pos
            console.log(newVal.education.data)
            // this.option.legend.data = newVal.name
            this.chart.setOption(this.option, true)
          } else {
            this.option.series = oldVal
            // this.option.legend.data = this.oldVal.name
            this.chart.setOption(this.option, true)
          }
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
  methods: {
    drawEcharts () {
      let myChart = this.$echarts.init(
        document.getElementById('barChart')
      )
      this.chart = myChart
      this.chart.showLoading()
      this.option = {
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'cross',
            crossStyle: {
              color: '#999'
            }
          }
        },
        toolbox: {
          feature: {
            magicType: {show: true, type: ['line', 'bar']},
            restore: {show: true},
            saveAsImage: {show: true}
          }
        },
        legend: {
          data: ['High Education Proportion', 'Liberal National Coalition Proportion', 'Overall Positive Tweet Proportion', 'Positive Tweet About China Proportion'],
          textStyle: {
            color: 'white'
          }
        },
        xAxis: [
          {
            type: 'category',
            data: ['Victoria', 'New South Wales', 'Tasmania', 'Queensland', 'Western Australia', 'South Australia'],
            axisPointer: {
              type: 'shadow'
            },
            axisLabel: { // X轴线 标签修改
              textStyle: {
                color: 'white' // 坐标值得具体的颜色
              }
            }
          }
        ],
        yAxis: [
          {
            type: 'value',
            name: 'Proportion',
            min: 0.0,
            max: 0.8,
            interval: 0.1,
            axisLabel: {
              formatter: '{value} %',
              textStyle: {
                color: '#fff'
              }
            }

          }
        ],
        series: [
          this.combineInfo.education,
          this.combineInfo.election,
          this.combineInfo.pos,
          this.combineInfo.china_pos
        ]
      }
      this.chart.setOption(this.option, true)
      console.log('hello')
      window.onresize = function () {
        console.log('resizing now ')
        myChart.resize()
      }
    }
  }
}
</script>

<style scoped>
.myBar{
    width:80%;
    height: 800px;
    margin-left: 10%;
    margin-right: 10%;
}
</style>
