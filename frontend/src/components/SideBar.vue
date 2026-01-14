<template>
  <div>
    <v-navigation-drawer permanent>
      <v-list nav>
        <v-list-item
          v-for="route in navigationRoutes"
          :key="route.path"
          :to="route.path"
          :value="route.path"
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
import { useRouter } from 'vue-router'

const router = useRouter()

const navigationRoutes = computed(() => {
  return router.getRoutes()
    .filter(r => r.meta?.showInSidebar)
    .sort((a, b) => (a.meta.order || 999) - (b.meta.order || 999))
})
</script>

<style scoped>
</style>

<style scoped>
.sidebar {
  width: 250px;
  background-color: #ffffff;
  padding: 24px;
  border-right: #e5e7eb 1px solid;
}
v-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
</style>