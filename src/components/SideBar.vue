<template>
  <div>
    <!-- Navigation Drawer -->
    <v-navigation-drawer 
      app 
      class="my-drawer" 
      clipped 
      permanent 
      :rail="miniDrawer"
      :width="240"
    >
      <div class="text-right pa-2">
        <v-btn
          icon
          variant="text"
          @click="toggleMiniDrawer"
          size="small"
        >
          <v-icon color="#021E3E" size="24" :style="{ fontWeight: 'bold' }">mdi-menu</v-icon>
        </v-btn>
      </div>
      
      <div class="pa-4 text-center" v-if="!miniDrawer">
        <img src="@/assets/appLogo2.png" alt="app logo" style="max-width: 100%;" />
      </div>

      <!-- Scrollable content area -->
      <div class="scrollable-content">
        <v-list>
          <!-- Dashboard Item -->
          <v-list-item prepend-icon="mdi-home" :title="miniDrawer ? '' : 'Dashboard'" nav to="/dashboard"
            :class="{ 'v-list-item--active': $route.path === '/dashboard' }" />
          
          <!-- Main Menu Divider -->
          <div class="menu-divider" v-if="!miniDrawer">
            <span class="divider-label">Main Menu</span>
          </div>
          <div v-else class="mini-divider"></div>
          
          <!-- Main Menu Items -->
          <v-list-item prepend-icon="mdi-account-group" :title="miniDrawer ? '' : 'Project Management'" 
            nav @click="handleNavigation('Project Management')"
            :class="{ 'v-list-item--active': $route.path.startsWith('/project') }">
            <template v-slot:subtitle v-if="!miniDrawer">
              <div class="subtitle-wrapper">Project Management</div>
            </template>
          </v-list-item>
          
          <v-list-item prepend-icon="mdi-receipt-text" :title="miniDrawer ? '' : 'Budget Preparation'" 
            nav @click="handleNavigation('Budget Preparation')"
            :class="{ 'v-list-item--active': $route.path.startsWith('/budget') }">
            <template v-slot:subtitle v-if="!miniDrawer">
              <div class="subtitle-wrapper">Budget Preparation</div>
            </template>
          </v-list-item>
          
          <v-list-item prepend-icon="mdi-file-document-multiple" :title="miniDrawer ? '' : 'Expense Verification'" 
            nav @click="handleNavigation('Expense Verification')"
            :class="{ 'v-list-item--active': $route.path.startsWith('/documents') }">
            <template v-slot:subtitle v-if="!miniDrawer">
              <div class="subtitle-wrapper">Expense Verification</div>
            </template>
          </v-list-item>

          <!-- Updated Analytics item to handle all analytics-related routes -->
          <v-list-item prepend-icon="mdi-google-analytics" :title="miniDrawer ? '' : 'Archives'" nav to="/archives"
            :class="{ 'v-list-item--active': $route.path === '/archives' }" />
          <v-list-item prepend-icon="mdi-bank" :title="miniDrawer ? '' : 'Portal'" nav to="/Portal"
            :class="{ 'v-list-item--active': $route.path === '/portal' }" />
          <v-list-item prepend-icon="mdi-help-box" :title="miniDrawer ? '' : 'Personnel'" nav to="/Personnel"
            :class="{ 'v-list-item--active': $route.path === '/personnel' }" />
        </v-list>
      </div>
    </v-navigation-drawer>

    <v-snackbar v-model="snackbar" :color="snackbarColor">
      {{ snackbarMessage }}
    </v-snackbar>
  </div>
</template>

<script>
</script>

<style scoped>
.my-drawer {
  display: flex;
  flex-direction: column;
  height: 100vh;
  position: relative;
  transition: width 0.3s ease;
}

.scrollable-content {
  flex: 1;
  overflow-y: auto;
}

.v-list-item.v-list-item--active {
  position: relative;
  color: white !important;
}

.v-list-item.v-list-item--active::before {
  content: '';
  position: absolute;
  top: 0;
  bottom: 0;
  left: 12px;
  right: 12px;
  background-color: #6E9DD4;
  border-radius: 8px;
  z-index: -1;
}

.v-list-item {
  padding-left: 16px !important;
  padding-right: 16px !important;
  min-height: 40px;
}

.subtitle-wrapper {
  white-space: normal;
  overflow: visible;
  text-overflow: clip;
  line-height: 1.2;
  font-size: 0.8rem;
  max-width: 100%;
}

.menu-divider {
  position: relative;
  height: 40px;
  display: flex;
  align-items: center;
  padding: 0 16px;
  margin-top: 8px;
  margin-bottom: 4px;
}

.menu-divider::before {
  content: '';
  position: absolute;
  left: 16px;
  right: 16px;
  top: 50%;
  height: 1px;
  background-color: rgba(0, 0, 0, 0.12);
}

.mini-divider {
  height: 1px;
  margin: 8px 8px;
  background-color: rgba(0, 0, 0, 0.12);
}

.divider-label {
  position: relative;
  background-color: #f5f5f5;
  padding: 0 8px;
  font-size: 0.75rem;
  font-weight: 600;
  color: rgba(0, 0, 0, 0.6);
  margin-left: 8px;
  z-index: 1;
}

.primary-color {
  background-color: #4A6782 !important;
  color: white !important;
}
</style>