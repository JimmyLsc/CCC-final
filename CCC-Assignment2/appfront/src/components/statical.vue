<template>
    <div id="statical" class="myecharts"></div>
</template>

<script>
export default {
  props: {
    staticalData: {
      type: Array,
      // eslint-disable-next-line vue/require-valid-default-prop
      default: [
        ['number', 'amount', 'product'],
        [89.3, 58212, 'Matcha Latte'],
        [57.1, 78254, 'Milk Tea'],
        [74.4, 41032, 'Cheese Cocoa'],
        [50.1, 12755, 'Cheese Brownie'],
        [89.7, 20145, 'Matcha Cocoa'],
        [68.1, 79146, 'Tea'],
        [19.6, 91852, 'Orange Juice']
      ]
    }
  },
  data () {
    return {
      chart: null,
      option: null
    }
  },

  mounted () {
    this.drawECharts()
  },
  name: 'statical',
  methods: {
    drawECharts () {
      console.log('SUccess')
      this.chart = this.$echarts.init(
        document.getElementById('statical'),
        'temp'
      )
      console.log('SUccess!')
      this.option = {
        grid: {containLabel: true},
        xAxis: {
          name: 'amount',
          axisLine: {
            lineStyle: {
              color: 'white',
              width: 2
            }
          }
        },
        yAxis: {
          type: 'category',
          axisLine: {
            lineStyle: {
              color: 'white',
              width: 2
            }
          }
        },
        visualMap: {
          orient: 'horizontal',
          left: 'center',
          min: 10,
          max: 100,
          text: ['High Vote', 'Low Vote'],
          // Map the score column to color
          dimension: 0,
          textStyle: {
            color: 'white'
          },
          inRange: {
            color: ['#D7DA8B', '#E15457']
          }
        },
        series: [
          {
            type: 'bar',
            encode: {
              // Map the "amount" column to X axis.
              x: 'amount',
              // Map the "product" column to Y axis
              y: 'product'
            }
          }
        ],
        dataset: {
          source: this.staticalData
        }
      }

      if (this.option && typeof this.option === 'object') {
        this.chart.setOption(this.option, true)
        // window.addEventListener('resize', function () {
        //   this.chart.resize()
        // })
      }
    }
  }

}
</script>

<style scoped>
.myecharts {
  width: 450px;
  height: 500px;
}
</style>
