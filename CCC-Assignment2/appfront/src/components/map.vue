<template>
  <div class="container mt-4">
     <dv-decoration-11 style="width:80%;height:80px;" class="title">Percentage of Chinese Population Over the State Population</dv-decoration-11>
    <div class="map-container border rounded">
      <!--地圖呈現在此-->
      <div class="google-map" id="map1"></div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'map',
  props: {
    mapName: {
      type: String,
      default: 'state.json'
    },
    mapData: {
      type: Array
    },
    mapTitle: {
      type: Map
    },
    maxValue: {
      type: Number
    }
  },
  data () {
    return {
      mapAddress: '../static/' + this.mapName
    }
  },
  mounted () {
    this.initMap()
    // this.setMarker();
  },
  methods: {
    // 建立地圖
    initMap () {
      console.log('map created!')
      let myChart = this.$echarts.init(document.getElementById('map1'))
      myChart.showLoading()

      // eslint-disable-next-line no-undef
      this.axios.get(this.mapAddress).then(response => {
        myChart.hideLoading()
        console.log(response)
        console.log('map here!')
        let features = response.data.features
        console.log(response)
        features.forEach(element => {
          element.properties.name = element.properties.STATE_NAME
        })
        response.data.features = features
        // eslint-disable-next-line no-unused-vars
        this.$echarts.registerMap('vic', response.data)
        // eslint-disable-next-line no-unused-vars

        let option = {
          // title: {
          //     text: 'USA Population Estimates (2012)',
          //     subtext: 'Data from www.census.gov',
          //     sublink: 'http://www.census.gov/popest/data/datasets.html',
          //     left: 'right'
          // },
          title: this.mapTitle,
          tooltip: {
            trigger: 'item',
            showDelay: 0,
            transitionDuration: 0.2,
            formatter: function (params) {
              var value = (params.value * 100).toFixed(2) + '%'
              // value = value[0].replace(/(\d{1,3})(?=(?:\d{3})+(?!\d))/g, '$1,')
              return params.seriesName + '<br/>' + params.name + ': ' + value
            }
          },
          visualMap: {
            show: false,
            min: 0,
            max: 0.030982,
            inRange: {
              color: [
                '#313695',
                '#4575b4',
                '#74add1',
                '#abd9e9',
                '#e0f3f8',
                '#ffffbf',
                '#fee090',
                '#fdae61',
                '#f46d43',
                '#d73027',
                '#a50026'
              ]
            },
            text: ['High', 'Low'], // 文本，默认为数值文本
            calculable: false,
            textStyle: {
              color: 'white'
            }
          },
          series: [
            {
              name: 'Chinese people rate',
              type: 'map',
              roam: false,
              map: 'vic',
              emphasis: {
                label: {
                  show: true
                }
              },
              // 文本位置修正
              textFixed: {
                Alaska: [20, -20]
              },
              data: [
                {name: 'New South Wales', value: 0.030982},
                {name: 'Queensland', value: 0.009793},
                {name: 'South Australia', value: 0.014637},
                {name: 'Tasmania', value: 0.00607},
                {name: 'Northern Territory', value: 0.004734},
                {name: 'Victoria', value: 0.010755},
                {name: 'Australian Capital Territory', value: 0.028276},
                {name: 'Western Australia', value: 0.010755}
              ]
            }
          ]
        }
        if (option && typeof option === 'object') {
          myChart.setOption(option, true)
          window.onresize = function () {
            console.log('resizing now ')
            myChart.resize()
          }
        }
      })
    }
  }
}
</script>

<style scoped>
.google-map {
  width: 100%;
  height: 800px;
  margin-left: 50px;
}
.title {
    font-weight: 700;
    font-size: 20px;
    width: 200px;
    height: 60px;
    display: block;
    margin: 0 auto;
    color: white
  }
</style>
