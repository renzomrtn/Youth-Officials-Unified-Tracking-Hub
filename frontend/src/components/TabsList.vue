<template>
  <v-tabs 
    v-if="tabs.length > 0" 
    v-model="activeTab" 
    color="#174499"
    align-tabs="start"
    class="custom-tabs"
    height="60"
  >
    <v-tab 
      v-for="item in tabs" 
      :key="item.route"
      :value="item.route"
      @click="navigateToTab(item.route)"
      class="tab-item"
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

const tabs = computed(() => {
  const currentPath = route.path
  const parentPath = route.meta.parentRoute || currentPath
  const parentRoute = router.options.routes.find(r => r.path === parentPath)
  return parentRoute?.meta?.tabs || []
})

const navigateToTab = (tabRoute) => {
  if (tabRoute !== route.path) {
    router.push(tabRoute)
  }
}

const setActiveTab = () => {
  const currentPath = route.path
  const matchingTab = tabs.value.find(tab => tab.route === currentPath)
  
  if (matchingTab) {
    activeTab.value = matchingTab.route
  } else {
    const defaultTab = tabs.value.find(tab => tab.default)
    activeTab.value = defaultTab?.route || tabs.value[0]?.route
  }
}

watch(() => route.path, () => setActiveTab())
onMounted(() => setActiveTab())
</script>

<style scoped>
.custom-tabs {
  border-bottom: 1px solid #e0e0e0;
  background-color: #ffffff;
  padding-left: 32px; 
}

:deep(.v-tab__slider) {
  height: 4px !important; 
  border-radius: 4px 4px 0 0;
}

.v-tab.v-tab--selected {
  font-weight: 700 !important;
  color: #174499 !important;
}

.tab-item {
  font-family: 'Source Sans 3', sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.8px;
  font-size: 15px;
  padding: 0 20px;
  display: flex;
  align-items: center;
}
</style>