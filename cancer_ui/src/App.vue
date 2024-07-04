<script setup>
import { RouterView } from 'vue-router'
import NavBar from '@/components/NavBar.vue'
</script>

<template>
  <NavBar />

  <RouterView />
</template>

<style lang="scss">
@import '@/assets/styles/style.scss';
</style>
