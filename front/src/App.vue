<template>
  <div id="app">
    <Navbar></Navbar>
    <Home> </Home>
  </div>
</template>

<script>
import Home from "@/components/Home.vue";
import Navbar from "@/components/Navbar.vue";

export default {
  name: 'App',
  components: {
    Home,
    Navbar,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
