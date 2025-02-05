import request from '@/api/http'

const getAbsentTypes = () => {
  const path = '/absent/type'
  return request.get(path)
}

const getResponder = () => {
  const path = '/absent/responder'
  return request.get(path)
}

export default {
  getAbsentTypes,
  getResponder
}