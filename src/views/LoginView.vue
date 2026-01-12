<template>
    <main>
        <section>
            <div class="left">
                <img src="@/assets/youth-ims-logo.svg" alt="YOUTH Logo" width="150" height="150" />
            </div>
            <div class="right">
                <h1>YOUTH</h1>
                <h4>Youth Officials' Unified Transparency Hub</h4>
            </div>
        </section>

        <section>
            <form>
                <div class="input-group">
                    <label for="username">Username</label>
                    <input type="text" id="username" name="username" required />
                </div>
                <div class="input-group">
                    <label for="password">Password</label>
                    <input type="password" id="password" name="password" required />
                </div>
                <button type="submit">Login</button>
            </form>
        </section>
    </main>
</template>
<style scoped>
main {
    background-image: url('@/assets/login-bg.jpg');
    background-size: cover;
    background-position: center;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
    gap: 2rem;
}
</style>