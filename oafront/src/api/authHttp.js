import request from '@/api/http'

const login = (email, password) => {
  const path  = '/auth/login'
  return request.post(path, {email, password})
}


export default {
  login
}