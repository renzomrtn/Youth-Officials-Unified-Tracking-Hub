<template>
    <section class="content">
        <div class="tabs-list">
            <TabsList v-if="hasTabs" />
        </div>
        <div class="inner-content">
            <section>
                <div class="top">
                    <h1>Certificate Generator</h1>
                    <p>Upload your CSV data and certificate template, then position and resize the name field</p>
                </div>
                <div class="mid">
                    
                </div>
                <div class="bot">
                    
                </div>
            </section>
        </div>
    </section>
</template>
<script setup>
import { useTabs } from '@/composables/useTabs'
import TabsList from '@/components/TabsList.vue'

const { hasTabs } = useTabs()
</script>