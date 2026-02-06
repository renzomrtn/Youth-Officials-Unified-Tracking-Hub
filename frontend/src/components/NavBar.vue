<template>
    <div class="navbar">
        <p>branding</p>
        <p>breadcrumb</p>
        <p>mode</p>
        <p>account</p>
    </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()
const emit = defineEmits(['toggle-sidebar'])

const toggleSidebar = () => {
  emit('toggle-sidebar')
}

const breadcrumbs = computed(() => {
  const crumbs = []

  // 1. Check if the current route has a parent defined in meta
  if (route.meta && route.meta.parentRoute) {
    const parent = router.getRoutes().find(r => r.path === route.meta.parentRoute)
    if (parent) {
      crumbs.push({
        title: parent.meta.title || parent.name,
        path: parent.path
      })
    }
  }

  // 2. Add the current route
  if (route.meta && route.meta.title) {
    crumbs.push({
      title: route.meta.title,
      path: route.path
    })
  } else if (route.name) {
    crumbs.push({
      title: route.name,
      path: route.path
    })
  }

  return crumbs
})
</script>

<style scoped>
.navbar {
  background-color: #f8fafd;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px 24px 16px 0;
}

.navbar-icon-container {
  width: 64px;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-shrink: 0;
}

.branding-container {
  display: flex;
  align-items: center;
  gap: 10px;
}

.navbar-logo {
  height: 52px;
  width: auto;
}

.vertical-divider {
  width: 2.5px;
  height: 50px;
  background-color: #000;
}

.branding-text-group {
  display: flex;
  flex-direction: column;
  justify-content: center;
  line-height: 1.3;
}

.main-title {
  font-size: 22px;
  font-weight: 600;
  margin: 0;
  letter-spacing: -0.5px;
  color: #000;
}

.sub-title {
  font-size: 12px;
  font-weight: 500;
  margin: 0;
  color: #333;
  white-space: nowrap;
}

/* Breadcrumb Styles */
.breadcrumb-container {
  display: flex;
  align-items: center;
  flex-grow: 1;
  margin-left: 40px;
  gap: 4px;
}

.breadcrumb-wrapper {
  display: flex;
  align-items: center;
  gap: 4px;
}

.breadcrumb-item {
  margin: 0;
  color: #757575; /* Grey for parent/inactive */
  font-size: 20px;
  font-weight: 400;
}

.active-crumb {
  color: #000; /* Black for current page */
  font-weight: 600;
}

.breadcrumb-separator {
  color: #bdbdbd;
}

.navbar-right {
  display: flex;
  align-items: center;
  gap: 20px;
}

.branding {
    color: 000000;
    display: flex;
    justify-content: center;
    align-items: center;
}

.brand-image {
    width: 3rem;
}

.vl {
  border-left: 6px solid rgb(0, 0, 0);
  height: 100%;
  margin: 0 5px 0 5px;
}
</style>