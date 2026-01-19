<script setup>
import { RouterView, useRoute } from 'vue-router'
import { computed, ref } from 'vue'
import NavBar from './components/NavBar.vue'
import SideBar from './components/SideBar.vue'

const route = useRoute()
const showSidebar = computed(() => !route.meta.hideLayout)
const showNavBar = computed(() => !route.meta.hideLayout)

const sidebarOpen = ref(true)
</script>

<template>
  <v-app>
    <NavBar v-if="showNavBar" @toggle-sidebar="sidebarOpen = !sidebarOpen" />

    <v-layout>
      <SideBar v-if="showSidebar" :is-open="sidebarOpen" />

      <v-main class="main-content">
        <RouterView />
      </v-main>
    </v-layout>
  </v-app>
</template>

<style scoped>
.main-content {
  background-color: white;
  margin: 0 8px 8px 0;
  border-radius: 12px;
  min-height: calc(100vh - 80px);
}
</style>