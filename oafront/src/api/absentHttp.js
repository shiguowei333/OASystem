import request from '@/api/http'

const getAbsentTypes = () => {
  const path = '/absent/type'
  return request.get(path)
}

const getResponder = () => {
  const path = '/absent/responder'
  return request.get(path)
}

const applyAbsent = (data) => {
  const path = '/absent/absent'
  return request.post(path, data)
}

export default {
  getAbsentTypes,
  getResponder,
  applyAbsent
}