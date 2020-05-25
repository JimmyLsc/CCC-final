<template>
    <div class="header-wrap">
      <div class="header-left">
        <dv-decoration-8 style="width:300px;height:50px;" />
      </div>
      <div class="header-title">
        <h1 class="title">Performance Analysis</h1>
        <dv-decoration-5 style="width:800px;height:40px;" />
      </div>
      <div class="header-right">
        <dv-decoration-8 :reverse="true" style="width:300px;height:50px;" />
      </div>
  </div>

</template>

<script>
export default {
  name: 'header'
}
</script>

<style scoped>
.header-wrap {
  width: 100%;
  display: flex;
  justify-content: space-between;
  }

.title {
  color: white;
  text-align: center;
  font-size: 50px;
  padding-top: 10px;
  width:800px;
}
</style>
