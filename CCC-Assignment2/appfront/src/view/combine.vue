<template>
    <div class='combine'>
        <dv-border-box-11 title="Twitter analysis" style="padding-top:100px">
            <el-button type="info" @click="goBack" icon="el-icon-arrow-left" style="margin-bottom: 20px">GoBack</el-button>
            <div class="box">
                <combineData :loaded="loaded" :combineInfo="combineInfo"></combineData>
            </div>
        </dv-border-box-11>
    </div>
</template>

<script>
import combineData from '../part/combineData'
export default {
  name: 'combine',
  data () {
    return {
      loaded: false,
      combineInfo:
      {
        education: {
          name: 'High Education Proportion',
          type: 'bar',
          data: [
            0.106092,
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
    this.getCombineData()
    setInterval(() => {
      this.getCombineData()
      console.log('hi')
      console.log(this.combineInfo.education.data)
    }, 10000)
  },
  methods: {
    getCombineData () {
      this.axios.get('/api/tweet/get_combine_data').then(response => {
        this.loaded = true
        this.combineInfo = response.data
      })
    },
    goBack () {
      this.$router.push('/analysis')
    }
  },
  components: {
    combineData
  }
}
</script>

<style scoped>
.combine{
  width: 100%;
  background-color: black;
}
.box{
    width:100%;
    height: 800px;
}
</style>
