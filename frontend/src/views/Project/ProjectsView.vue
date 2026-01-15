<template>
    <section class="content">
        <div class="tabs-list">
            <TabsList v-if="hasTabs" />
        </div>
        <div class="inner-content">
            <v-table striped="even" hover rounded class="tables rounded-lg overflow-hidden">
                <thead>
                    <tr class="table-header">
                        <td>
                        </td>
                        <td>
                            Projects for 2025
                        </td>
                    </tr>
                </thead>
                <thead>
                    <tr class="row-header">
                        <th class="text-left">
                        </th>
                        <th class="text-left">
                            Proponent
                        </th>
                        <th class="text-left">
                            Project Title
                        </th>
                        <th class="text-left">
                            Line Item Information
                        </th>
                        <th class="text-left">
                            Budgeting Information
                        </th>
                        <th class="text-left">
                            Date Information
                        </th>
                        <th class="text-left">
                            Progress & Status
                        </th>
                        <th class="text-left">
                            Expense Verification
                        </th>
                        <th class="text-left">
                            Action
                        </th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="item in desserts" :key="item.name">
                        <td>V</td>
                        <td>{{ item.name }}</td>
                        <td>{{ item.calories }}</td>
                        <td>{{ item.name }}</td>
                        <td>{{ item.calories }}</td>
                        <td>{{ item.name }}</td>
                        <td>{{ item.calories }}</td>
                        <td>{{ item.name }}</td>
                        <td>{{ item.calories }}</td>
                    </tr>
                </tbody>
            </v-table>
        </div>
    </section>
</template>
<script setup>
import { ref } from 'vue'
import { useTabs } from '@/composables/useTabs'
import TabsList from '@/components/TabsList.vue'

const { hasTabs } = useTabs()

const desserts = ref([
  {
    name: 'Frozen Yogurt',
    calories: 159,
  },
  {
    name: 'Ice cream sandwich',
    calories: 237,
  },
  {
    name: 'Eclair',
    calories: 262,
  },
  {
    name: 'Cupcake',
    calories: 305,
  },
  {
    name: 'Gingerbread',
    calories: 356,
  },
])
</script>