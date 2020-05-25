<template>
  <div id="analysis">
    <div class="home">
      <header_com></header_com>
      <el-row>
        <el-button type="primary" @click="getPieData('vic', 'Victoria')">Victoria</el-button>
        <el-button type="primary" @click="getPieData('nsw', 'New South Wales')">New South Wales</el-button>
        <el-button type="primary" @click="getPieData('tas', 'Tasmania')">Tasmania</el-button>
        <el-button type="primary" @click="getPieData('queens', 'Queensland')" >Queensland</el-button>
        <el-button type="primary" @click="getPieData('western', 'Western Australia')">Western Australia</el-button>
        <el-button type="primary" @click="getPieData('southern', 'South Australia')">South Australia</el-button>
        <el-button type="success" @click="goToCombine()">Overall analysis<i class="el-icon-arrow-right el-icon-right"></i></el-button>
        <el-button type="info" @click="goToPerformace()">Instance Info<i class="el-icon-arrow-right el-icon-right"></i></el-button>
      </el-row>
      <el-row type="flex" class="row-bg" justify="center">
        <!-- <el-col :span="2"><el-button type="primary" @click="getPieData" style="float:left; margin: 2px;">新增</el-button></el-col> -->
        <el-col :span="7">
          <leftGraph :loaded="loaded" :election="election" :education="education" :state="state"></leftGraph>
        </el-col>
        <el-col :span="11">
          <dv-border-box-8>
            <map_com></map_com>
          </dv-border-box-8>
        </el-col>
        <el-col :span="6">
            <emotionRight :LabelData="LabelData" :LabelData_China="LabelData_China" :state="state"></emotionRight>
        </el-col>
      </el-row>
      <el-row>
        <dv-border-box-10 style="width:100%; height:120%; padding-bottom: 20px; padding-top:20px">
        <textBelow :TextData_pos="TextData_pos" :TextData_neg="TextData_neg" :TextData_china_pos="TextData_china_pos" :TextData_china_neg="TextData_china_neg" style="margin-bottom:30px"></textBelow>
        </dv-border-box-10>
      </el-row>
    </div>
  </div>
</template>

<script>
import header from '../part/header'
import map from '../components/map'
import leftGraph from '../part/leftGraph'
import rightGraph from '../part/rightGraph'
import emotionRight from '../part/emotionRight'
import textBelow from '../part/textBelow'
export default {
  data () {
    return {
      loaded: false,
      election: [
        {name: 'labor party', value: 165394},
        {name: 'national coalition', value: 129032}
      ],
      education: [
        {name: 'has no qualification', value: 0.5378},
        {name: 'lower than bachelor qualification', value: 0.2760},
        {name: 'above bachelor degree', value: 0.1861}
      ],
      LabelData: [
        {name: 'positive', value: '--'},
        {name: 'negative', value: '--'}
      ],
      LabelData_China: [
        {name: 'positive', value: '--'},
        {name: 'negative', value: '--'}
      ],
      state: 'Victoria',
      TextData_pos: [ ],
      TextData_neg: [],
      TextData_china_pos: [],
      TextData_china_neg: []

    }
  },
  mounted () {
    this.getPieData('vic', 'Victoria')
  },
  name: 'analysis',
  components: {
    header_com: header,
    map_com: map,
    leftGraph,
    emotionRight,
    rightGraph,
    textBelow
    // piechart_com2: piechart
  },
  methods: {
    // 从后段调取接口更新数据
    getPieData (state, stateName) {
      console.log('I click!!')
      this.loaded = false
      this.hideNumber()
      this.axios.get('/api/tweet/get_data?state=' + state).then(response => {
        this.loaded = true
        console.log(window.location.host)
        var res = response.data
        this.state = stateName
        console.log(res)
        if (res.msg === 0) {
          this.election = res['election']
          console.log('>>>>' + this.election)
          this.education = res['education']
          console.log('>>>>' + this.education)
          this.LabelData = res['LabelData']
          this.LabelData_China = res['LabelData_China']
          this.TextData_pos = res['TextData_pos']
          this.TextData_neg = res['TextData_neg']
          this.TextData_china_pos = res['TextData_china_pos']
          this.TextData_china_neg = res['TextData_china_neg']
        }
      })
    },
    goToPerformace () {
      this.$router.push('/performance')
    },
    hideNumber () {
      this.LabelData = [
        {name: 'positive', value: '--'},
        {name: 'negative', value: '--'}
      ]
      this.LabelData_China = [
        {name: 'positive', value: '--'},
        {name: 'negative', value: '--'}
      ]
    },
    goToCombine () {
      this.$router.push('/combine')
    }
  }
}
</script>

<style scoped>
  /* html,body{
      margin:0;
      padding:0;
   } */

  .home {
    width: 100%;
    height: 100%;
    background-image: url(http://datav.jiaminghi.com/demo/electronic-file/img/bg.110420cf.png);
    background-repeat: non-repeat;
    background-size: cover;
    padding-bottom: 5%;
  }
  .el-button {
    width: 150px;
    margin-bottom: 20px;
    margin-top: 20px;
    margin-left: 50px;
  }
</style>
