<script setup>
import { RouterView, useRoute } from 'vue-router'
import { computed } from 'vue'
import NavBar from './components/NavBar.vue'
import SideBar from './components/SideBar.vue'

const route = useRoute()
const showSidebar = computed(() => !route.meta.hideLayout)
const showNavBar = computed(() => !route.meta.hideLayout)
</script>

<template>
  <v-app>
    <NavBar v-if="showNavBar" />

    <v-layout>
      <SideBar v-if="showSidebar" />

      <v-main>
        <RouterView />
      </v-main>
    </v-layout>
  </v-app>
</template>