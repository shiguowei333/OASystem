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

const handleSubAbsent = (absent_id, status, response_content) => {
  const path = `/absent/absent/${absent_id}`
  return request.put(path,{status, response_content})
}

export default {
  getAbsentTypes,
  getResponder,
  applyAbsent,
  getMyAbsents,
  getSubAbsents,
  handleSubAbsent
}