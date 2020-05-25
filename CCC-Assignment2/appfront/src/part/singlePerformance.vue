<template>
<div>
  <dv-border-box-3 class="border-box-content">
    <div class="container-item">
        <div class="box-item-subtitle">
            <dv-decoration-11 style="width:300px;height:80px;" class="title">Performance for Instance {{instance.instance_num}}</dv-decoration-11>
        </div>

      <div class="box-item1">
        <p class="item">CPU-Usage</p>
         <usage :cpu_usage="instance.cpu_usage" :id="instance.instance_num"></usage>
      </div>

      <dv-decoration-2 style="height:5px;display: block;" />
      <div class="box-item">
        <p class="item">Number of CPU</p>
        <dv-decoration-9 style="width:150px;height:150px;color:#fff">
          <p>{{instance.cpu_num}}</p>
        </dv-decoration-9>
      </div>

      <dv-decoration-2 style="height:5px;display: block;" />
      <div class="box-item">
        <p class="item">Memory Usage</p>
        <dv-decoration-9 style="width:150px;height:150px;color:#fff">
          <p>{{instance.storage_usage}}%</p>
        </dv-decoration-9>
      </div>

      <dv-decoration-2 style="height:5px;display: block;" />
      <div class="box-item last-item">
        <p class="item">Disk Usage</p>
        <dv-decoration-9 style="width:150px;height:150px;color:#fff">
          <p>{{instance.disk_usage}}%</p>
        </dv-decoration-9>
      </div>
    </div>
  </dv-border-box-3>
</div>
</template>

<script>

import usage from '../components/usage'
export default {
  name: 'singlePerformace',
  props: {
    instance: {
      type: Array,
      // eslint-disable-next-line vue/require-valid-default-prop
      default: {
        'instance_num': 1,
        'cpu_num': 2,
        'storage_usage': 18.1,
        'cpu_usage': 15.1,
        'disk_usage': 16.6
      }
    }
  },
  components: {
    usage
  }
}
</script>

<style scoped>
.container-item {
  width:460px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-around;

}
.box-item1{
    width: 100%;
}
.box-item {
    margin-bottom: 10px;
}
.item{
    color:white;
}
.box-item-subtitle{
    margin-top:50px;
    height:100px;
    width: 80%;
    font-size:30px;
}
</style>
