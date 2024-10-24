<template>
  <div class="home">
    <div id="nav">
      <div class="nav-center">
        <h1 class="title">Drinks Menu</h1>
      </div>
    </div>
    <DrinkTable title="Drinks Menu" :limit="12" />
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import DrinkTable from "@/components/DrinkTable.vue"; // @ is an alias to /src

@Component({
  components: { DrinkTable }
})
export default class Home extends Vue { }
</script>

<style>
#nav {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #333;
  /* Darker background for navigation */
  padding: 30px;
  /* Or your desired padding */
  font-weight: bold;
  color: #fff;
}

h1 .nav-center {
  font-family: 'Playfair Display', serif;
  /* Or your chosen serif font */
  margin-bottom: 20px;
  border-bottom: 3px solid #f0f0f0;
}
</style>