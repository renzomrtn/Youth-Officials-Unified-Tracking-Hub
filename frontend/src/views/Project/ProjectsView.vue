<template>
    <section class="content">
        <div class="tabs-list">
            <TabsList v-if="hasTabs" />
        </div>
        <div class="inner-content">
            <section class="holder">
                <div class="wrapper">
                    <h1>Projects for 2025</h1>
                    <div class="toolbar">
                        <v-text-field label="Search Projects"></v-text-field>
                        <v-btn rounded>+ Add Project</v-btn>
                    </div>
                </div>
                <v-table striped="even" hover rounded class="tables rounded-lg overflow-hidden">
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
                            <td>{{ item.title }}</td>
                            <td>{{ item.lineitem }}</td>
                            <td>{{ item.budget }}</td>
                            <td>{{ item.date }}</td>
                            <td>{{ item.progress }}</td>
                            <td>{{ item.expense }}</td>
                            <td>{{ item.action }}</td>
                        </tr>
                    </tbody>
                </v-table>
                <v-pagination :length="4"></v-pagination>
            </section>
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
        name: 'Melody Marks',
        title: 'HIV/AIDS Awareness Seminar',
        lineitem: '123456',
        budget: 159,
        date: '1/1/2025',
        progress: '100%',
        expense: 'Pending',
        action: 'edit'
    },
    {
        name: 'Hazel Moore',
        title: 'Cleanup Drive',
        lineitem: '123457',
        budget: 159,
        date: '1/1/2025',
        progress: '100%',
        expense: 'Pending',
        action: 'edit'
    },
    {
        name: 'Valerica Steele',
        title: 'Tree Planting',
        lineitem: '123458',
        budget: 159,
        date: '1/1/2025',
        progress: '100%',
        expense: 'Pending',
        action: 'edit'
    },
    {
        name: 'Tru Kait',
        title: 'Cooking Seminar',
        lineitem: '123459',
        budget: 159,
        date: '1/1/2025',
        progress: '100%',
        expense: 'Pending',
        action: 'edit'
    },
    {
        name: 'Eden Ivy',
        title: 'Resume Making / Job Application Seminar',
        lineitem: '123455',
        budget: 159,
        date: '1/1/2025',
        progress: '100%',
        expense: 'Pending',
        action: 'edit'
    },
])
</script>