<template>
  <dv-border-box-3 class="border-box-content">
    <div class="container-item">
        <div class="box-item-subtitle">
            <dv-decoration-11 style="width:200px;height:60px;" class="title">MAJOR FINDINGS</dv-decoration-11>
        </div>
      <div class="box-item">
        <p class="item">Tasmania</p>
        <dv-decoration-9 style="width:150px;height:150px;color:#fff">
         <p>{{dataObj[0].data1}}</p>
        </dv-decoration-9>
      </div>
      <dv-decoration-2 style="height:5px;display: block;" />
      <div class="box-item">
        <p class="item">New South Wale</p>
        <dv-decoration-9 style="width:150px;height:150px;color:#fff">
          <p>{{dataObj[1].data2}}</p>
        </dv-decoration-9>
      </div>
      <dv-decoration-2 style="height:5px;display: block;" />
      <div class="box-item last-item">
        <p class="item">Victoria</p>
        <dv-decoration-9 style="width:150px;height:150px;color:#fff">
          <p>{{dataObj[2].data3}}</p>
        </dv-decoration-9>
      </div>
    </div>
  </dv-border-box-3>
</template>

<script>
export default {
  props: {
    // data: {
    //   type: Array,
    //   // eslint-disable-next-line vue/require-valid-default-prop
    //   default: [
    //     {data1: 300},
    //     {data2: 500},
    //     {data3: 400}
    //   ]
    // }
  },
  data () {
    return {
      dataObj: [
        {data1: 300},
        {data2: 200},
        {data3: 300}
      ]
    }
  },
  created () {
    console.log(this.dataObj[0].data1)
  },
  name: 'rightGraph'

}
</script>
<style scoped>
.container-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-around;
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
    width: 400px;
    font-size:30px;
}
</style>
