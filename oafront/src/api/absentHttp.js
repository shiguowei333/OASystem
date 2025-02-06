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

const getMyAbsents = (page=1) => {
  const path = `/absent/absent?who=my&page=${page}`
  return request.get(path)
}

const getSubAbsents = (page=1) => {
  const path = `/absent/absent?who=sub&page=${page}`
  return request.get(path)
}

export default {
  getAbsentTypes,
  getResponder,
  applyAbsent,
  getMyAbsents,
  getSubAbsents
}