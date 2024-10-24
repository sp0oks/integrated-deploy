<template>
  <div id="card">
    <b-card class="text-center" :title="drink.name" :img-src="drink.img" img-top>
      <b-card-text>{{ truncateText(drink.instructions, 150) }}</b-card-text>
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

  // Method to truncate text and add "..."
  truncateText(text: string, maxLength: number): string {
    if (text.length > maxLength) {
      return text.substring(0, maxLength) + "...";
    }
    return text;
  }
}

</script>

<style scoped>
.card-container {
  display: flex;
  flex-direction: column;
  align-items: stretch;
  flex-wrap: wrap;
  /* Allow cards to wrap to multiple lines */
  justify-content: center;
  /* Center cards within the container */
}

#card {
  max-width: 300px;
  flex: 1;
  height: auto;
  margin-bottom: 15px;
  margin-top: 15px;
}

#card .card-text {
  font-size: 16px;
  line-height: 1.5;
  word-break: break-word;
  word-wrap: break-word;
}
</style>