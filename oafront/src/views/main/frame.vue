<template>
    <el-container class="container">
      <el-aside class="aside" width="200px">
        <router-link to="/" class="brand">OA管理系统</router-link>
      </el-aside>
      <el-container>
        <el-header class="header">Header</el-header>
        <el-main class="main">Main</el-main>
      </el-container>
    </el-container>
</template>

<script setup name="frame">

</script>

<style scoped>
  .container {
    height: 100vh;
    background-color: #f4f6f9;
  }
  .aside {
    background-color: #343a40;
    box-shadow: 0 14px 28px rgba(0,0,0, .25), 0 10px 10px rgba(0,0,0, .22) !important;
  }
  .aside .brand {
    color: #fff;
    text-decoration: none;
    border-bottom: 1px solid #434a50;
    background-color: #232631;
    height: 60px;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 20px;
  }
  .header {
    height: 60px;
    background-color: #fff;
    border-bottom: 1px solid #e6e6e6;
  }
</style>