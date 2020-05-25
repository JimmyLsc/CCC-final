<template>
  <div class="container-item">
    <div class="box-item">
      <dv-border-box-1>
        <dv-decoration-11 style="width:80%;height:100px;" class="title">Political Party Voting Distribution for {{state}}</dv-decoration-11>
        <piechart :loaded="loaded" :election="election"></piechart>
      </dv-border-box-1>
    </div>
    <div class="box-item">
      <dv-border-box-1 style="padding-top: 10px">
        <dv-decoration-11 style="width:80%;height:80px;" class="title">Education Distribution for {{state}}</dv-decoration-11>
        <piechart2 :loaded="loaded" :education="education"></piechart2>
      </dv-border-box-1>
    </div>
  </div>
</template>

<script>
import piechart from '../components/piechart'
import piechart2 from '../components/piechart2'
export default {
  props: {
    election: {
      type: Array
    },
    education: {
      type: Array
    },
    state: {
      type: String,
      default: 'vic'
    },
    loaded: {
      type: Boolean,
      default: false
    }
  },

  data () {
    return {
    }
  },
  name: 'left',
  components: {
    piechart,
    piechart2
  }
}
</script>
<style>
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
