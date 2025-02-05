<template>
    <el-space direction="vertical" fill :size="20" style="width: 100%;">
        <OAPageHeader content="个人考勤"></OAPageHeader>
        <el-card style="text-align: right;">
            <el-button type="primary"><el-icon>
                    <Plus />
                </el-icon>发起考勤</el-button>
        </el-card>
    </el-space>

</template>

<script setup name="myabsent">
import OAPageHeader from '@/components/OAPageHeader.vue';

</script>

<style lang="scss" scoped></style>