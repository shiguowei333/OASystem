<template>
  <el-container class="container">
    <el-aside class="aside" :width="asideWidth">
      <router-link to="/" class="brand">OA<span v-show="!isCollapse">管理系统</span></router-link>
      <el-menu active-text-color="#ffd04b" background-color="#343a40" class="el-menu-vertical-demo" default-active="1"
        text-color="#fff" :collapse="isCollapse" :collapse-transition="false">
        <el-menu-item index="1">
          <el-icon>
            <HomeFilled />
          </el-icon>
          <span>首页</span>
        </el-menu-item>
        <el-sub-menu index="2">
          <template #title>
            <el-icon>
              <Checked />
            </el-icon>
            <span>考勤管理</span>
          </template>
          <el-menu-item index="2-1">
            <el-icon>
              <UserFilled />
            </el-icon>
            <span>个人考勤</span>
          </el-menu-item>
          <el-menu-item index="2-2">
            <el-icon>
              <User />
            </el-icon>
            <span>下属考勤</span>
          </el-menu-item>
        </el-sub-menu>
        <el-sub-menu index="3">
          <template #title>
            <el-icon>
              <BellFilled />
            </el-icon>
            <span>通知管理</span>
          </template>
          <el-menu-item index="3-1">
            <el-icon>
              <CirclePlusFilled />
            </el-icon>
            <span>发布通知</span>
          </el-menu-item>
          <el-menu-item index="3-2">
            <el-icon>
              <List />
            </el-icon>
            <span>通知列表</span>
          </el-menu-item>
        </el-sub-menu>
        <el-sub-menu index="4">
          <template #title>
            <el-icon>
              <Avatar />
            </el-icon>
            <span>员工管理</span>
          </template>
          <el-menu-item index="4-1">
            <el-icon>
              <CirclePlusFilled />
            </el-icon>
            <span>新增员工</span>
          </el-menu-item>
          <el-menu-item index="4-2">
            <el-icon>
              <List />
            </el-icon>
            <span>员工列表</span>
          </el-menu-item>
        </el-sub-menu>
      </el-menu>
    </el-aside>
    <el-container>
      <el-header class="header">
        <div class="left-header">
          <el-button :icon="isCollapse ? 'Expand' : 'Fold'" @click="onCollapseAside"></el-button>
        </div>
        <el-dropdown>
          <span class="el-dropdown-link">
            <el-avatar :size="30" :icon="UserFilled"></el-avatar>
            <span style="margin-left: 10px;">[{{ authStore.user.department.name }}]{{ authStore.user.real_name }}</span>
            <el-icon class="el-icon--right">
              <arrow-down />
            </el-icon>
          </span>
          <template #dropdown>
            <el-dropdown-menu>
              <el-dropdown-item @click="showResetPwdDialog">修改密码</el-dropdown-item>
              <el-dropdown-item @click="onLogout">退出登录</el-dropdown-item>
            </el-dropdown-menu>
          </template>
        </el-dropdown>
      </el-header>
      <el-main class="main">Main</el-main>
    </el-container>
  </el-container>
  <el-dialog v-model="dialogVisible" title="修改密码" width="500">
    <el-form :model="restForm" :rules="rules" ref="formTag">
      <el-form-item label="旧密码" :label-width="formLabelWidth" prop="oldpwd">
        <el-input v-model="restForm.oldpwd" autocomplete="off" type="password" />
      </el-form-item>
      <el-form-item label=" 新密码" :label-width="formLabelWidth" prop="pwd1">
          <el-input v-model="restForm.pwd1" autocomplete="off" type="password" />
      </el-form-item>
      <el-form-item label=" 确认密码" :label-width="formLabelWidth" prop="pwd2">
            <el-input v-model="restForm.pwd2" autocomplete="off" type="password" />
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

<script setup name="frame">
import { ref, computed } from 'vue'
import { Expand, Fold, UserFilled } from '@element-plus/icons-vue'
import { userAuthStore } from '@/stores/auth'
import { useRouter } from 'vue-router'
import { reactive } from 'vue'
import authHttp from '@/api/authHttp'
import { ElMessage } from 'element-plus'

const authStore = userAuthStore()
const $router = useRouter()

let isCollapse = ref(false)
let asideWidth = computed(() => {
  if (isCollapse.value) {
    return '64px'
  } else {
    return '250px'
  }
})

let dialogVisible = ref(false)
let restForm = reactive({
  oldpwd: '',
  pwd1: '',
  pwd2: ''
})
let formTag = ref()

let rules = reactive({
  oldpwd: [
    { required: true, message: '请输入旧的密码', trigger: 'blur' },
    { min: 6, max: 20, message: '密码长度需再6-20位', trigger: 'blur' }
  ],
  pwd1: [
    { required: true, message: '请输入新的密码', trigger: 'blur' },
    { min: 6, max: 20, message: '密码长度需要满足6-20位', trigger: 'blur' }
  ],
  pwd2: [
    { required: true, message: '请输入确认密码', trigger: 'blur' },
    { min: 6, max: 20, message: '密码长度需要满足6-20位', trigger: 'blur' }
  ]
})

let formLabelWidth = '80px'

const onCollapseAside = () => {
  isCollapse.value = !isCollapse.value
}

const onLogout = () => {
  authStore.clearUserToken()
  $router.push({ name: 'login' })
}

const onSubmit = () => {
  formTag.value.validate(async(valid, fields) => {
    if(valid) {
      try {
        let result = await authHttp.resetPwd(restForm.oldpwd, restForm.pwd1, restForm.pwd2)
        if(result.status == 200) {
          ElMessage.success('密码修改成功！')
          dialogVisible.value = false
        }
      } catch (error) {
        ElMessage.error('密码修改失败!')
      }
    }else {
      ElMessage.info('输入密码不符合要求')
    }
  })
}

const showResetPwdDialog = () => {
  restForm.oldpwd = ''
  restForm.pwd1 = ''
  restForm.pwd2 = ''
  dialogVisible.value = true
}
</script>

<style scoped>
.container {
  height: 100vh;
  background-color: #f4f6f9;
}

.aside {
  background-color: #343a40;
  box-shadow: 0 14px 28px rgba(0, 0, 0, .25), 0 10px 10px rgba(0, 0, 0, .22) !important;
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
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.el-dropdown-link {
  display: flex;
  align-items: center;
}

.el-menu {
  border-right: none;
}
</style>