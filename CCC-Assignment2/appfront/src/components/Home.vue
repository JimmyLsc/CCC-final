<template>
  <div class="home">
    <header_com></header_com>
      <button v-on:click="greet">Greet</button>
    <el-row display="margin-top:10px">
        <el-input v-model="input" placeholder="请输入书名" style="display:inline-table; width: 30%; float:left"></el-input>
        <el-button type="primary" @click="addBook" style="float:left; margin: 2px;">新增</el-button>
    </el-row>
    <el-row>
        <el-input placeholder="" v-model="result" :disabled="true" style="width: 100%; float:left">
    </el-input>
    </el-row>
  </div>

</template>

<script>
import header from '../part/header'

export default {
  name: 'Home',
  data: function () {
    return {
      input: '',
      name: 'Vue.js'
    }
  },
  components: {
    header_com: header
  },

  methods: {
    greet: function (event) {
      // `this` inside methods points to the Vue instance
      alert('Hello ' + this.name + '!')
      console.log('hello!')
      // `event` is the native DOM event
      if (event) {
        alert(event.target.tagName)
      }
    },

    addBook () {
      console.log('succcuess')
      this.$http.get('http://127.0.0.1:8000/api/add_book?book_name=' + this.input)
        .then((response) => {
          var res = JSON.parse(response.bodyText)
          console.log(res)
          console.log(response)
          if (res.error_num === 0) {
            this.result = res['msg']
          } else {
            this.$message.error('新增书籍失败，请重试')
            console.log(res['msg'])
          }
        })
    }

  }
}
</script>
