<template>
  <div>
    <b-card-group deck id="card-table">
      <div v-for="drink in drinks" :key="drink.id">
        <DrinkCard :drink="drink" />
      </div>
    </b-card-group>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";
import DrinkCard from "@/components/DrinkCard.vue";
import ApiService from "@/controllers/ApiService";
import { Drink } from "@/models/Drink";

@Component({
  components: { DrinkCard }
})
export default class DrinkTable extends Vue {
  private apiService: ApiService = new ApiService();

  @Prop() private title!: string;
  @Prop() private limit!: number;
  @Prop() private drinks: Array<Drink> = [];

  async mounted() {
    const promises: Array<Promise<Drink>> = [];
    for (let i = 0; i < this.limit; i++) {
      const drink: Promise<Drink> = this.apiService.getDrink();
      promises.push(drink);
    }
    this.drinks = await Promise.all(promises);
  }
}
</script>

<style scoped>
#card-table {
  display: flex;
  padding-bottom: 5%;
  padding-top: 5%;
  margin-left: auto;
  margin-right: auto;
  margin-top: auto;
  margin-bottom: auto;
}

.card-deck {
  display: flex;
  justify-content: center;
}
</style>
