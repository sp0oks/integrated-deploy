<template>
  <div class="home">
    <DrinkTable title="Drinks Menu" :limit="12" />
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import DrinkTable from "@/components/DrinkTable.vue"; // @ is an alias to /src

@Component({
  components: { DrinkTable }
})
export default class Home extends Vue {}
</script>
