<template>
    <div>
        <el-row type="flex" class="row-bg" justify="center">
            <el-col>
                 <div class="container-item">
                    <div class="box-item">
                        <img :src='smileFace' style="width:100px;height:100px;margin-right: 40px" alt ="">
                    </div>
                </div>
            </el-col>
            <el-col>
                <img :src='sadFace' style="width:100px;height:100px" alt ="">
            </el-col>

        </el-row>
        <el-row type="flex" class="row-bg" justify="center">
            <el-col>
               <p style="font-size: 20px; color:#3de7c9; margin-right:10px"> Postive</p>
                <p class='item' style="font-size: 30px; color:#3de7c9; margin-right: 40px">{{LabelData[0].value}}</p>
            </el-col>
            <el-col>
                  <p style="font-size: 20px; color:#3de7c9;margin-left:5px"> Negative</p>
                 <p class='item' style="font-size: 30px; color:#3de7c9">{{LabelData[1].value}}</p>
            <el-col>
        </el-row>
    </div>
</template>

<script>
export default {
  name: 'emotion',
  props: {
    LabelData: {
      type: Array
    }
  },

  data () {
    return {
      smileFace: require('../assets/sad2.png'),
      sadFace: require('../assets/sad.png'),
      config1: {
        number: [100],
        content: '{nt}s'
      }

    }
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
</style>
