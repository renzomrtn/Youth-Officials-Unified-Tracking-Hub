<template>
    <section class="content">
        <div class="tabs-list">
            <TabsList v-if="hasTabs" />
        </div>
        <div class="inner-content">
            <section>
                
            </section>
        </div>
    </section>
</template>
<script setup>
import { useTabs } from '@/composables/useTabs'
import TabsList from '@/components/TabsList.vue'

const { hasTabs } = useTabs()
</script>