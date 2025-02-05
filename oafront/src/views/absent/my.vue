<template>
    <el-space direction="vertical" fill :size="20" style="width: 100%;">
        <OAPageHeader content="个人考勤"></OAPageHeader>
        <el-card style="text-align: right;">
            <el-button type="primary"><el-icon>
                    <Plus />
                </el-icon>发起考勤</el-button>
        </el-card>
    </el-space>
    <el-dialog v-model="dialogVisible" title="发起请假" width="500">
        <el-form :model="absentForm" :rules="rules" ref="formTag">
            <el-form-item label="标题" :label-width="formLabelWidth" prop="title">
                <el-input v-model="absentForm.title" autocomplete="off" />
            </el-form-item>
            <el-form-item label="请假类型" :label-width="formLabelWidth">
                <el-option v-for="item in absent_types" :label="item.name" :value="item.id" :key="item.name" />
            </el-form-item>
        </el-form>
        <template #footer>
            <div class=" dialog-footer">
                <el-button @click="dialogVisible = false">取消</el-button>
                <el-button type="primary" @click="onSubmit">
                    确认
                </el-button>
            </div>
        </template>
    </el-dialog>
</template>

<script setup name="myabsent">
import OAPageHeader from '@/components/OAPageHeader.vue';
import { ref,reactive } from 'vue'

let dialogVisible = ref(false)
let formLabelWidth = ref('100px')
let absentForm = reactive({
    title: '',
    absent_type_id: null,
    start_date: '',
    end_date: '',
    request_content: ''
})
let absent_types = ref([])
</script>

<style lang="scss" scoped></style>