<template>
  <div id="card">
    <b-card class="text-center" :title="drink.name" :img-src="drink.img" img-top>
      <b-card-text>{{ drink.instructions }}</b-card-text>
    </b-card>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";
import { Drink } from "../models/Drink";

@Component
export default class DrinkCard extends Vue {
  @Prop()
  private drink!: Drink;
}
</script>

<style scoped>
#card {
  max-width: 300px;
  height: auto;
}
</style>