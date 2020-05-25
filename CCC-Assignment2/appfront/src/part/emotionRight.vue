<template>
  <dv-border-box-3 class="border-box-content" style="padding-top: 20px">
    <div class="container-item">

        <dv-decoration-11 style="width:80%;height:80px; margin-top:10px;" class="title">Overall Emotion Analysis</dv-decoration-11>

      <div class="box-item">
          <emotion :LabelData="LabelData"></emotion>
      </div>
        <div class="box-item">
            <dv-decoration-2 style="height:5px;display: block;" />
        </div>
          <dv-decoration-11 style="width:80%;height:80px;" class="title">China Related Emotion Analysis for {{state}}</dv-decoration-11>
      <div class="box-item">
          <emotion :LabelData="LabelData_China"></emotion>
      </div>

    </div>
  </dv-border-box-3>
</template>

<script>
import emotion from '../components/emotion'
import map from '../components/map'
export default {
  name: 'emotionRight',
  props: {
    LabelData: {
      type: Array,
      // eslint-disable-next-line vue/require-valid-default-prop
      default: [
        {name: 'positive', value: '--'},
        {name: 'negative', value: '--'}
      ]
    },
    LabelData_China: {
      type: Array,
      // eslint-disable-next-line vue/require-valid-default-prop
      default: [
        {name: 'positive', value: '--'},
        {name: 'negative', value: '--'}
      ]
    },
    state: {
      type: String,
      default: 'Victoria'
    }

  },
  components: {
    emotion,
    map
  }

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
.box-item-subsubtitle{
    margin-top:50px;
    height:100px;
    width: 400px;
    font-size:20px;
}
</style>
