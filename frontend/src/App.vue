<script setup>
import { RouterView, useRoute } from 'vue-router'
import { computed } from 'vue'
import NavBar from './components/NavBar.vue'
import SideBar from './components/SideBar.vue'

const route = useRoute()
const showSidebar = computed(() => !route.meta.hideLayout)
</script>

<template>
  <v-app>
    <NavBar />
    <v-main>
      <SideBar v-if="showSidebar" />
      <RouterView />
    </v-main>
  </v-app>
</template>

<style scoped>
v-app {
  height: 100vh;
  display: flex;
  flex-direction: column;
}

v-main {
  flex: 1;
  display: flex;
}
</style>