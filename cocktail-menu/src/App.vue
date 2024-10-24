<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";

@Component
export default class App extends Vue { }
</script>

<style>
/* Overall Styles */
#app {
  font-family: 'Roboto', sans-serif;
  /* Example font: Roboto */
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  background-color: #2c3e50;
}

/* Title Styles */
h1,
h2,
h3 {
  font-family: 'Playfair Display', serif;
  /* Example serif font: Playfair Display */
  margin-bottom: 20px;
  /* Add space below the title */
}

h1 {
  border-bottom: 3px solid #f0f0f0;
  /* Add a solid border for the main title */
  padding-bottom: 10px;
  /* Add padding below the border */
}
</style>
