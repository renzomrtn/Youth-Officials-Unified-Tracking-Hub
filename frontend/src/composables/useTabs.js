import { computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'

/**
 * Composable for managing dynamic tabs
 * @returns {Object} Tab management utilities
 */
export function useTabs() {
  const route = useRoute()
  const router = useRouter()

  /**
   * Get tabs for current subsystem
   */
  const currentTabs = computed(() => {
    const currentPath = route.path
    const parentPath = route.meta.parentRoute || currentPath
    const parentRoute = router.options.routes.find(r => r.path === parentPath)
    return parentRoute?.meta?.tabs || []
  })

  /**
   * Check if current page has tabs
   */
  const hasTabs = computed(() => currentTabs.value.length > 0)

  /**
   * Get parent subsystem info
   */
  const parentSubsystem = computed(() => {
    const parentPath = route.meta.parentRoute || route.path
    return router.options.routes.find(r => r.path === parentPath)
  })

  /**
   * Get active tab
   */
  const activeTab = computed(() => {
    return currentTabs.value.find(tab => tab.route === route.path)
  })

  /**
   * Navigate to a tab
   */
  const navigateToTab = (tabRoute) => {
    if (tabRoute !== route.path) {
      router.push(tabRoute)
    }
  }

  return {
    currentTabs,
    hasTabs,
    parentSubsystem,
    activeTab,
    navigateToTab
  }
}