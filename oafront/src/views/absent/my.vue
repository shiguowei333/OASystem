<template>
  <el-space direction="vertical" fill :size="20" style="width: 100%;">
    <OAPageHeader content="个人考勤"></OAPageHeader>
    <el-card style="text-align: right;">
      <el-button type="primary" @click="onShowDialog"><el-icon>
          <Plus />
        </el-icon>发起考勤</el-button>
    </el-card>
  </el-space>
  <el-dialog v-model="dialogVisible" title="发起请假" width="500">
    <el-form :model="absentForm" :rules="rules" ref="absentFormRef">
      <el-form-item label="标题" :label-width="formLabelWidth" prop="title">
        <el-input v-model="absentForm.title" autocomplete="off" />
      </el-form-item>
      <el-form-item label="请假类型" :label-width="formLabelWidth" prop="absent_types">
        <el-select v-model="absentForm.absent_type_id" placeholder="请选择请假类型">
          <el-option v-for="item in absent_types" :label="item.name" :value="item.id" :key="item.name"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="请假时间" :label-width="formLabelWidth" prop="date_range">
        <el-date-picker v-model="absentForm.date_range" type="daterange" range-separator="到" start-placeholder="起始日期"
          end-placeholder="结束日期">
        </el-date-picker>
      </el-form-item>
      <el-form-item label="审批领导" :label-width="formLabelWidth">
        <el-input value="白展堂" readonly disabled />
      </el-form-item>
      <el-form-item label="请假理由" :label-width="formLabelWidth" prop="request_content">
        <el-input type="textarea"  v-model="absentForm.request_content"/>
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
import { ref, reactive } from 'vue'

let dialogVisible = ref(false)
let formLabelWidth = ref('100px')
let absentForm = reactive({
  title: '',
  absent_type_id: null,
  date_range: [],
  request_content: ''
})
let rules = reactive({
  title: [
    {required: true, message: '请输入标题', trigger: 'blur'},
  ],
  absent_types: [
    {required: true, message: '请选择请假类型', trigger: 'change'}
  ],
  date_range: [
    {required: true, message: '请选择请假时间', trigger: 'blur'}
  ],
  request_content: [
    {required: true, message: '请输入请假理由', trigger: 'blur'}
  ]
})

let absent_types = ref([])

const onShowDialog = () => {
  absentForm.title = ''
  absentForm.absent_type_id = null
  absentForm.date_range = []
  absentForm.request_content = ''
  dialogVisible.value = true
}

const onSubmit = () => {
  console.log(absentForm)
}
</script>

<style lang="scss" scoped></style>