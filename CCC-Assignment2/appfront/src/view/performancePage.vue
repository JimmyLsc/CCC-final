<template>
<div class="perform">
    <secondHeader></secondHeader>
    <el-row>
      <el-button type="info" @click="goBack" icon="el-icon-arrow-left">Back to Analysis</el-button>
    </el-row>
    <el-row type="flex" class="row-bg">
        <el-column :span="6">
          <!-- <rightGraph></rightGraph> -->
            <singlePerformance :instance="instance.instance1"></singlePerformance>
        </el-column>
        <el-column :span="6">
            <singlePerformance :instance="instance.instance2"></singlePerformance>
        </el-column>
        <el-column :span="6">
            <singlePerformance :instance="instance.instance3"></singlePerformance>
        </el-column>
        <el-column :span="6">
            <singlePerformance :instance="instance.instance4"></singlePerformance>
        </el-column>
    </el-row>
</div>
</template>

<script>
import singlePerformance from '../part/singlePerformance'
import rightGraph from '../part/rightGraph'
import secondHeader from '../part/secondHeader'

export default {
  name: 'performancePage',
  components: {
    singlePerformance,
    rightGraph,
    secondHeader
  },
  mounted () {
    this.getData()
    this.getDataRecursive()
  },
  data () {
    return {
      instance: {
        'instance1': {
          'instance_num': 1,
          'cpu_num': 2,
          'storage_usage': 18.1,
          'cpu_usage': 0,
          'disk_usage': 16.6
        },
        'instance2': {
          'instance_num': 2,
          'cpu_num': 3,
          'storage_usage': 18.1,
          'cpu_usage': 0,
          'disk_usage': 16.6
        },
        'instance3': {
          'instance_num': 3,
          'cpu_num': 2,
          'storage_usage': 18.1,
          'cpu_usage': 0,
          'disk_usage': 16.6
        },
        'instance4': {
          'instance_num': 4,
          'cpu_num': 2,
          'storage_usage': 18.1,
          'cpu_usage': 0,
          'disk_usage': 16.6
        }
      }

    }
  },
  methods: {
    goBack () {
      this.$router.push('/analysis')
    },
    getData () {
      this.axios.get('/api/information/send_info').then(response => {
        var res = response.data
        this.instance = res
      })
    },
    getDataRecursive () {
      setInterval(() => { this.getData() }, 5000)
    }
  }
}
</script>

<style scoped>
.perform{
  width: 2000px;
  height:100%;
  background-color: black;
}
</style>
