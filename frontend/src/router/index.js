import { createRouter, createWebHistory } from 'vue-router'
// main pages
import LoginView from '@/views/LoginView.vue'
import DashboardView from '@/views/DashboardView.vue'
import ProjectsView from '@/views/Project/ProjectsView.vue'
import BudgetView from '@/views/Budget/BudgetView.vue'
import ExpensesView from '@/views/Expense/ExpensesView.vue'
import ArchivesView from '@/views/Archive/ArchivesView.vue'
import PortalView from '@/views/Portal/PortalView.vue'
import PersonnelView from '@/views/Personnel/PersonnelView.vue'
// sub pages
import CertificateGenerator from '@/views/Project/CertificateGenerator.vue'
import ProjectsByYear from '@/views/Project/ProjectsByYear.vue'
import SKMonitor from '@/views/Project/SKMonitor.vue'

const routes = [
  {
    path: '/',
    redirect: '/login'
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginView,
    meta: { hideLayout: true }
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: DashboardView,
    meta: { 
      showInSidebar: true,
      title: 'Dashboard',
      icon: 'mdi-view-dashboard',
      order: 1
    }
  },
  {
    path: '/projects',
    name: 'Projects',
    component: ProjectsView,
    meta: { 
      showInSidebar: true,
      title: 'Project Management',
      icon: 'mdi-folder-table-outline',
      order: 2,
      tabs: [
        { name: 'Projects', route: '/projects', default: true },
        { name: 'Certificate Generator', route: '/projects/certificate-generator' },
        { name: 'Projects by Year', route: '/projects/projects-by-year' },
        { name: 'Project Monitor', route: '/projects/monitor' }
      ]
    }
  },
  {
    path: '/budget',
    name: 'Budget',
    component: BudgetView,
    meta: { 
      showInSidebar: true,
      title: 'Budget Preparation',
      icon: 'mdi-currency-usd',
      order: 3,
      tabs: [
        { name: 'Line Items', route: '/budget', default: true },
        { name: 'Needs Assessment', route: '/budget/needs-assessment' },
        { name: 'SK Monitor', route: '/budget/monitor' }
      ]
    }
  },
  {
    path: '/expenses',
    name: 'Expenses',
    component: ExpensesView,
    meta: { 
      showInSidebar: true,
      title: 'Expense Verification',
      icon: 'mdi-google-analytics',
      order: 4,
      tabs: [
        { name: 'Current Verifications', route: '/expenses', default: true },
        { name: 'Past Verifications', route: '/expenses/past-verifications' },
        { name: 'Verifications Monitoring', route: '/expenses/monitor' },
      ]
    }
  },
  {
    path: '/archives',
    name: 'Archives',
    component: ArchivesView,
    meta: { 
      showInSidebar: true,
      title: 'Archives',
      icon: 'mdi-archive-outline',
      order: 5
    }
  },
  {
    path: '/portal',
    name: 'Portal',
    component: PortalView,
    meta: { 
      showInSidebar: true,
      title: 'Portal',
      icon: 'mdi-view-compact-outline',
      order: 6
    }
  },
  {
    path: '/personnel',
    name: 'Personnel',
    component: PersonnelView,
    meta: { 
      showInSidebar: true,
      title: 'Personnel',
      icon: 'mdi-account-group',
      order: 7
    }
  },
  // child routes
  {
    path: '/projects/certificate-generator',
    name: 'Certificate-Generator',
    component: CertificateGenerator,
    meta: {
      parentRoute: '/projects',
      title: 'Certificate Generator'
    }
  },
  { 
    path: '/projects/projects-by-year',
    name: 'Projects-By-Year',
    component: ProjectsByYear,
    meta: {
      parentRoute: '/projects',
      title: 'Projects By Year'
    }
  },
  {
    path: '/projects/monitor',
    name: 'SK-Monitor',
    component: SKMonitor,
    meta: {
      parentRoute: '/projects',
      title: 'SK Monitor'
    }
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router
