import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

const USER_KEY = 'OA_USER_KEY'
const TOKEN_KEY = "OA_TOKEN_KEY"

export const userAuthStore = defineStore('auth', () => {
    let _user = ref({})
    let _token = ref("")

    function setUserToken(user, token) {
        _user.value = user
        _token.value = token

        localStorage.setItem(USER_KEY,JSON.stringify(user))
        localStorage.setItem(TOKEN_KEY,token)
    }

    let user = computed(() => {
        if(!_user.value) {
            _user.value = localStorage.getItem(USER_KEY)
        }
        return _user.value
    })

    let token = computed(() => {
        if(!_token.value) {
            _token.value = localStorage.getItem(TOKEN_KEY)
        }
        return _token.value
    })

    return { setUserToken, user, token}
})