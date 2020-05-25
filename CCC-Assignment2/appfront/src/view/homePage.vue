<template>
    <div class='homePage'>
      <vue-particles style="width:100%; height: 100%; position: absolute" color="#dedede"
                   :particleOpacity="0.7"
                   :particlesNumber="80"
                   shapeType="circle"
                   :particleSize="4"
                   linesColor="#dedede"
                   :linesWidth="1"
                   :lineLinked="true"
                   :lineOpacity="0.4"
                   :linesDistance="150"
                   :moveSpeed="3"
                   :hoverEffect="true"
                   hoverMode="grab"
                   :clickEffect="true"
                   clickMode="push">
    </vue-particles>
    <div class="login">
      <div class="login-center">
        <dv-border-box-7 style="padding-top:20px; padding-bottom:20px">
        <p>CCC Assignment 2<br>Using Twitter and Aurin to Analyze Data</p>
          <li>Team Member:
            <ul>893060 Shuhua Zhang</ul>
            <ul>935209 Shuai Mou</ul>
            <ul>962546 Yicheng Jin</ul>
            <ul>961002 Shuocheng Li</ul>
            <ul>830789 Ningjing Wang</ul>
          </li>
        <el-button @click="openPage">Begin Your Journey Here</el-button>
        </dv-border-box-7>
      </div>
    </div>
</template>

<script>
export default {
  name: 'homePage',
  methods: {
    openPage () {
      this.$router.push('/analysis')
    }
  }
}
</script>

<style scoped>
 .homePage {
    width: 100%;
    height: 100%;
    position:absolute;
    background-color: black;
    background-repeat: non-repeat;
    background-size: cover;
    padding-bottom: 5%;
  }
   .login {
    position: relative;
    width: 600px;
    margin: 0 auto;
    z-index: 100000;
   }
  .login-center {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin-top: 100px;
    z-index: 100000;
  }
  p {
    font-size: 30px;
    color: white;
  }
  li {
    font-size: 30px;
    color: white;
  }
</style>
