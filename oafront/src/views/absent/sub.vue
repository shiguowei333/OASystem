<template>
    <OAMain title="下属考勤">
        <el-card>
            <el-table :data="absents" style="width: 100%;">
                <el-table-column prop="title" label="标题" />
                <el-table-column prop="absent_type.name" label="类型" />
                <el-table-column prop="request_content" label="原因" />
                <el-table-column label="发起时间">
                    <template #default="scope">
                        {{ timeFormatter.stringFromDateTime(scope.row.create_time) }}
                    </template>
                </el-table-column>
                <el-table-column prop="start_date" label="开始日期" />
                <el-table-column prop="end_date" label="结束日期" />
                <el-table-column prop="responder.real_name" label="审核领导" />
                <el-table-column prop="response_content" label="反馈意见" />
                <el-table-column label="审核状态">
                    <template #default="scope">
                        <el-tag type="info" v-if="scope.row.status == 1">审核中</el-tag>
                        <el-tag type="success" v-else-if="scope.row.status == 2">已通过</el-tag>
                        <el-tag type="danger" v-else>已拒绝</el-tag>
                    </template>
                </el-table-column>
                <el-table-column label="处理">
                    <template #default="scope">
                        <el-button v-if="scope.row.status == 1" type="primary" icon="EditPen" @click="onShowDialog" />
                        <el-button v-else type="default" icon="EditPen" disabled>已处理</el-button>
                    </template>
                </el-table-column>
            </el-table>
            <template #footer>
                <!-- <el-pagination background layout="prev, pager, next" :total="pagination.total"
                    v-model:current-page="pagination.page" :page-size="10" /> -->
                    <OAPagination v-model="pagination.page" :total="pagination.total"></OAPagination>
            </template>
        </el-card>
    </OAMain>
    <OADialog title="考勤审核" v-model="dialogVisible" @submit="onSumitAbsent" label-width="100px">
      <el-form :model="absentForm" :rules="rules" ref="absentFormRef">
      <el-form-item label="结果"  prop="status">
        <el-radio-group v-model="absentForm.status" class="ml-4">
          <el-radio :value="2" >通过</el-radio>
          <el-radio :value="3" >拒绝</el-radio>
        </el-radio-group>        
      </el-form-item>
      <el-form-item label="理由" size="normal" prop="response_content">
        <el-input type="textarea" v-model="absentForm.response_content" />
      </el-form-item>
    </el-form>
    </OADialog>
</template>

<script setup name="myabsent">
import OAMain from '@/components/OAMain.vue'
import timeFormatter from '@/utils/timeFormatter'
import absentHttp from '@/api/absentHttp'
import { ref, reactive, onMounted, computed } from 'vue'
import { ElMessage } from 'element-plus'
import OAPagination from '@/components/OAPagination.vue'
import OADialog from '@/components/OADialog.vue'

let absents = ref([])
let pagination = reactive({
    total: 0,
    page: 1
})
let absentFormRef = ref()
let dialogVisible = ref(false)
let absentForm = reactive({
  status: 2,
  response_content: ''
})
let rules = reactive({
  status: [{required: true, message: '请选择处理结果！', trigger: 'change'}],
  response_content: [{required: true, message: '请输入理由！', trigger: "blur"}]
})

const onSumitAbsent = () => {

}

const onShowDialog = () => {
  dialogVisible.value = true
}

onMounted(async() => {
  let result = await absentHttp.getSubAbsents()
  if(result.status == 200) {
    pagination.total = result.data.count
    absents.value = result.data.results
  }
})

</script>

<style scoped>
.el-pagination {
    justify-content: right;
}
</style>