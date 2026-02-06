<template>
  <v-navigation-drawer
    :model-value="true"
    location="left"
    :rail="!isOpen"
    permanent
    :border="0"
    class="sidebar-drawer"
    color="#f8fafd"
  >
    <v-list nav>
      <v-list-item
        v-for="navRoute in navigationRoutes"
        :key="navRoute.path"
        :to="navRoute.path"
        :value="navRoute.path"
        :active="isRouteActive(navRoute)"
        active-color="#174499"
        class="sidebar-item"
      >
        <template #prepend v-if="navRoute.meta?.icon">
          <v-icon class="sidebar-icon">{{ navRoute.meta.icon }}</v-icon>
        </template>

        <v-list-item-title class="sidebar-title">
          {{ navRoute.meta?.title || navRoute.name }}
        </v-list-item-title>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>

<script setup>
import { computed } from 'vue'
import { useRouter, useRoute } from 'vue-router'

const props = defineProps({
  isOpen: {
    type: Boolean,
    default: true
  }
})

const router = useRouter()
const currentRoute = useRoute()

const navigationRoutes = computed(() => {
  return router.getRoutes()
    .filter(r => r.meta?.showInSidebar)
    .sort((a, b) => (a.meta.order || 999) - (b.meta.order || 999))
})

const isRouteActive = (navRoute) => {
  const currentPath = currentRoute.path
  const navPath = navRoute.path
  
  if (currentPath === navPath) return true
  
  if (currentRoute.meta?.parentRoute === navPath) return true
  
  return false
}
</script>

<style scoped>
:deep(.v-navigation-drawer__content) {
  --sidebar-font-size: 15.5px; 
}

.sidebar-drawer {
  height: 100vh !important;
}

.v-list {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  padding: 10px;
}

.sidebar-title {
  font-family: 'Source Sans 3', sans-serif !important;
  font-size: var(--sidebar-font-size) !important;
  font-weight: 500;
  letter-spacing: 0.015em;
}

.sidebar-icon {
  font-size: calc(var(--sidebar-font-size) + 6px) !important;
  opacity: 0.7;
}

.sidebar-item {
  min-height: 50px !important; 
  border-radius: 8px !important;
  margin-bottom: 2px;
  transition: all 0.2s ease;
}

.sidebar-item.v-list-item--active {
  background-color: #174499 !important;
  color: white !important;
  opacity: 1 !important;
  box-shadow: 0 4px 8px rgba(23, 68, 153, 0.15);
}

.sidebar-item.v-list-item--active .sidebar-title {
  font-weight: 700 !important;
  color: white !important;
}

.sidebar-item.v-list-item--active .sidebar-icon {
  color: white !important;
  opacity: 1 !important;
}

.sidebar-item:not(.v-list-item--active):hover {
  background-color: rgba(0, 0, 0, 0.04) !important;
}
</style>