<template>
    <main>
        <section class="branding">
            <div class="left">
                <img src="@/assets/youth-ims-logo.svg" alt="YOUTH Logo" width="150" height="150" />
            </div>
            <div class="right">
                <h1>title</h1>
                <h4>subtitle</h4>
            </div>
        </section>

        <section class="login">
            <div class="headline">
                <h2>Welcome Back</h2>
                <p>Please sign in to your account</p>
            </div>

            <div v-if="errorMessage" class="error-message">
                {{ errorMessage }}
            </div>

            <form @submit.prevent="handleLogin">
                <div class="inputs">
                    <div class="input-group">
                        <input type="text" id="username" v-model="username" placeholder="Enter your Username"
                            required />
                    </div>
                    <div class="input-group">
                        <input type="password" id="password" v-model="password" placeholder="Enter your Password"
                            required />
                    </div>
                </div>
                <div class="buttons">
                    <a href="#" class="forgot">Forgot Password?</a>
                    <button type="submit" :disabled="isLoading">
                        {{ isLoading ? 'Logging in...' : 'Login' }}
                    </button>
                </div>
            </form>
        </section>
    </main>
</template>
<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const username = ref('')
const password = ref('')
const errorMessage = ref('')
const isLoading = ref(false)

const API_URL = 'http://localhost:8000'

const handleLogin = async () => {
  errorMessage.value = ''
  isLoading.value = true
  
  try {
    const response = await fetch(`${API_URL}/api/login`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        username: username.value.trim(),
        password: password.value.trim(),
      }),
    })
    
    if (!response.ok) {
      const error = await response.json()
      throw new Error(error.detail || 'Login failed')
    }
    
    const data = await response.json()
    
    // Store the token (consider using a more secure method in production)
    localStorage.setItem('access_token', data.access_token)
    
    // Redirect to dashboard or home page
    router.push('/dashboard')
    
  } catch (error) {
    errorMessage.value = error.message
  } finally {
    isLoading.value = false
  }
}
</script>
<style scoped>
main {
    background-image: url('@/assets/login-bg.png');
    background-size: cover;
    background-position: center;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
    gap: 2rem;
}

.branding {
    display: flex;
    align-items: center;
    gap: 1rem;
    color: #000000;
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.7);
}

.login {
    background: rgba(255, 255, 255, 0.8);
    padding: 2rem;
    border-radius: 12px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    width: 100%;
    max-width: 400px;
    display: flex;
    ;
    flex-direction: column;
    gap: 2rem;
    justify-content: center;
}

.headline {
    text-align: center;
    display: flex;
    flex-direction: column;
}

form {
    display: flex;
    flex-direction: column;
    gap: 3rem;
}

.inputs {
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

input {
    width: 100%;
    padding: 1rem;
    border: #004fb6 1px solid;
    border-radius: 12px;
}

.buttons {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1rem;
}

.forgot {
    color: #f80f0f;
    text-decoration: none;
}

button {
    background-color: #004fb6;
    color: white;
    padding: 1rem;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    font-size: 1rem;
    width: 100%;
}
</style>