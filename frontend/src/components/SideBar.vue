<template>
  <div class="sidebar">
    <v-navigation-drawer permanent>
      <v-list>
        <v-list-item
          v-for="route in navigationRoutes"
          :key="route.path"
          :to="route.path"
          :active="isActiveRoute(route.path)"
          color="primary"
        >
          <template v-slot:prepend v-if="route.meta?.icon">
            <v-icon>{{ route.meta.icon }}</v-icon>
          </template>
          <v-list-item-title>{{ route.meta?.title || route.name }}</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRouter, useRoute } from 'vue-router'

const router = useRouter()
const route = useRoute()

// Filter routes that should appear in the sidebar
const navigationRoutes = computed(() => {
  return router.getRoutes().filter(r => r.meta?.showInSidebar)
})

const isActiveRoute = (path) => {
  return route.path === path || route.path.startsWith(path + '/')
}
</script>

<style scoped>
.sidebar {
  background-color: aqua;
  padding: 24px;
}
v-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
</style>