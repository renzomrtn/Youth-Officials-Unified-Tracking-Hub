<template>
  <v-tabs v-if="tabs.length > 0" v-model="activeTab" slider-color="secondary">
    <v-tab 
      v-for="item in tabs" 
      :key="item.route"
      :value="item.route"
      @click="navigateToTab(item.route)"
    >
      {{ item.name }}
    </v-tab>
  </v-tabs>
</template>

<script setup>
import { ref, computed, watch, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()
const activeTab = ref(null)

// Get tabs for the current subsystem
const tabs = computed(() => {
  // Find the parent route (main subsystem route)
  const currentPath = route.path
  const parentPath = route.meta.parentRoute || currentPath
  
  // Find the route that has tabs defined
  const parentRoute = router.options.routes.find(r => r.path === parentPath)
  
  return parentRoute?.meta?.tabs || []
})

// Navigate to selected tab
const navigateToTab = (tabRoute) => {
  if (tabRoute !== route.path) {
    router.push(tabRoute)
  }
}

// Set active tab based on current route
const setActiveTab = () => {
  const currentPath = route.path
  const matchingTab = tabs.value.find(tab => tab.route === currentPath)
  
  if (matchingTab) {
    activeTab.value = matchingTab.route
  } else {
    // If no exact match, set to default tab
    const defaultTab = tabs.value.find(tab => tab.default)
    activeTab.value = defaultTab?.route || tabs.value[0]?.route
  }
}

// Watch for route changes
watch(() => route.path, () => {
  setActiveTab()
})

// Initialize on mount
onMounted(() => {
  setActiveTab()
})
</script>