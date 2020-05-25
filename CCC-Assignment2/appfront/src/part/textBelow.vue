<template>
    <div>
      <div class="paragraph">
            <dv-decoration-11 style="width:500px;height:80px; margin-top:20px" class="title">Recent Positive Emotion Text</dv-decoration-11>
            <ol>
              <li>{{TextData_pos[0]}}</li>
              <li>{{TextData_pos[1]}}</li>
              <li>{{TextData_pos[2]}}</li>
              <li>{{TextData_pos[3]}}</li>
              <li>{{TextData_pos[4]}}</li>
            </ol>
            <dv-decoration-11 style="width:500px;height:80px;" class="title">Recent Negtive Emotion Text</dv-decoration-11>
            <ol>
              <li>{{TextData_neg[0]}}</li>
              <li>{{TextData_neg[1]}}</li>
              <li>{{TextData_neg[2]}}</li>
              <li>{{TextData_neg[3]}}</li>
              <li>{{TextData_neg[4]}}</li>
            </ol>
            <dv-decoration-11 style="width:500px;height:80px;" class="title">Recent Positive Emotion Text About China</dv-decoration-11>
            <ol>
              <li>{{TextData_china_pos[0]}}</li>
              <li>{{TextData_china_pos[1]}}</li>
              <li>{{TextData_china_pos[2]}}</li>
              <li>{{TextData_china_pos[3]}}</li>
              <li>{{TextData_china_pos[4]}}</li>
            </ol>
            <dv-decoration-11 style="width:500px;height:80px;" class="title">Recent Negtive Emotion Text About China</dv-decoration-11>
            <ol>
              <li>{{TextData_china_neg[0]}}</li>
              <li>{{TextData_china_neg[1]}}</li>
              <li>{{TextData_china_neg[2]}}</li>
              <li>{{TextData_china_neg[3]}}</li>
              <li>{{TextData_china_neg[4]}}</li>
            </ol>
      </div>
    </div>
</template>

<script>
export default {
  name: 'textBelow',
  props: {
    TextData_pos: {
      type: Array,
      // eslint-disable-next-line vue/require-valid-default-prop
      default: [
        '@smerkaliscious Lol ok but I’ve had some GNs 👍🏼😜 - I’d love to hun but not sure if I can cross the boarders yet - b… https://t.co/8H7wdNKMTI',
        '@DancingDanB @MoVidaMelbourne When I was there I found it easier to find good vegetarian food in Barcelona, than an… https://t.co/YuBqrOT4py',
        '@Dococtplays All good my man \nI’m just trying to connect with good people 🤙🏽',
        '@kayenini Awesome  hun - don’t let 1 person that can’t take a joke put you off - the true genuine friends will stick by you and enjoy - 👍🏼❤️',
        '@mrcjohnston @3RRRFM The Rasta shorts getting a work out in iso CJ? Hope ya well cobs 🐨🦁❤️'

      ]
    },
    TextData_neg: {
      type: Array,
      // eslint-disable-next-line vue/require-valid-default-prop
      default: [
        "@ujaybaba Bro I'm wheezing right now 😭😭😭",
        "@ujaybaba Bro I'm wheezing right now 😭😭😭",
        '@ProudSocialist Yeah. \nIt’s always been fucking ugly... take it from the rest of the world who have got the shits with you lot...😤',
        'Trump Tests Extremely Negative for Corona: https://t.co/ab1RLmXvhd \n#COVID19',
        'In three words describe the left. \n- Hypocrites\n- Liars\n- Degenerates'

      ]
    },
    TextData_china_pos: {
      type: Array,
      // eslint-disable-next-line vue/require-valid-default-prop
      default: [
      ]
    },
    TextData_china_neg: {
      type: Array,
      // eslint-disable-next-line vue/require-valid-default-prop
      default: [
      ]
    }
  }
}
</script>
<style scoped>
p{
    color: white;
    margin-bottom: 30px;
}
li{
  color: white;
  margin-bottom: 30px;
  margin-left:0PX;
  text-align: left;
}
.title{
    margin-top:30 px;
}
.paragraph{
  margin-left: 25%;
  margin-right: 25%;
  margin-top: 20px;
  margin-bottom: 50px;
}
</style>
