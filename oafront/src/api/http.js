import axios from 'axios'
import { userAuthStore } from '@/stores/auth'

const request = axios.create({
  baseURL: import.meta.env.VITE_BASE_URL,
  timeout: 6000
})

request.interceptors.request.use(config => {
  const authStore = userAuthStore()
  const token = authStore.token
  if(token) {
    config.headers.Authorization = 'JWT ' + token
  }
  return config
})

export default request